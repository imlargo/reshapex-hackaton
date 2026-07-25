# AgentSprint Neutral Starter

A competition-ready, case-neutral shell for one bounded DeepSeek agent built
with LangChain and LangGraph. It must use typed evidence tools before returning
a structured, citation-visible decision package.

The implementation deliberately chooses one green UI path: Streamlit. It does
not preload a company corpus, silently fake a provider, or commit a secret.

## Restore and verify

Requirements: `uv` and Python 3.12.

```powershell
Copy-Item .env.example .env
uv sync --locked
uv run python scripts/smoke.py
uv run pytest
uv run ruff check .
```

The deterministic smoke injects a LangChain test model and traverses the same
compiled LangGraph as the real model. The running application never falls back
to it.

## Configure DeepSeek

Put the key only in the ignored `.env` file:

```dotenv
LLM_API_KEY=your-key
LLM_MODEL=deepseek-v4-flash
```

The runner explicitly disables thinking mode for the bounded tool loop. Start
the UI with:

```powershell
uv run streamlit run app.py
```

Upload `.txt`, `.md`, `.csv`, or `.json` sources, enter one decision request,
and run it. The result panel exposes citations, evidence grade, uncertainty,
next action, model usage, tool steps, and latency.

## Real-provider preflight

With `LLM_API_KEY` configured:

```powershell
uv run python scripts/real_preflight.py
```

This spends a small number of real tokens and proves a non-thinking model call,
a typed knowledge-tool call, a validated result, and a usage/latency trace.

## Competition-day control room

Start with [agentsprint/START_HERE.md](agentsprint/START_HERE.md). It adapts to
an organizer-provided repository without overwriting its instructions, stack,
history, or source layout. The optional `$sprint-director` skill lives in
`.agents/skills/sprint-director/`.

The fictional rehearsal under `examples/rehearsal/` demonstrates intake,
option selection, contract freeze, main-only execution, score evidence, and
the judge journey without coupling the starter to a real brand.

## Architecture

```text
uploaded sources
  -> deterministic text chunks with stable evidence IDs
  -> LangChain ChatDeepSeek + typed tools/messages
  -> bounded LangGraph StateGraph
       model -> tools -> model -> validate -> repair/end
  -> citation-ID and result-schema validation
  -> evidence grade or honest insufficient-evidence result
  -> judge-facing Streamlit result and trace
```

The case gates in `agentsprint/` determine whether a later build should add
hybrid retrieval, a micro-graph, LangGraph persistence/interrupts, runtime
specialists, or human approval.
