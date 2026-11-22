"""Evalúa respuestas ya obtenidas; este programa nunca llama a OpenRouter.

Las tareas MBPP se prueban solo si el código supera una barrera conservadora de
seguridad. Las tareas SecurityEval nunca se ejecutan: quedan disponibles para
Semgrep y Lizard después de la extracción.
"""

from __future__ import annotations

import argparse
import ast
import csv
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile


CODE_BLOCK = re.compile(r"```(?:python)?\s*\n(.*?)```", re.DOTALL | re.IGNORECASE)
ALLOWED_IMPORTS = {
    "bisect", "collections", "copy", "decimal", "fractions", "functools",
    "heapq", "itertools", "math", "operator", "re", "statistics", "string",
}
BLOCKED_CALLS = {
    "__import__", "breakpoint", "compile", "eval", "exec", "exit", "getattr",
    "globals", "help", "input", "locals", "open", "quit", "setattr",
}


def slug(value: str) -> str:
    return re.sub(r"[^a-zA-Z0-9]+", "_", value).strip("_").lower()


def extract_code(content: str) -> str:
    """Extract the first fenced block when present; otherwise preserve the response."""
    blocks = CODE_BLOCK.findall(content)
    return (blocks[0] if blocks else content).strip() + "\n"


def syntax_status(code: str, filename: str) -> str:
    if not code.strip():
        return "sin_codigo"
    try:
        compile(code, filename, "exec")
    except SyntaxError:
        return "error_sintaxis"
    return "valido"


def mbpp_execution_policy(code: str) -> tuple[bool, str]:
    """Return whether code is eligible for a local MBPP test subprocess.

    This is a risk reduction, not a security sandbox. It intentionally blocks
    APIs unrelated to the selected pure-function MBPP tasks.
    """
    try:
        tree = ast.parse(code)
    except SyntaxError:
        return False, "error_sintaxis"
    for node in ast.walk(tree):
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            modules = [alias.name.split(".")[0] for alias in node.names]
            if isinstance(node, ast.ImportFrom) and node.module:
                modules.append(node.module.split(".")[0])
            disallowed = [module for module in modules if module not in ALLOWED_IMPORTS]
            if disallowed:
                return False, f"importacion_no_permitida:{disallowed[0]}"
        if isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name) and node.func.id in BLOCKED_CALLS:
                return False, f"llamada_no_permitida:{node.func.id}"
            if isinstance(node.func, ast.Attribute) and node.func.attr in {"system", "popen", "run", "Popen", "connect", "request", "urlopen"}:
                return False, f"llamada_no_permitida:{node.func.attr}"
    return True, "permitido"


def run_mbpp_pytest(code: str, tests: list[str]) -> tuple[str, str]:
    """Run official MBPP assertions in a short-lived isolated working directory."""
    allowed, reason = mbpp_execution_policy(code)
    if not allowed:
        return "no_ejecutado_por_politica", reason
    with tempfile.TemporaryDirectory(prefix="paper_llm_mbpp_") as directory:
        working = Path(directory)
        (working / "solution.py").write_text(code, encoding="utf-8")
        indented_tests = "\n".join(f"    {test}" for test in tests)
        body = "from solution import *\n\n\ndef test_reference():\n" + indented_tests + "\n"
        (working / "test_reference.py").write_text(body, encoding="utf-8")
        environment = {
            "PATH": os.environ.get("PATH", ""),
            "PYTHONDONTWRITEBYTECODE": "1",
            "PYTHONNOUSERSITE": "1",
            # The MBPP assertions do not need third-party pytest plug-ins.
            "PYTEST_DISABLE_PLUGIN_AUTOLOAD": "1",
        }
        try:
            completed = subprocess.run(
                [sys.executable, "-m", "pytest", "-q", "-p", "no:cacheprovider", "test_reference.py"],
                cwd=working,
                env=environment,
                capture_output=True,
                text=True,
                timeout=5,
                check=False,
            )
        except subprocess.TimeoutExpired:
            return "tiempo_agotado", "pytest_supero_5_segundos"
    details = (completed.stdout + completed.stderr).replace("\x00", " ").strip()
    return ("pasa" if completed.returncode == 0 else "falla"), details[-1000:]


