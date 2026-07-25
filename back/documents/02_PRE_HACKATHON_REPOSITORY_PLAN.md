# Pre-Hackathon Repository Preparation Plan

> Revision status: partially superseded. LangChain and LangGraph are now
> mandatory core dependencies, but React/FastAPI remains gated by a fully green
> shell. Apply the product, grounding, UI, and advanced-graph gates in
> [05_REVISED_MASTER_PLAN.md](./05_REVISED_MASTER_PLAN.md).

## Goal

Arrive with a neutral, fully runnable agent-application shell. The shell must remove setup work without pre-deciding the unknown industrial case. It should make the first case-specific change a product decision, not environment repair.

The prepared repository should already prove this infrastructure path:

```text
React input
  -> FastAPI streaming endpoint
  -> LangGraph agent loop
  -> injected fake model for smoke verification
  -> streamed node/tool/result events
  -> React timeline and result panel
```

The real provider is selected only through environment configuration. The smoke model must never be a silent runtime fallback.

## 1. Recommended platform baseline

### Development environment

- Primary OS: Windows with the native Codex sandbox configured correctly.
- Python: CPython 3.12, pinned with `.python-version`.
- Python project manager: uv.
- Node.js: 22.12 or newer to satisfy current Vite requirements.
- Frontend package manager: npm, unless the team already standardizes on another installed tool.
- Primary agent surface: Codex Desktop.
- Secondary surface: VS Code with the Codex extension.

Python 3.12 is a conservative compatibility choice while still providing modern async behavior. LangGraph streaming documentation specifically recommends Python 3.11+ for simpler async streaming.

### Locking policy

- Commit `pyproject.toml`, `.python-version`, and `uv.lock`.
- Commit `frontend/package.json` and its lockfile.
- Run preflight commands with locked dependency resolution.
- Do not upgrade packages during the event unless a case-required API is missing or broken.

## 2. Target repository structure

```text
AGENTS.md
.codex/
  config.toml
  agents/
    scout.toml
    verifier.toml
.agents/
  skills/
    rapid-mvp/
      SKILL.md
      agents/openai.yaml
      references/
        architecture-gates.md
        completion-checklist.md
.env.example
.gitignore
.python-version
pyproject.toml
uv.lock
README.md

backend/
  __init__.py
  app/
    __init__.py
    main.py
    api.py
    settings.py
    model_factory.py
    graph.py
    state.py
    tools.py
    stream.py
    schemas.py

frontend/
  package.json
  package-lock.json
  tsconfig.json
  vite.config.ts
  src/
    App.tsx
    main.tsx
    styles.css
    api.ts
    types.ts
    components/
      InputPanel.tsx
      RunTimeline.tsx
      ResultPanel.tsx
      ErrorBanner.tsx

scripts/
  preflight.ps1
  smoke_graph.py
  smoke_api.py
  refresh_repo_map.py

docs/
  context/
    CASE.md
    ARCHITECTURE.md
    ACTIVE_SLICE.md
    DECISIONS.md
    REPO_MAP.md
```

Do not add Docker, Kubernetes, a database, CI workflows, authentication, background queues, or deployment manifests to the base template. Add one only if the venue or revealed case makes it necessary.

## 3. Python dependency plan

Keep the initial dependency set small:

```toml
[project]
requires-python = ">=3.12,<3.13"
dependencies = [
  "fastapi",
  "uvicorn[standard]",
  "pydantic-settings",
  "langchain",
  "langgraph",
  "langchain-openai",
  "langchain-deepseek",
  "httpx",
]

[dependency-groups]
dev = [
  "ruff",
]
```

Rationale:

- `langgraph` and `langchain` provide the graph and agent abstractions.
- `langchain-deepseek` covers the likely low-cost provider without pretending that every provider behaves identically.
- `langchain-openai` covers OpenAI and OpenAI-compatible endpoints.
- `httpx` supports the bounded API smoke script.
- `ruff` supplies fast syntax/import/static checks without establishing a large lint/type-check regime.

