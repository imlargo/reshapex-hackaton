# Codex Instruction Architecture

> Revision status: retained as background for lean Codex configuration and
> context hygiene. The competition-day workspace, skill, agent roles, grounding
> requirement, and architecture defaults are superseded by
> [05_REVISED_MASTER_PLAN.md](./05_REVISED_MASTER_PLAN.md).

## Objective

Configure Codex to produce the smallest working, judgeable vertical slice quickly while preserving a narrow quality floor. The design must reduce repeated prompting, context growth, unnecessary approvals, broad repository rereads, speculative features, and duplicate verification.

The instruction system should be layered. Each concern belongs in the smallest native Codex surface that matches its scope.

| Surface | Purpose | Loaded when |
| --- | --- | --- |
| Root `AGENTS.md` | Durable mission, scope rules, commands, minimum verification, completion boundary | Every Codex run |
| `.codex/config.toml` | Model, reasoning, sandbox, approval behavior, subagent limits | Trusted project configuration |
| `.codex/agents/*.toml` | Narrow subagent roles and model overrides | Only when spawned |
| `.agents/skills/rapid-mvp/SKILL.md` | Repeatable rapid-build workflow | Only when explicitly invoked |
| `docs/context/*.md` | Current case, architecture contracts, task state, decisions, and repo map | Only when a task needs the file |
| Current task prompt | The revealed case, current objective, and any one-off limits | Current task only |

Do not duplicate a rule across these surfaces. Duplication wastes context and increases the chance of contradictory behavior.

## 1. Root `AGENTS.md`

The root file should stay short enough to scan in one pass. It should link to the context ledger and the rapid-MVP skill instead of embedding the full process.

The following is the planned core contract to implement:

```md
# Mission

Build the smallest end-to-end demo that proves the revealed industrial use
case. Optimize for a working vertical slice, visible agent behavior, and a
clear technical story. This is a four-hour prototype, not a production system.

# Default execution

- For build or fix requests, inspect only the relevant files and implement the
  requested in-scope change without asking for routine local approval.
- Ask a question only when the answer would change the user journey, external
  side effects, required data, or architecture. Otherwise choose the simplest
  reversible option and record the assumption.
- Use targeted search and file reads. Do not reread the full repository when
  `docs/context/REPO_MAP.md` and `docs/context/ARCHITECTURE.md` provide the
  needed breadcrumbs.
- Complete one thin vertical slice before adding a second feature.
- Keep the demo path free of placeholders, silent mocks, and TODO behavior.

# Scope discipline

- Implement only behavior required by `docs/context/CASE.md` and the active
  acceptance criteria.
- Do not add authentication, multi-tenancy, queues, migrations, distributed
  infrastructure, production deployment, generalized plugin systems, elaborate
  fallbacks, or speculative abstractions unless the case directly requires
  them.
- Do not add RAG, runtime subagents, durable memory, or a knowledge graph merely
  because they are agentic techniques. Apply the architecture gates in the
  rapid-mvp skill.
- Prefer one explicit implementation over a generic framework for hypothetical
  future cases.
- Fail clearly at external boundaries. Do not create multiple retry or fallback
  layers for a demo.

# Change discipline

- Preserve working behavior outside the active slice.
- Prefer small cohesive edits. Do not refactor unrelated code.
- The main agent is the default writer.
- Delegate only independent, bounded work. Parallel writers require frozen
  contracts, non-overlapping directories, and an explicit owner for integration.
- Subagents return concise conclusions, file references, and unresolved risks;
  they do not paste raw logs into the main task.

# Minimum verification

- Backend changes: import or compile the changed application path.
- Frontend changes: run the production build after an integrated UI slice, not
  after every small edit.
- Vertical-slice completion: run the happy-path smoke command and one manual
  browser journey.
- After a manual failure, fix that failure and rerun the exact reproduction.
- Do not create a broad unit-test suite before the demo path works. Add a narrow
  regression check only for critical pure logic or a bug that has recurred.

# Completion

Done means the primary journey starts from a clean environment, reaches a real
final result through the intended graph and tools, reports external failures
visibly, and can be demonstrated again. A successful import, isolated tool call,
or mocked UI is not completion.

# Project context

- Current case: `docs/context/CASE.md`
- Current contracts and entry points: `docs/context/ARCHITECTURE.md`
- Current slice and acceptance criteria: `docs/context/ACTIVE_SLICE.md`
- Durable decisions: `docs/context/DECISIONS.md`
- File and symbol map: `docs/context/REPO_MAP.md`

Invoke `$rapid-mvp` for the initial case implementation or a material new slice.
```

