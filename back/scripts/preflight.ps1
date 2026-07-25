$ErrorActionPreference = "Stop"

function Fail([string]$Message, [string]$NextCommand) {
    Write-Error "$Message`nNext: $NextCommand"
    exit 1
}

if (-not (Get-Command uv -ErrorAction SilentlyContinue)) {
    Fail "uv is not available." "Install uv, then reopen the terminal."
}

$pythonVersion = uv run --locked python -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')"
if ($LASTEXITCODE -ne 0 -or $pythonVersion.Trim() -ne "3.12") {
    Fail "The locked environment did not resolve Python 3.12." "uv python install 3.12; uv sync --locked"
}

uv lock --check
if ($LASTEXITCODE -ne 0) {
    Fail "uv.lock is stale." "uv lock"
}

uv run ruff check .
if ($LASTEXITCODE -ne 0) {
    Fail "Ruff found a blocker." "uv run ruff check . --fix"
}

uv run pytest
if ($LASTEXITCODE -ne 0) {
    Fail "Tests failed." "uv run pytest -x -vv"
}

uv run python scripts/smoke.py
if ($LASTEXITCODE -ne 0) {
    Fail "The deterministic smoke failed." "uv run python scripts/smoke.py"
}

uv run python scripts/validate_control_room.py
if ($LASTEXITCODE -ne 0) {
    Fail "The AgentSprint control room or skill is incomplete." "uv run python scripts/validate_control_room.py"
}

uv run python scripts/check_secrets.py
if ($LASTEXITCODE -ne 0) {
    Fail "The tracked-file secrets check failed." "Review the reported path; never print the secret."
}

Write-Output "OK: Python 3.12 lock, lint, tests, smoke, control room, skill, and secrets check are green."
if (-not (Test-Path -LiteralPath ".env")) {
    Write-Output "NOTICE: .env is absent. Copy .env.example to .env before the real-provider preflight."
}
