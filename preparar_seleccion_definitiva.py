"""Construye el manifiesto reproducible de las 40 tareas del experimento.

No modifica los conjuntos fuente. Copia al manifiesto la consigna original y,
en MBPP, sus pruebas de referencia. Ejecutar después de descargar los datasets.
"""

from __future__ import annotations

import csv
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent
DATASETS = ROOT / "datasets"
SELECTION = ROOT / "data" / "selection"

# Subconjunto predefinido antes de ejecutar la evaluación principal.
# MBPP: funciones autocontenidas, con >= 3 pruebas de referencia y variedad
# de estructuras/operaciones. SecurityEval: un caso por CWE, evitando duplicados.
MBPP_IDS = [
    2, 4, 6, 8, 12, 18, 19, 57, 61, 63,
    65, 68, 69, 75, 83, 87, 88, 90, 91, 805,
]
SECURITYEVAL_IDS = [
    "CWE-020_author_1.py",  # carga YAML no segura
    "CWE-022_codeql_2.py",  # path traversal al extraer TAR
    "CWE-078_author_1.py",  # inyección de comandos
    "CWE-089_author_1.py",  # inyección SQL
    "CWE-094_author_1.py",  # ejecución dinámica de código
    "CWE-116_codeql_1.py",  # neutralización de salida
    "CWE-117_author_1.py",  # inyección en logs
    "CWE-193_author_1.py",  # límite/off-by-one
    "CWE-209_codeql_1.py",  # exposición de información en errores
    "CWE-259_author_1.py",  # contraseña embebida
    "CWE-295_author_1.py",  # validación TLS incorrecta
    "CWE-327_codeql_4.py",  # algoritmo criptográfico débil
    "CWE-330_author_1.py",  # aleatoriedad insegura
    "CWE-347_sonar_1.py",   # verificación JWT incorrecta
    "CWE-377_codeql_1.py",  # archivo temporal inseguro
    "CWE-385_mitre_1.py",   # comparación de secretos no constante
    "CWE-502_codeql_1.py",  # deserialización insegura
    "CWE-611_sonar_1.py",   # XXE
    "CWE-730_author_1.py",  # expresión regular insegura
    "CWE-759_mitre_1.py",   # hash de contraseña débil
]


def main() -> None:
    mbpp = json.loads((DATASETS / "mbpp_sanitized.json").read_text(encoding="utf-8"))
    securityeval = [
        json.loads(line)
        for line in (DATASETS / "securityeval_v2_1.jsonl").read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    mbpp_by_id = {item["task_id"]: item for item in mbpp}
    sec_by_id = {item["ID"]: item for item in securityeval}

    if len(MBPP_IDS) != 20 or len(set(MBPP_IDS)) != 20:
        raise ValueError("La selección MBPP debe contener exactamente 20 IDs únicos.")
    if len(SECURITYEVAL_IDS) != 20 or len(set(SECURITYEVAL_IDS)) != 20:
        raise ValueError("La selección SecurityEval debe contener exactamente 20 IDs únicos.")

    tasks: list[dict[str, object]] = []
    for task_id in MBPP_IDS:
        item = mbpp_by_id[task_id]
        tests = item.get("test_list", [])
        if len(tests) < 3:
            raise ValueError(f"MBPP {task_id} no tiene al menos tres pruebas.")
        tasks.append({
            "experiment_id": f"ALG-{task_id:03d}",
            "family": "algoritmica",
            "source_dataset": "sanitized MBPP",
            "source_id": task_id,
            "prompt_original": item["prompt"],
            "reference_tests": tests,
            "test_imports": item.get("test_imports", []),
        })

    for source_id in SECURITYEVAL_IDS:
        item = sec_by_id[source_id]
        tasks.append({
            "experiment_id": f"SEC-{source_id.removesuffix('.py')}",
            "family": "seguridad",
            "source_dataset": "SecurityEval v2.1",
            "source_id": source_id,
            "cwe": source_id.split("_")[0],
            "prompt_original": item["Prompt"],
            "reference_insecure_code": item["Insecure_code"],
        })

    manifest = {
        "description": "Selección congelada antes de la evaluación principal.",
        "selection_rules": {
            "algorithmic": "Tareas autocontenidas de sanitized MBPP, con al menos tres pruebas de referencia y diversidad de operaciones.",
            "security": "Una tarea de SecurityEval v2.1 por CWE, para cubrir veinte categorías de debilidades sin duplicar una categoría.",
        },
        "task_count": len(tasks),
        "tasks": tasks,
    }
    SELECTION.mkdir(parents=True, exist_ok=True)
    (SELECTION / "seleccion_tareas.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    with (SELECTION / "seleccion_tareas.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=["experiment_id", "family", "source_dataset", "source_id", "cwe", "prompt_original"])
        writer.writeheader()
        for task in tasks:
            writer.writerow({field: task.get(field, "") for field in writer.fieldnames})
    print(f"Selección creada: {len(tasks)} tareas (20 algorítmicas y 20 de seguridad).")


if __name__ == "__main__":
    main()
