#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT/back"

if [[ ! -d "$ROOT/contents" ]]; then
  echo "Missing corpus at $ROOT/contents" >&2
  exit 1
fi

if [[ ! -f "$ROOT/back/.env" && -f "$ROOT/back/.env.example" ]]; then
  echo "Copy back/.env.example to back/.env and set CLAUDE_API_KEY or LLM_API_KEY" >&2
  exit 1
fi

PYTHON=""
if [[ -x "$ROOT/back/.venv/bin/python" ]]; then
  PYTHON="$ROOT/back/.venv/bin/python"
elif [[ -x "$HOME/ReshapeX-Hackathon---Codex/.venv/bin/python" ]]; then
  PYTHON="$HOME/ReshapeX-Hackathon---Codex/.venv/bin/python"
  "$PYTHON" -m pip install -e "$ROOT/back" -q
else
  echo "Create back/.venv or use the ReshapeX-Hackathon---Codex virtualenv." >&2
  exit 1
fi

export KNOWLEDGE_CORPUS_DIR="contents"
exec "$PYTHON" -m uvicorn agentsprint_starter.service.http:app --host 0.0.0.0 --port 8001
