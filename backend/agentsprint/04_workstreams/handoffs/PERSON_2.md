# Handoff — Usuario 2: Semantic Processing

## Owner decision

- Challenge discovered:
  - Usuario 1 force-pushed `codex/semantic-processing` (tip `b15ad81`); prior U2
    commits were removed from remote history.
  - Processing must emit `agentsprint_starter.rag` contracts (`NormalizedKnowledgePackage`)
    with strict limits (≤12 evidence IDs per relationship).
- Alternatives researched:
  1. Standalone schemas (pre-force-push) — rejected after U1 contract freeze.
  2. Adapter layer between processing and rag — rejected (extra boundary).
  3. Direct import of U1 contracts + `inventory_from_paths` — **selected**.
- Evidence or experiment:
  - `pytest tests/processing/ tests/rag/ demo/semantic/tests/` — 27 passed.
  - End-to-end: `build_inventory_from_directory` → `process_inventory` →
    `AdaptiveRagCompiler.compile` → `search_evidence` + LangGraph runner.
- Selected approach and why:
  - Hybrid pdftotext/HTML extraction + regex entities + rule relations, packaged
    for direct consumption by Usuario 1 adaptive RAG compiler.
- Known trade-offs:
  - KB HTML noise; relationship evidence capped at 12 IDs; large full-corpus PKG.
- Rollback/revisit condition:
  - Use `representative_only=True` in build for demo; add LLM triple verification if needed.

## Delivery

- Branch: `codex/semantic-processing`
- Coordination-baseline SHA: `b15ad81` (Usuario 1) + service layer commits
- Owned outcome completed: U2 processing + backend service boundary for external UI
- Files changed:
  - `src/agentsprint_starter/processing/**`
  - `src/agentsprint_starter/quality/**`
  - `src/agentsprint_starter/service/**`
  - `tests/processing/`, `tests/quality/`, `tests/service/`
  - `agentsprint/05_knowledge/{cleaned,structured,EVIDENCE_MAP.md}`
- Small test/build result:
  - `pytest tests/ -q` — full backend suite
  - `python -m agentsprint_starter.processing.build` — PKG generated
  - `agentsprint-api` or `uvicorn agentsprint_starter.service.http:app` — REST for UI repo
- Evidence artifact: `agentsprint/05_knowledge/structured/PKG-*.json`

## Integration for UI repo (Usuario 3)

### Option A — Python import

```python
from pathlib import Path
from agentsprint_starter.service import KnowledgeBaseService

service = KnowledgeBaseService()
session = service.build_from_corpus(Path("contents"), representative_only=True)
payload = service.export_ui_payload(session)
answer = service.query(session, "Which order number matches WTB4S-3N2131?", deterministic=True)
session.close()
```

### Option B — REST API (recommended for separate frontend repo)

Start server from repo root (requires `contents/` corpus):

```bash
uv sync
agentsprint-api
# or: uvicorn agentsprint_starter.service.http:app --host 0.0.0.0 --port 8000
```

| Method | Route | Purpose |
|--------|-------|---------|
| GET | `/api/health` | `provider_configured`, `knowledge_base_ready`, `index_id` |
| POST | `/api/knowledge/build` | Body: `{ "corpus_dir": "contents", "representative_only": true }` |
| GET | `/api/knowledge/state` | Full `export_ui_payload` after build |
| POST | `/api/knowledge/query` | Body: `{ "question": "...", "deterministic": false }` |

Query response shape: `index_id`, `question`, `answer` (citations, confidence, evidence_grade, trace), `validation_status`.

Errors on query return HTTP 422 with `ErrorEnvelope`: `{ code, message, retryable, details }`.

CORS is open (`*`) for local Vite/React development.

### Pipeline stages covered by this backend

1. `SourceInventory` — U1 contract via `build_inventory_from_directory`
2. `NormalizedKnowledgePackage` — U2 `process_inventory`
3. `RagStrategyPlan` + `QueryableIndex` — U1 `AdaptiveRagCompiler.compile`
4. `ValidationReport` — `validate_knowledge_base`
5. Grounded query — `KnowledgeBaseService.query` (LangGraph runner + citations)

UI repo owns intake forms, validation UX, and cited answer presentation only.

- Known limitations: requires system `pdftotext`; DeepSeek key in `.env` for non-deterministic queries
