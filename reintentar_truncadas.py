"""Reintenta una sola vez las respuestas cuyo proveedor marcó como truncadas.

Los datos originales nunca se modifican: cada reintento conserva su razón y
queda en un JSONL independiente para trazabilidad.
"""

from __future__ import annotations

import argparse
import copy
import json
import os
from pathlib import Path

from generar_experimento import case_key, collect


def was_truncated(record: dict[str, object]) -> bool:
    response = record.get("response", {})
    if not isinstance(response, dict):
        return False
    choices = response.get("choices", [])
    if not isinstance(choices, list) or not choices or not isinstance(choices[0], dict):
        return False
    return choices[0].get("finish_reason") == "length"


def previous_keys(output: Path) -> set[tuple[str, str, str]]:
    if not output.exists():
        return set()
    rows = [json.loads(line) for line in output.read_text(encoding="utf-8").splitlines() if line.strip()]
    return {case_key(row["case"]) for row in rows if isinstance(row.get("case"), dict)}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=Path("runs/principal/primer_intento.jsonl"))
    parser.add_argument("--output", type=Path, default=Path("runs/principal/reintento_truncadas.jsonl"))
    parser.add_argument("--run", action="store_true", help="Autoriza las llamadas pagadas de reintento.")
    args = parser.parse_args()

    originals = [json.loads(line) for line in args.input.read_text(encoding="utf-8").splitlines() if line.strip()]
    truncated = [row for row in originals if was_truncated(row)]
    existing = previous_keys(args.output)
    pending = [row for row in truncated if case_key(row["case"]) not in existing]
    print(f"Truncadas detectadas: {len(truncated)}; ya reintentadas: {len(existing)}; pendientes: {len(pending)}.")
    if not args.run:
        print("Vista previa solamente. Usa --run para iniciar los reintentos.")
        return
    key = os.getenv("OPENROUTER_API_KEY")
    if not key:
        parser.error("No se encontró OPENROUTER_API_KEY en esta sesión.")

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("a", encoding="utf-8") as output:
        for number, original in enumerate(pending, start=1):
            request = copy.deepcopy(original["request"])
            request["max_tokens"] = 8192
            result = collect(key, request)
            record = {
                "case": original["case"],
                "request": request,
                "attempt": 2,
                "retry_reason": "finish_reason_length_en_intento_inicial",
                "initial_record_file": args.input.name,
                **result,
            }
            output.write(json.dumps(record, ensure_ascii=False) + "\n")
            output.flush()
            case = original["case"]
            print(f"{number}/{len(pending)} | {case['task_id']} | {case['model']} | {case['condition']} | {result.get('http_status', 'error')}", flush=True)
            if result.get("http_status") in (401, 402, 403, 429):
                print("Se detuvo para conservar los registros y revisar el estado de la cuenta.")
                return


if __name__ == "__main__":
    main()
