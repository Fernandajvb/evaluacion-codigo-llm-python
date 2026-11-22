$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent $MyInvocation.MyCommand.Path
$secret = Read-Host 'Pega la clave de OpenRouter' -AsSecureString
$pointer = [Runtime.InteropServices.Marshal]::SecureStringToBSTR($secret)
try {
    $env:OPENROUTER_API_KEY = [Runtime.InteropServices.Marshal]::PtrToStringBSTR($pointer)
    & "$root\.venv\Scripts\python.exe" "$root\reintentar_truncadas.py" --run
}
finally {
    [Runtime.InteropServices.Marshal]::ZeroFreeBSTR($pointer)
    Remove-Item Env:OPENROUTER_API_KEY -ErrorAction SilentlyContinue
}