Do not preinstall vector databases, document loaders, OCR stacks, browser automation, database drivers, observability SDKs beyond what LangChain already uses, or multiple model-provider packages. Add the package only after the case needs the capability.

## 4. Runtime model provider boundary

Create one small `model_factory.py` with explicit provider branches. Avoid a generalized provider framework.

Environment contract:

```dotenv
LLM_PROVIDER=deepseek
LLM_MODEL=deepseek-v4-flash
LLM_API_KEY=
LLM_BASE_URL=https://api.deepseek.com
LLM_TEMPERATURE=0
LLM_TIMEOUT_SECONDS=60

LANGSMITH_TRACING=false
LANGSMITH_API_KEY=
LANGSMITH_PROJECT=agentsprint
```

Supported initial paths:

### DeepSeek

- Use `ChatDeepSeek`.
- Use current V4 model names, not the retired `deepseek-chat` or `deepseek-reasoner` aliases.
- Start with `deepseek-v4-flash` for cost and latency.
- Switch to `deepseek-v4-pro` only when a representative case shows a material quality gap.
- Keep thinking/tool behavior explicit because provider capabilities and defaults can differ.

### OpenAI-compatible provider

- Use `ChatOpenAI` with `base_url`, `api_key`, and `model` from the environment.
- Use this path only when the event provider advertises OpenAI-compatible chat/tool semantics.
- Verify one tool call and one structured result before assuming full compatibility.

### Provider behavior

- Validate configuration at startup.
- If a key or model is missing, return an actionable configuration error.
- Never silently switch providers or models.
- Never switch to the smoke fake model in the running application.
- Keep provider-specific arguments inside the relevant branch.

The provider interface should expose only what the graph needs: a LangChain chat model capable of message invocation, streaming if available, and tool binding when the case requires it.

## 5. Minimal LangGraph shell

Prepare a graph builder that accepts an injected model and tool list.

Recommended initial state:

```text
messages
run_id
artifacts
errors
```

Do not create a large universal state object. Add case-specific keys only when a node must share the value.

Recommended graph behavior:

1. accept the user request;
2. call the model with the currently enabled tools;
3. execute a requested tool;
4. return to the model when needed;
5. emit a normalized final result; and
6. stream node, tool, status, error, and result events.

Use an in-memory checkpointer only if the generic UI exposes a thread identifier and multi-turn continuity. Losing state on restart is acceptable for the base demo. Do not add a database-backed store until the case requires persistence beyond the process.

The graph builder must support dependency injection so `scripts/smoke_graph.py` can use a deterministic fake chat model. This verifies graph wiring without external credits and without introducing a production fallback.

## 6. FastAPI contract

Prepare only two required routes:

### `GET /api/health`

Return:

```json
{
  "status": "ok",
  "provider_configured": true,
  "graph_ready": true
}
```

The endpoint should not call the external model.

### `POST /api/run`

Request:

```json
{
  "message": "string",
  "thread_id": "optional-string",
  "context": {}
}
```

Return a streaming response using a single normalized event schema:

```json
{
  "type": "status | node | tool | token | result | error",
  "run_id": "string",
  "source": "string",
  "data": {}
}
```

Use LangGraph's unified streaming format internally and translate it once at the API boundary. Do not let provider-specific chunks leak into the frontend.

For development, run Vite and FastAPI separately with an explicit local CORS origin. For the final demo, build the frontend and let FastAPI serve the static build so the team starts one process.

Do not add CRUD routes, authentication, server-side sessions, upload endpoints, or job queues until the case requires them.

## 7. Generic React demo shell

Use React + TypeScript + Vite. Prepare a neutral industrial dashboard rather than a domain-specific product.

The shell needs only four components:

1. `InputPanel`: primary text input and Run action.
2. `RunTimeline`: visible nodes, tools, and statuses.
3. `ResultPanel`: the final judge-facing artifact.
4. `ErrorBanner`: explicit external/configuration failure.

UI requirements:

- one obvious primary action;
- readable status while the model runs;
- visible distinction between model reasoning stages, tool use, and final output without exposing private chain-of-thought;
- a result view that can render plain text and simple structured fields;
- a reset/new-run action handled in frontend state;
- responsive layout for a laptop projector;
- no login, settings area, design system, routing framework, or generic form builder.

