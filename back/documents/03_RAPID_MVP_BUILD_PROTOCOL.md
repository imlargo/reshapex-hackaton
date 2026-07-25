# Rapid MVP Build Protocol

> Revision status: the vertical-slice, verification, and scope-cut practices
> remain useful. The authoritative event-day intake, innovation selection,
> option packs, human-team parallelization, timeline, and architecture ladders
> are in [05_REVISED_MASTER_PLAN.md](./05_REVISED_MASTER_PLAN.md).

## Purpose

This protocol is the case-day workflow that the planned `$rapid-mvp` skill should enforce. It is stage-based, not a minute-by-minute schedule.

The central rule is:

> Prove one valuable agentic decision path end to end before expanding the system.

“Agentic” does not mean maximizing agent count. It means the system uses model judgment, tools, state, and controlled routing where those mechanisms improve the revealed case.

## Stage 1: Normalize the case

Before editing application code, create or replace `docs/context/CASE.md`.

Answer only:

1. Who is the primary user?
2. What decision or action is currently expensive, slow, or error-prone?
3. What input will the demo receive?
4. What concrete output or action creates value?
5. Which external data or tools are truly required?
6. What single journey will be shown to the jury?
7. What must visibly happen for the demo to count as successful?
8. What is explicitly excluded?

The agent may ask at most the questions whose answers would change the journey, data access, external side effects, or architecture. For other gaps, choose the smallest reversible assumption and record it.

## Stage 2: Apply architecture gates

Start with one LangGraph agent/tool loop. Add a technique only when its gate passes.

| Technique | Add it only when | Fast default |
| --- | --- | --- |
| Deterministic workflow nodes | The process has ordered business stages, validation, or a required approval boundary | Explicit `StateGraph` nodes |
| Runtime subagents | At least two roles have distinct tools/context and their work benefits from separation or parallelism | Single agent with a small tool set |
| Router | Inputs fall into distinct domains that require different tools or prompts | Direct tool selection |
| RAG | The answer depends on a corpus too large or dynamic to place in the request | Pass the small source directly |
| Thread memory | The demo requires multi-turn continuity or pause/resume | In-memory checkpointer |
| Long-term memory | Information must survive across different threads or users | No store |
| Knowledge graph | Relationship traversal is central to the domain result and ordinary retrieval loses that structure | Documents or simple records |
| Human-in-the-loop | A side effect is consequential, irreversible, or must be approved | No interrupt for read-only analysis |
| External tool | The agent must retrieve live/private data or perform the value-producing action | Local deterministic function |
| Structured output | The UI or downstream tool must reliably consume fields | Plain final text |

### Runtime multi-agent selection

Choose runtime subagents only if the case can name the roles in domain language and each role has a distinct input/output contract. Examples include a maintenance triage specialist and an inventory availability specialist whose independent results are synthesized.

Do not create “planner,” “researcher,” and “writer” agents only to satisfy the phrase multi-agent. That pattern adds calls and latency without demonstrating domain architecture.

### Memory selection

- Use graph state for values needed during one run.
- Use a checkpointer for thread-scoped continuity.
- Use a store for cross-thread facts or preferences.
- Do not add both a checkpointer and store without a separate requirement for each.
- In-memory persistence is acceptable for the demo unless restart durability itself is part of the case.

## Stage 3: Freeze one vertical-slice contract

Write `docs/context/ACTIVE_SLICE.md` with:

- one-sentence objective;
- request shape;
- stream-event shape;
- final-result shape;
- tools or external calls;
- backend files in scope;
- frontend files in scope;
- acceptance criteria;
- explicit non-goals.

Before any parallel frontend/backend work, record the request and event schemas in `ARCHITECTURE.md`. Once frozen, only the main agent may change them during the slice.

The first slice should cross every intended boundary, even if the domain logic is simple:

```text
real user input
  -> real API route
  -> real graph execution
  -> real selected model
  -> at least one real or deterministic case tool
  -> real final artifact
  -> visible UI result
```

Do not build all backend nodes before connecting the UI. Do not polish the UI against fake final data after a real model path is available.

## Stage 4: Implement with a single default writer

The main Codex agent owns integration and shared contracts.

Default order:

1. update case-specific state and schemas;
2. implement the minimum case tool;
3. implement or adapt the graph route;
4. expose the streaming API;
5. adapt the existing UI shell;
6. run the integrated path;
7. stop and demonstrate before considering another feature.

Use a scout subagent only when a bounded unknown blocks the next implementation action. The main agent should continue independent local work while the scout researches.

### Parallel frontend/backend option

Use only after the contract is frozen.

Backend worker output:

- only files under `backend/`;
- implemented endpoint and normalized events;
- one import or smoke command result;
- no root dependency changes without returning a request to the parent.

Frontend worker output:

- only files under `frontend/`;
- UI against the frozen schema;
- production build result;
- no backend or shared instruction edits.

The parent integrates once. Do not create iterative cross-agent negotiation.

## Stage 5: Minimum verification budget

Verification is risk-weighted and boundary-focused.

### Required automated evidence

Backend:

```powershell
uv run python -m compileall backend
```

or a narrower import when it provides better evidence:

```powershell
uv run python -c "from backend.app.main import app"
```

