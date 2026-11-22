$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent $MyInvocation.MyCommand.Path

# No llama a OpenRouter ni consume créditos: usa respuestas ya registradas.
& "$root\.venv\Scripts\python.exe" "$root\evaluar_respuestas.py" --input "$root\runs\principal\primer_intento.jsonl"
& "$root\.venv\Scripts\semgrep.exe" --config "$root\rules\securityeval.yml" --json --output "$root\results\principal\semgrep_principal.json" "$root\results\principal\generated"
& "$root\.venv\Scripts\lizard.exe" "$root\results\principal\generated" | Out-File -Encoding utf8 "$root\results\principal\lizard_principal.txt"
Write-Host 'Evaluación completa: results/principal/'