Prepare a small set of reusable CSS tokens and components before the event. Avoid spending hackathon time choosing colors, spacing, icons, or panel layouts.

## 8. Context and instruction files

Implement the instruction architecture from [01_CODEX_INSTRUCTION_ARCHITECTURE.md](./01_CODEX_INSTRUCTION_ARCHITECTURE.md).

Seed the ledger with templates rather than fake case content:

- `CASE.md`: empty fields and one example comment.
- `ARCHITECTURE.md`: base entry points, API schema, graph shell, and provider boundary.
- `ACTIVE_SLICE.md`: empty active objective and acceptance criteria.
- `DECISIONS.md`: only the starter decisions.
- `REPO_MAP.md`: generated from the actual prepared repository.

The ledger must describe the code that exists. Never prepopulate speculative RAG, subagent, memory, or tool architecture.

## 9. Deterministic scripts

### `preflight.ps1`

Check only:

- `uv` is available;
- the pinned Python version resolves;
- `uv lock --check` passes;
- Node satisfies Vite's minimum;
- the frontend lockfile installs;
- required ports are available or clearly reported;
- `.env` exists without printing secrets;
- the Codex CLI configuration parses;
- the repository is trusted.

The script should fail on the first actionable blocker and print the exact next command.

### `smoke_graph.py`

Inject a fake model and assert:

- the graph compiles;
- one fake request reaches the final node;
- one tool event can be emitted; and
- the final event matches the normalized schema.

This is not a broad unit-test suite.

### `smoke_api.py`

Start from an already running backend and assert:

- health returns success;
- one fake-provider run streams a final result in development smoke mode; and
- malformed input returns one clear client error.

Keep smoke-mode injection explicit through the script or app factory. It must not be selectable through an undocumented runtime fallback.

### `refresh_repo_map.py`

Generate a concise structural map from paths and known entry points. Exclude:

- `.git`;
- virtual environments;
- `node_modules`;
- frontend build output;
- caches;
- lockfile contents;
- secrets.

## 10. Minimal commands to standardize

Document exact commands in the final root `README.md` and `AGENTS.md`:

```powershell
uv sync --locked
uv run uvicorn backend.app.main:app --reload
npm --prefix frontend ci
npm --prefix frontend run dev
npm --prefix frontend run build
uv run python scripts/smoke_graph.py
uv run python scripts/smoke_api.py
uv run ruff check backend scripts
```

For the event, prefer already completed installs. `uv run --locked` and the committed lockfiles should prevent surprise upgrades.

## 11. Pre-hackathon completion checklist

The repository is ready only when all of the following are true:

- The folder is an initialized Git repository with a known-good baseline commit.
- A clean checkout can restore both locked environments.
- Python 3.12 is installed automatically or through one documented uv command.
- The backend starts without a real model key and reports that the provider is unconfigured rather than crashing ambiguously.
- The deterministic graph smoke succeeds without network access.
- The API smoke succeeds in explicit smoke mode.
- The React production build succeeds.
- FastAPI serves the production frontend build.
- A real DeepSeek V4 call has been verified if a key is available.
- One tool call has been verified against the intended provider.
- The `AGENTS.md`, skill, custom agents, and project configuration are discovered by both Codex Desktop and the IDE extension.
- The global Codex `service_tier` parse error is resolved.
- No secret is committed.
- `REPO_MAP.md` matches the prepared tree and commands.
- The repository is tagged or committed as a known-good starter state.

## 12. Explicitly deferred work

Do not prepare these before the case is known:

- domain prompts;
- domain data models;
- domain tools or integrations;
- RAG ingestion;
- vector or graph databases;
- runtime multi-agent roles;
- long-term memory;
- authentication;
- production hosting;
- comprehensive tests;
- generalized observability dashboards;
- an admin console;
- prompt evaluation datasets.

Preparing unknown-domain features creates more code for Codex and the human team to understand and remove. The base repository should be stable infrastructure plus one replaceable example path.