### Why this contract is intentionally strict

The instructions do not simply remove testing and review. They replace broad process with a smaller set of completion evidence:

- one real vertical slice instead of several partial layers;
- one import/build check at the relevant boundary;
- one smoke path;
- one manual demo;
- targeted regression checks only after observed failures.

This preserves a defensible minimum without spending the event building production infrastructure.

## 2. Project Codex configuration

Plan a project-local `.codex/config.toml` so Desktop, CLI, and the IDE use the same trusted-repository defaults.

Recommended baseline:

```toml
model = "gpt-5.6-sol"
model_reasoning_effort = "xhigh"
approval_policy = "on-request"
sandbox_mode = "workspace-write"

[agents]
enabled = true
max_concurrent_threads_per_session = 2
default_subagent_model = "gpt-5.6-terra"
default_subagent_reasoning_effort = "medium"
```

Design notes:

- The main thread stays on the requested `gpt-5.6-sol` + Extra High setup.
- Two subagent slots are sufficient: one explorer/researcher and one bounded verifier, or two independent read-heavy scans.
- `workspace-write` avoids repeated approvals for normal repository work while retaining boundaries around external and destructive actions.
- `on-request` is preferable to globally disabling approvals. The time savings should come from clear authorization rules, not from removing safety boundaries.
- Do not pin every subagent to Sol/XHigh. Official Codex guidance positions Terra as the faster option for read-heavy scans. If the account does not expose Terra, inherit the parent model and keep the subagent task smaller.

### Fast mode

Fast mode can increase supported-model speed, but GPT-5.6 consumes credits at a higher multiplier. Treat it as an event-day switch:

```toml
service_tier = "fast"

[features]
fast_mode = true
```

Enable it only after checking the available credit budget. Standard execution plus smaller tasks is the safe default when credits are uncertain.

### Local configuration issue to resolve

The current machine's global Codex configuration failed to parse because `service_tier = "default"` is not accepted by the installed CLI. Before the hackathon:

1. open `C:\Users\jacob\.codex\config.toml`;
2. remove the `service_tier` line for standard behavior, or replace it with a currently supported tier after confirming the desired credit policy;
3. run `codex --version` and one harmless `codex mcp list` command;
4. verify that the repo is marked trusted so project-local `.codex` settings load.

Do not wait until the event to discover this configuration blocker.

## 3. Repository skill: `rapid-mvp`

Use one repository skill at `.agents/skills/rapid-mvp/SKILL.md`. Keep implicit invocation disabled and invoke it explicitly at the start of the revealed case. This avoids adding its full instructions to unrelated repair tasks.

Planned metadata:

```yaml
---
name: rapid-mvp
description: Build or materially extend a four-hour hackathon MVP as the smallest working vertical slice. Use for initial case implementation and major case-required slices; do not use for tiny follow-up fixes.
---
```

Optional `agents/openai.yaml` policy:

```yaml
policy:
  allow_implicit_invocation: false
```

The skill should perform exactly six stages:

1. Normalize the case into `CASE.md`.
2. Apply architecture gates and record the selected pattern.
3. Define one user journey and freeze the API/UI contract.
4. Implement the vertical slice.
5. Run the minimum verification budget and surface gaps.
6. Update the context ledger and stop when the slice is demonstrable.

The skill should reference, rather than inline, two small documents:

- `references/architecture-gates.md`
- `references/completion-checklist.md`

Do not create separate skills for planning, coding, testing, review, frontend, and backend. A large skill catalog consumes discovery context and encourages unnecessary process switching.

## 4. Custom subagents

Create only two project-scoped custom agents initially.

### `scout`

Purpose: bounded code mapping, official documentation lookup, or API capability verification.

Recommended configuration:

```toml
name = "scout"
description = "Read-only scout for targeted repository mapping and current API documentation. Use only when a bounded unknown blocks implementation."
model = "gpt-5.6-terra"
model_reasoning_effort = "medium"
sandbox_mode = "read-only"
developer_instructions = """
Answer the assigned question only.
Prefer targeted search and exact file reads over broad scans.
Use primary documentation for version-sensitive API claims.
Return at most: conclusion, evidence links or file references, and one unresolved risk.
Do not propose unrelated features and do not edit files.
"""
```

### `verifier`

Purpose: execute the explicitly named smoke/build command, inspect the active diff for demo blockers, and report only actionable failures.