Frontend after the integrated UI slice:

```powershell
npm --prefix frontend run build
```

Graph or API:

```powershell
uv run python scripts/smoke_graph.py
```

Run only the checks relevant to the files changed. Do not repeatedly execute the full set after every small edit.

### Required manual evidence

Perform:

1. one clean happy-path browser journey;
2. one obvious invalid or missing-input journey;
3. the exact judge-facing journey again after the last critical repair.

Record failures as short reproduction entries in `ACTIVE_SLICE.md`. Do not produce a general QA report.

### When to add a regression check

Add a narrow automated test only when:

- the failed logic is deterministic and important;
- the same failure has appeared twice;
- a state transition could silently corrupt the final result; or
- manual repetition is slower than writing the check.

Do not add snapshots, broad mocks, exhaustive edge-case tables, coverage targets, or a test framework expansion during the initial slice.

## Stage 6: Manual-failure repair loop

Send one failure at a time. A repair prompt should contain:

```text
Fix this reproduced failure in the active MVP slice.

Expected:
[observable behavior]

Actual:
[observable behavior or exact error]

Reproduction:
[short ordered steps]

Evidence:
[relevant log excerpt, request/response, screenshot path, or file reference]

Scope:
Change only the files needed for this failure. Preserve the working happy path.
Do not add generalized fallbacks, refactor unrelated code, or expand features.

Done when:
The exact reproduction passes and the prior happy-path smoke still passes.
```

The agent should:

1. reproduce or inspect the supplied evidence;
2. identify the smallest credible cause;
3. edit the narrow path;
4. rerun the exact reproduction;
5. run the prior happy-path smoke only if the fix touches shared behavior; and
6. report evidence and any unresolved blocker.

Do not ask the agent to “improve the whole app” after a manual failure.

## Scope-cut policy

Cut a feature when any of these is true:

- it does not appear in the jury demo journey;
- it does not reduce a material technical risk;
- it requires a new infrastructure category;
- a simpler visible approximation proves the same decision;
- it depends on unavailable credentials or data;
- it cannot be integrated and manually demonstrated quickly;
- it exists mainly to make the architecture look enterprise-grade.

### Default exclusions

- account management;
- roles and permissions;
- background task infrastructure;
- generalized retries and provider failover;
- elaborate exception hierarchies;
- multiple deployment targets;
- database migrations;
- production observability;
- full design systems;
- generic workflow builders;
- a second user journey before the first is stable;
- RAG without a real corpus;
- memory without a cross-turn requirement;
- subagents without distinct domain responsibilities.

### Acceptable demo shortcuts

- in-memory thread state;
- a fixed local dataset when the case supplies one;
- one explicit provider;
- one narrow output schema;
- a deterministic local tool standing in for a clearly unavailable industrial integration, if labeled honestly;
- manual startup commands;
- one machine and one browser.

Shortcuts must be visible and defendable. Do not misrepresent a deterministic stub as a live external integration.

## Prompt format for the initial build

Use a compact outcome-focused prompt:

```text
$rapid-mvp

Build the smallest working vertical slice for the case in
docs/context/CASE.md.

Primary journey:
[one sentence]

Available data and credentials:
[facts only]

Hard constraints:
- FastAPI backend, React/Vite frontend, LangGraph/LangChain core.
- Main coding model: GPT-5.6 Sol, Extra High.
- One working path before secondary features.
- No production infrastructure or speculative fallbacks.

Done when:
[observable judge-facing result]

You may inspect and edit repository files and run non-destructive local
commands without asking. Ask only if an ambiguity changes the journey,
external side effects, required data, or architecture.
```

Do not prescribe every coding step. GPT-5.6 performs better with a clear result, boundaries, evidence, and completion condition than with repeated process scaffolding.

## Prompt format for a new feature after the first slice

```text
Add only this case-required capability to the working MVP:
[capability]

User-visible value:
[why it matters in the demo]

Existing contract to preserve:
[API/event/result references]

Files or layers likely in scope:
[breadcrumbs]

Done when:
[one observable acceptance criterion]

Do not change the architecture or add adjacent features unless this capability
cannot work without that change. Run only the relevant boundary check and the
existing happy-path smoke.
```

## Definition of done

The MVP is functionally ready when:

- the primary journey uses real user input;
- the graph and intended tool path visibly execute;
- the selected provider is real and explicitly configured;
- the result reaches the frontend in the agreed schema;
- external/configuration failures are visible;
- the production frontend build succeeds;
- the happy-path smoke succeeds;
- a human has completed the final judge-facing browser journey;
- no known critical defect remains in that journey;
- the context ledger matches the implemented architecture; and
- all secondary work has either been cut or explicitly deferred.

The agent must not declare completion based only on generated code, successful imports, isolated tool calls, or a frontend displaying mock data.

## Jury defense notes to capture

For every agentic technique actually used, record:

- the problem it solves;
- the simpler option considered;
- why the chosen option improves the demo;
- its latency/token/reliability tradeoff;
- what would change for production.

For every technique not used, be prepared to say that it failed the decision gate for this case. Deliberately avoiding unnecessary RAG, memory, or subagents is an architectural decision, not a missing feature.