def content_from_record(record: dict[str, object]) -> str:
    response = record.get("response", {})
    if not isinstance(response, dict):
        return ""
    choices = response.get("choices", [])
    if not isinstance(choices, list) or not choices:
        return ""
    first = choices[0] if isinstance(choices[0], dict) else {}
    message = first.get("message", {}) if isinstance(first, dict) else {}
    content = message.get("content", "") if isinstance(message, dict) else ""
    return content if isinstance(content, str) else ""


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True, help="JSONL de respuestas del experimento")
    parser.add_argument("--retries", type=Path, default=Path("runs/principal/reintento_truncadas.jsonl"))
    parser.add_argument("--selection", type=Path, default=Path("data/selection/seleccion_tareas.json"))
    parser.add_argument("--generated-dir", type=Path, default=Path("results/principal/generated"))
    parser.add_argument("--summary", type=Path, default=Path("results/principal/resultados_principal.csv"))
    args = parser.parse_args()

    selection = json.loads(args.selection.read_text(encoding="utf-8"))
    tasks = {task["experiment_id"]: task for task in selection["tasks"]}
    records = [json.loads(line) for line in args.input.read_text(encoding="utf-8").splitlines() if line.strip()]
    retries_by_case: dict[tuple[str, str, str], dict[str, object]] = {}
    if args.retries.exists():
        retries = [json.loads(line) for line in args.retries.read_text(encoding="utf-8").splitlines() if line.strip()]
        retries_by_case = {
            (str(row["case"]["task_id"]), str(row["case"]["model"]), str(row["case"]["condition"])): row
            for row in retries
            if row.get("http_status") == 200 and isinstance(row.get("case"), dict)
        }
    args.generated_dir.mkdir(parents=True, exist_ok=True)
    summaries: list[dict[str, object]] = []

    for number, initial_record in enumerate(records, start=1):
        initial_case = initial_record.get("case", {})
        if not isinstance(initial_case, dict):
            continue
        retry_key = (str(initial_case.get("task_id")), str(initial_case.get("model")), str(initial_case.get("condition")))
        record = retries_by_case.get(retry_key, initial_record)
        case = record.get("case", {})
        if not isinstance(case, dict):
            continue
        task_id = case.get("task_id")
        task = tasks.get(task_id)
        if task is None:
            raise ValueError(f"Tarea desconocida en respuestas: {task_id!r}")
        model = str(case.get("model", ""))
        condition = str(case.get("condition", ""))
        content = content_from_record(record)
        code = extract_code(content)
        folder = args.generated_dir / str(task_id)
        folder.mkdir(parents=True, exist_ok=True)
        code_path = folder / f"{slug(model)}__{slug(condition)}.py"
        code_path.write_text(code, encoding="utf-8")
        status = syntax_status(code, str(code_path))
        mbpp_status = "no_aplica"
        mbpp_details = ""
        if task["family"] == "algoritmica" and status == "valido":
            reference_tests = task.get("reference_tests", [])
            mbpp_status, mbpp_details = run_mbpp_pytest(code, reference_tests if isinstance(reference_tests, list) else [])
        response = record.get("response", {})
        usage = response.get("usage", {}) if isinstance(response, dict) else {}
        summaries.append({
            "task_id": task_id,
            "family": task["family"],
            "source_dataset": task["source_dataset"],
            "source_id": task["source_id"],
            "cwe": task.get("cwe", ""),
            "model": model,
            "condition": condition,
            "attempt": record.get("attempt", 1),
            "retry_reason": record.get("retry_reason", ""),
            "http_status": record.get("http_status", ""),
            "code_file": str(code_path),
            "syntax_status": status,
            "mbpp_test_status": mbpp_status,
            "mbpp_test_details": mbpp_details,
            "prompt_tokens": usage.get("prompt_tokens", "") if isinstance(usage, dict) else "",
            "completion_tokens": usage.get("completion_tokens", "") if isinstance(usage, dict) else "",
            "cost_usd": usage.get("cost", "") if isinstance(usage, dict) else "",
            "elapsed_seconds": record.get("elapsed_seconds", ""),
        })
        if number % 20 == 0:
            print(f"Procesadas {number}/{len(records)} respuestas...", flush=True)

    args.summary.parent.mkdir(parents=True, exist_ok=True)
    with args.summary.open("w", encoding="utf-8", newline="") as output:
        writer = csv.DictWriter(output, fieldnames=list(summaries[0]) if summaries else ["task_id"])
        writer.writeheader()
        writer.writerows(summaries)
    print(f"Evaluadas {len(summaries)} respuestas; resumen: {args.summary}", flush=True)


if __name__ == "__main__":
    main()