Recommended configuration:

```toml
name = "verifier"
description = "Read-only bounded verifier for the active demo slice. Use after integration or after a reproduced failure, not after every edit."
model = "gpt-5.6-terra"
model_reasoning_effort = "medium"
sandbox_mode = "read-only"
developer_instructions = """
Verify only the active acceptance criteria and named commands.
Do not expand into a general review.
Ignore style-only findings.
Return pass/fail evidence, the first blocking failure, and the smallest next action.
Do not edit files.
"""
```

The main agent remains responsible for implementation and synthesis. A Sol reviewer at High or XHigh can be added only if the revealed case contains a genuinely risky algorithm, safety boundary, or complex state transition.

## 5. Subagent concurrency gate

Subagents are not automatically faster. Each agent adds tokens, tool calls, and coordination. Use this gate before delegation:

Delegate when all are true:

1. the task is independent from the main writer's next decision;
2. its input can be expressed in a short bounded prompt;
3. it has a clear output contract;
4. duplicate work is unlikely; and
5. the expected wall-clock saving exceeds the synthesis overhead.

Default parallel tasks:

- current external API documentation lookup;
- targeted repository mapping;
- log or trace analysis;
- smoke command execution;
- independent domain research.

Avoid by default:

- two agents editing the same layer;
- broad “review everything” assignments;
- agents that must repeatedly ask the parent for missing context;
- separate agents for trivial files;
- parallel tasks whose outputs are prerequisites for each other.

### Parallel-writing exception

After the main agent freezes the request/response and stream-event schemas, it may assign:

- one worker to `backend/`;
- one worker to `frontend/`.

Neither worker may edit root configuration, shared schemas, instruction files, or the other worker's directory. The parent agent owns integration and the first end-to-end run. If the contract is still moving, do not parallelize writes.

## 6. Context ledger instead of a knowledge graph

A semantic graph is not the right default for a small, rapidly changing hackathon repository. It would require extraction, indexing, update rules, retrieval tooling, and synchronization precisely while the codebase is changing fastest.

Use five small checked-in files:

### `CASE.md`

Single source of truth for:

- target user;
- painful decision or action;
- input data;
- required output;
- one demo journey;
- must-have behavior;
- explicit non-goals;
- assumptions and open blockers.

Keep it under roughly one page.

### `ARCHITECTURE.md`

Record only stable breadcrumbs:

- current graph pattern;
- state keys;
- node and tool responsibilities;
- API request, stream, and final-result schemas;
- frontend entry points;
- model provider selection;
- important invariants.

Update it only when a contract or owner changes.

### `ACTIVE_SLICE.md`

Keep exactly one active slice:

- objective;
- files in scope;
- acceptance criteria;
- current failure evidence;
- next smallest action.

Replace its contents when moving to the next slice. Do not turn it into a historical log.

### `DECISIONS.md`

Append short architectural decisions:

```md
## D-003 — Use thread memory only

- Decision: InMemorySaver, no cross-thread store.
- Reason: the demo needs conversational continuity but no durable personalization.
- Revisit if: the revealed case explicitly requires cross-session recall.
```

### `REPO_MAP.md`

Generate deterministically from the repository. Include:

- two-level directory tree;
- application entry points;
- API routes;
- graph builder and state definitions;
- tool registry;
- frontend API client and main views;
- run, build, and smoke commands.

Do not embed file contents or prose summaries for every module. Regenerate only after structural changes.

## 7. Task and context hygiene

- Start the main implementation in a fresh Codex task after `CASE.md` is approved.
- Keep raw logs in files or subagent tasks; return only the failure-relevant excerpt to the main task.
- When the task becomes noisy or changes from initial build to repair, update the ledger and start a fresh task rather than carrying the full transcript.
- Give each subagent exact file breadcrumbs and the relevant acceptance criterion. Do not ask it to “understand the repo.”
- Update `ARCHITECTURE.md` before spawning parallel writers so both use the same contract.
- Required project rules remain in checked-in files, not Codex memories.

## 8. Recommended human workflow

Use Codex Desktop for the primary build because it is better suited to coordinating a long task and inspecting subagent activity. Keep VS Code open for the human team to:

- inspect exact code and diffs;
- make very small manual edits;
- attach a selected file or symbol to a focused follow-up;
- watch the running frontend and backend terminals.

Do not run two independent primary Codex writers against the same checkout. If another teammate uses a separate agent, give that teammate a branch or worktree and a non-overlapping deliverable.
