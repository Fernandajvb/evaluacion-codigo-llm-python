"""Produce tablas descriptivas a partir de los resultados ya evaluados."""

from __future__ import annotations

import csv
import json
from collections import Counter, defaultdict
from pathlib import Path
from statistics import median

import lizard


ROOT = Path(__file__).resolve().parent
RESULTS = ROOT / "results" / "principal"


def normalized_path(path: Path) -> str:
    return str(path.resolve()).casefold()


def semgrep_counts() -> dict[str, Counter[str]]:
    data = json.loads((RESULTS / "semgrep_principal.json").read_text(encoding="utf-8"))
    counts: dict[str, Counter[str]] = defaultdict(Counter)
    for finding in data["results"]:
        path = finding["path"]
        # Las tareas de seguridad tienen directorios SEC-CWE-...; MBPP no entra aquí.
        if "\\sec-" not in path.casefold() and "/sec-" not in path.casefold():
            continue
        severity = finding["extra"].get("severity", "INFO")
        counts[normalized_path(Path(path))][severity] += 1
    return counts


def lizard_metrics(path: Path, syntax_status: str) -> tuple[float | str, float | str]:
    if syntax_status != "valido" or not path.exists():
        return "", ""
    try:
        analysis = lizard.analyze_file(str(path))
        return analysis.nloc, sum(function.cyclomatic_complexity for function in analysis.function_list)
    except (OSError, UnicodeError):
        return "", ""


def main() -> None:
    rows = list(csv.DictReader((RESULTS / "resultados_principal.csv").open(encoding="utf-8")))
    findings = semgrep_counts()
    for row in rows:
        code_path = ROOT / Path(row["code_file"])
        severity_counts = findings.get(normalized_path(code_path), Counter()) if row["family"] == "seguridad" else Counter()
        row["semgrep_error"] = severity_counts["ERROR"]
        row["semgrep_warning"] = severity_counts["WARNING"]
        row["semgrep_info"] = severity_counts["INFO"]
        nloc, ccn = lizard_metrics(code_path, row["syntax_status"])
        row["lizard_nloc"] = nloc
        row["lizard_ccn_total"] = ccn

    detailed_path = RESULTS / "resultados_detallados.csv"
    with detailed_path.open("w", encoding="utf-8", newline="") as output:
        writer = csv.DictWriter(output, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)

    groups: dict[tuple[str, str, str], list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        groups[(row["family"], row["model"], row["condition"])].append(row)
    summaries: list[dict[str, object]] = []
    for (family, model, condition), group in sorted(groups.items()):
        valid = sum(row["syntax_status"] == "valido" for row in group)
        nloc_values = [float(row["lizard_nloc"]) for row in group if row["lizard_nloc"] != ""]
        ccn_values = [float(row["lizard_ccn_total"]) for row in group if row["lizard_ccn_total"] != ""]
        summaries.append({
            "family": family,
            "model": model,
            "condition": condition,
            "samples": len(group),
            "syntax_valid": valid,
            "syntax_valid_pct": round(100 * valid / len(group), 1),
            "mbpp_pass": sum(row["mbpp_test_status"] == "pasa" for row in group),
            "mbpp_fail": sum(row["mbpp_test_status"] == "falla" for row in group),
            "mbpp_not_run_policy": sum(row["mbpp_test_status"] == "no_ejecutado_por_politica" for row in group),
            "security_blocking_findings": sum(int(row["semgrep_error"]) + int(row["semgrep_warning"]) for row in group),
            "security_info_signals": sum(int(row["semgrep_info"]) for row in group),
            "median_nloc": round(median(nloc_values), 1) if nloc_values else "",
            "median_ccn": round(median(ccn_values), 1) if ccn_values else "",
        })
    summary_path = RESULTS / "resumen_resultados.csv"
    with summary_path.open("w", encoding="utf-8", newline="") as output:
        writer = csv.DictWriter(output, fieldnames=list(summaries[0]))
        writer.writeheader()
        writer.writerows(summaries)

    lines = ["# Resultados experimentales (descriptivos)", "", "Los hallazgos de seguridad se contabilizan solo para las tareas SecurityEval. `security_blocking_findings` suma severidades ERROR y WARNING; las señales INFO se informan aparte.", "", "| Familia | Modelo | Prompt | Válidas | MBPP pasan | Hallazgos bloqueantes | Mediana NLOC | Mediana CCN |", "|---|---|---|---:|---:|---:|---:|---:|"]
    for row in summaries:
        lines.append(
            f"| {row['family']} | {row['model']} | {row['condition']} | "
            f"{row['syntax_valid']}/{row['samples']} ({row['syntax_valid_pct']}%) | "
            f"{row['mbpp_pass']} | {row['security_blocking_findings']} | "
            f"{row['median_nloc']} | {row['median_ccn']} |"
        )
    (RESULTS / "resumen_resultados.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Archivos creados: {detailed_path.name}, {summary_path.name}, resumen_resultados.md")


if __name__ == "__main__":
    main()
