# AgentSprint Rapid-Build Plan

Status: implemented neutral starter. The repository root now contains the
portable control room, Codex instruction layer, Streamlit application, bounded
LangChain/LangGraph DeepSeek runner, typed evidence tools, deterministic
verification, and a fictional rehearsal described below. A real-provider
preflight still requires a local `LLM_API_KEY`.

## July 24 revision

The official event guide, judging rubric, competition-day intake requirements,
Agentic Architecture Toolbox, and DeepSeek token plan materially changed the
earlier fixed-stack proposal.

The authoritative plan is now
[05_REVISED_MASTER_PLAN.md](./05_REVISED_MASTER_PLAN.md). Where it conflicts
with documents 01–04, document 05 controls. In particular:

- LangChain and LangGraph are mandatory, while the graph remains deliberately
  bounded and small;
- evidence grounding is required for the target demo, while vector RAG remains
  conditional;
- React/FastAPI is used only if the entire shell is green before the event;
- the planned portable `agentsprint/` control room manages intake, decisions, team work,
  score evidence, validation, and the pitch; and
- innovation selection and the main-only-versus-fan-out decision happen before
  coding.

## Recommended operating model

Use Codex Desktop as the primary control surface and the IDE extension as the secondary inspection surface.

- Codex Desktop owns the main implementation task, subagent orchestration, terminal work, and final synthesis.
- The IDE extension is used for focused human edits, reviewing changed lines beside the source, and supplying exact file or selection context.
- The main coding agent uses `gpt-5.6-sol` with `xhigh` reasoning.
- Read-heavy subagents may use `gpt-5.6-terra` with `medium` reasoning. This is an optimization for scans and documentation lookup, not a change to the main builder.
- Use Fast mode only if the available credit budget justifies its higher consumption.
- One coordinator runs configuration through work division and pushes the
  frozen baseline. The implementation may remain entirely with the main agent;
  independent branches are used only when they save time without overlap.

The implementation strategy is a thin vertical slice: one real user journey
must reach a judge-facing result through DeepSeek and at least one
case-relevant knowledge/action tool before secondary features are considered.
The UI path is selected through preflight. LangChain/LangGraph are mandatory;
case-specific gates control graph expansion and optional retrieval/runtime
components.

## Core decisions

1. Use portable `agentsprint/START_HERE.md` and `AGENT_PLAYBOOK.md`; root
   `AGENTS.md` or `$sprint-director` integration is optional and must never
   overwrite organizer instructions.
2. Use `agentsprint/` as the event-day source, decision, work, validation, and demo
   control room.
3. Preserve raw sources and provenance; target visible evidence grounding.
4. Start with a bounded LangGraph using LangChain `ChatDeepSeek`, messages, and
   typed tools.
5. Add advanced LangGraph persistence/interrupts, runtime subagents, vector
   RAG, memory, or a micro-graph only after the corresponding gate.
6. Select one central differentiator before freezing the journey.
7. One coordinator completes intake, decisions, contracts, execution-mode
   selection, and the shared baseline push before implementation.
8. Keep all work with the main agent when separation is unnecessary or costly.
9. Use per-user branches only for genuinely independent tasks with a small
   local test; keep overlapping/shared work with the coordinator.
10. When fan-out is used, let the coordinator merge branches sequentially and
   own the end-to-end test.
11. Retain one automated happy-path smoke, targeted failure cases, and the
   exact manual judge journey.
12. Stop feature work at the planned demo-freeze time.

## Planned instruction and context tree

```text
agentsprint/
  START_HERE.md
  AGENT_PLAYBOOK.md
  REPOSITORY_CONTEXT.md
  REPOSITORY_MAP.md
  CONTROL.md
  00_inbox/
  01_case/
  02_decisions/
  03_contracts/
  04_workstreams/
    TEAM.md
    BRANCH_PLAN.md
    tasks/
    handoffs/
    integration/
  05_knowledge/
  06_validation/
  07_demo/
  99_archive/
  # Key files include:
    CASE.md
    ARCHITECTURE.md
    DECISION_LOG.md
    BOARD.md
    SCORECARD.md
    PITCH.md

# Optional only when compatible with the supplied repository:
.codex/
  agents/
.agents/
  skills/
    sprint-director/
```

This is intentionally not a plugin or a default semantic knowledge system. It
uses Codex's native instruction discovery and skill progressive disclosure
while keeping the always-loaded context small.

## Documents

- [Revised master plan](./05_REVISED_MASTER_PLAN.md) — authoritative
- [Imaginary end-to-end walkthrough](./06_IMAGINARY_CASE_WALKTHROUGH.md)
- [Codex instruction architecture](./01_CODEX_INSTRUCTION_ARCHITECTURE.md)
- [Pre-hackathon repository plan](./02_PRE_HACKATHON_REPOSITORY_PLAN.md)
- [Rapid MVP build protocol](./03_RAPID_MVP_BUILD_PROTOCOL.md)
- [Research and rationale](./04_RESEARCH_AND_RATIONALE.md)

## Implementation order

Implement the plan in this dependency order:

1. inspect and verify the supplied Git history, secrets handling, repository
   instructions, and locked toolchain; initialize Git only for a blank
   workspace;
2. create the portable `agentsprint/` templates, repository adapter, and
   `$sprint-director` instruction layer;
3. rehearse intake, option generation, decision capture, and work assignment
   with a sample case;
4. choose exactly one green UI path through preflight;
5. implement the bounded LangChain/LangGraph DeepSeek runner and typed tools;
6. implement the evidence/result contract and case-neutral knowledge-tool
   seams;
7. verify a real call, tool call, structured result, error path, token trace,
   and deterministic smoke;
8. verify clean startup and instruction discovery; and
9. create a clearly labeled neutral-starter baseline commit.

## Implemented outcome

A clean checkout should be able to:

1. restore the pinned environment for the chosen UI path;
2. ingest the revealed instructions and files without altering raw sources;
3. guide the team through the blocking product and architecture decisions;
4. produce a dependency-aware work board;
5. run a bounded LangChain/LangGraph DeepSeek tool loop;
6. return a structured, evidence-visible result;
7. pass a deterministic smoke without spending external tokens;
8. accept the later-selected brand without restructuring the repository; and
9. preserve score evidence, demo artifacts, and a traceable commit history.
