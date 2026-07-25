#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT/backend"

if [[ ! -d "$ROOT/backend/contents" ]]; then
  echo "Missing corpus at $ROOT/backend/contents" >&2
  exit 1
fi

if [[ ! -f "$ROOT/backend/.env" && -f "$ROOT/backend/.env.example" ]]; then
  echo "Copy backend/.env.example to backend/.env and set CLAUDE_API_KEY or LLM_API_KEY" >&2
  exit 1
fi

PYTHON=""
if [[ -x "$ROOT/backend/.venv/bin/python" ]]; then
  PYTHON="$ROOT/backend/.venv/bin/python"
elif [[ -x "$HOME/ReshapeX-Hackathon---Codex/.venv/bin/python" ]]; then
  PYTHON="$HOME/ReshapeX-Hackathon---Codex/.venv/bin/python"
  "$PYTHON" -m pip install -e "$ROOT/backend" -q
else
  echo "Create backend/.venv or use the ReshapeX-Hackathon---Codex virtualenv." >&2
  exit 1
fi

export KNOWLEDGE_CORPUS_DIR="contents"
exec "$PYTHON" -m uvicorn agentsprint_starter.service.http:app --host 0.0.0.0 --port 8001
