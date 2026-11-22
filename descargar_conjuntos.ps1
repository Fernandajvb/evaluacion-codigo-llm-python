$datasetDirectory = Join-Path $PSScriptRoot 'datasets'
New-Item -ItemType Directory -Force -Path $datasetDirectory | Out-Null

$sources = @(
    @{
        Name = 'securityeval_v2_1.jsonl'
        Url = 'https://raw.githubusercontent.com/s2e-lab/SecurityEval/v2.1/dataset.jsonl'
        Description = 'SecurityEval v2.1 prompts for Python security tasks'
    },
    @{
        Name = 'mbpp_sanitized.json'
        Url = 'https://raw.githubusercontent.com/google-research/google-research/master/mbpp/sanitized-mbpp.json'
        Description = 'MBPP sanitized Python programming tasks'
    }
)

$manifest = @()
foreach ($source in $sources) {
    $destination = Join-Path $datasetDirectory $source.Name
    Invoke-WebRequest -Uri $source.Url -OutFile $destination
    $manifest += [PSCustomObject]@{
        file = $source.Name
        source_url = $source.Url
        description = $source.Description
        sha256 = (Get-FileHash -Algorithm SHA256 -LiteralPath $destination).Hash
        downloaded_at_utc = (Get-Date).ToUniversalTime().ToString('o')
    }
}

$manifest | ConvertTo-Json | Set-Content -Encoding utf8 (Join-Path $datasetDirectory 'fuentes.json')
Get-ChildItem -LiteralPath $datasetDirectory | Select-Object Name,Length
