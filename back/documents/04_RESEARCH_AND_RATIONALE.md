# Research and Rationale

> Revision status: retained as supporting research. The official event rubric,
> supplied architecture toolbox, competition-day control room, and revised
> DeepSeek operating policy are synthesized in
> [05_REVISED_MASTER_PLAN.md](./05_REVISED_MASTER_PLAN.md).

Research date: 2026-07-24.

## Executive findings

### 1. Lean instructions are a performance optimization

OpenAI's current GPT-5.6 guidance recommends removing repeated instructions and examples, exposing only relevant tools, and keeping descriptions concise. OpenAI reports directional internal coding-agent results in which leaner system prompts improved evaluation scores while reducing tokens and cost. The same guide emphasizes explicit goals, hard constraints, approval boundaries, and success criteria rather than prescribing every step.

Plan consequence:

- keep `AGENTS.md` short;
- state each rule once;
- move the detailed repeated workflow into one on-demand skill;
- give subagents narrow tools and outputs;
- use completion criteria instead of a large process checklist.

Sources:

- [OpenAI GPT-5.6 model guidance](https://developers.openai.com/api/docs/guides/model-guidance?model=gpt-5.6)
- [Codex prompting guidance](https://learn.chatgpt.com/docs/prompting)

### 2. `AGENTS.md`, skills, custom agents, and config solve different problems

Codex reads `AGENTS.md` before work and layers repository guidance from the root toward the current directory. Repository skills are discovered under `.agents/skills` and use progressive disclosure: the model initially sees only name and description, then loads the full skill when selected. Project-local `.codex/config.toml` sets shared trusted-repository defaults. Custom agent TOML files can define narrow spawned roles and override model, reasoning, and sandbox settings.

Plan consequence:

- always-on rules belong in `AGENTS.md`;
- rapid-MVP procedure belongs in a skill;
- model, sandbox, and concurrency belong in `.codex/config.toml`;
- scout and verifier behavior belong in `.codex/agents`;
- current case knowledge remains in checked-in Markdown.

Sources:

- [Codex custom instructions with AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md)
- [Codex build skills](https://learn.chatgpt.com/docs/build-skills)
- [Codex config basics](https://learn.chatgpt.com/docs/config-file/config-basic)
- [Codex subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents)

### 3. Subagents help context isolation but are not free

Codex documentation describes context pollution and context rot from noisy intermediate outputs and recommends subagents for read-heavy exploration, tests, triage, and summarization. It also warns that subagents consume more tokens and that parallel write-heavy workflows create conflicts and coordination overhead. Current guidance recommends `gpt-5.6-terra` for faster, lower-cost read-heavy subagents.

Plan consequence:

- one main writer by default;
- at most two concurrent subagents;
- read-only scout and verifier roles;
- concise summaries instead of raw logs;
- parallel backend/frontend writing only after contract freeze and directory ownership.

Sources:

- [Codex subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents)
- [Codex configuration reference](https://learn.chatgpt.com/docs/config-file/config-reference)

### 4. Large context is not a substitute for context engineering

Chroma's controlled context-rot research reports increasingly non-uniform performance as input length grows, even for simple retrieval and replication tasks. LangChain's context-engineering guidance similarly treats the selection of instructions, messages, tools, model, output format, and persistent state as the central reliability problem.

Plan consequence:

- do not dump the repository into every task;
- use `REPO_MAP.md` and `ARCHITECTURE.md` as breadcrumbs;
- load task-specific context on demand;
- isolate noisy scans in subagents;
- start a fresh task when the main transcript changes phase or becomes noisy.

Sources:

- [Chroma: Context Rot](https://www.trychroma.com/research/context-rot)
- [LangChain context engineering](https://docs.langchain.com/oss/python/langchain/context-engineering)

### 5. A Codex knowledge graph would be overkill here

The repository will begin small and change quickly. A semantic knowledge graph would need an extractor, schema, index, update trigger, retrieval interface, and stale-data policy. The same problem can be solved with Codex-native instruction discovery, skill progressive disclosure, a deterministic repo map, a one-page case brief, explicit contracts, and short decisions.

This is an inference from the cited context research and Codex instruction model, not a vendor claim.

Plan consequence:

- use the five-file context ledger;
- generate `REPO_MAP.md` deterministically;
- add a semantic retrieval layer only if the repository later becomes large enough that targeted search and the ledger measurably fail.

### 6. Runtime multi-agent is a case decision, not a requirement

LangChain's multi-agent guidance explicitly notes that a single agent with the right tools and prompt can often solve complex work. Multi-agent patterns become valuable for context isolation, distributed ownership, parallel work, or too many specialized tools. They add model calls, tokens, and latency.

Plan consequence:

- runtime default is a single agent/tool loop;
- add subagents, handoffs, or a router only after the revealed case passes a specific gate;
- defend both use and non-use of multi-agent architecture to the jury.

Sources:

- [LangChain multi-agent overview](https://docs.langchain.com/oss/python/langchain/multi-agent/index)
- [LangChain subagents](https://docs.langchain.com/oss/python/langchain/multi-agent/subagents)

### 7. Memory types should follow scope

LangGraph separates checkpointers for thread-scoped graph state from stores for long-term cross-thread data. Subgraph documentation recommends isolated per-invocation state for most independent subagent calls.

Plan consequence:

- graph state for one run;
- optional in-memory checkpointer for a demo thread;
- no store until cross-thread memory is required;
- no database-backed persistence in the neutral starter;
- per-invocation subagent state by default.

Sources:

- [LangGraph persistence](https://docs.langchain.com/oss/python/langgraph/persistence)
- [LangGraph subgraphs](https://docs.langchain.com/oss/python/langgraph/use-subgraphs)
- [LangChain long-term memory](https://docs.langchain.com/oss/python/langchain/long-term-memory)

### 8. A normalized stream contract supports the generic UI

Current LangGraph streaming exposes a unified event shape for values, updates, messages, custom events, checkpoints, tasks, and debug output. A provider-independent API boundary can translate only the event categories needed by the demo UI.

Plan consequence:

- FastAPI owns one normalized stream schema;
- provider-specific tokens and tool chunks do not leak into React;
- the UI can remain stable while the case-specific graph changes.

Source:

- [LangGraph streaming](https://docs.langchain.com/oss/python/langgraph/streaming)

### 9. uv and Vite reduce setup variability

uv supports Python version pinning, cross-platform lockfiles, locked synchronization, and automatic environment management. Vite supplies a minimal React/TypeScript scaffold and currently requires Node 20.19+ or 22.12+.

Plan consequence:

- pin Python 3.12;
- commit `uv.lock`;
- use `uv sync --locked`;
- use Node 22.12+;
- prepare and lock the frontend before the event.

Sources:

- [uv Python versions](https://docs.astral.sh/uv/concepts/python-versions/)
- [uv locking and syncing](https://docs.astral.sh/uv/concepts/projects/sync/)
- [uv project structure](https://docs.astral.sh/uv/concepts/projects/layout/)
- [Vite getting started](https://vite.dev/guide/)

### 10. FastAPI can support both development and a one-process demo

FastAPI documents explicit CORS configuration for a separate development frontend and can serve a built static frontend. This supports Vite hot reload during development and a single FastAPI process for the final demo.

Plan consequence:

- separate Vite and FastAPI processes during development;
- explicit local CORS origin;
- build React once for the final demo;
- serve the build through FastAPI;
- avoid adding a separate production web server.

Sources:

- [FastAPI CORS](https://fastapi.tiangolo.com/tutorial/cors/)
- [FastAPI frontend hosting](https://fastapi.tiangolo.com/tutorial/frontend/)

### 11. DeepSeek should be integrated through current V4 names

As of the research date, DeepSeek's official documentation lists `deepseek-v4-flash` and `deepseek-v4-pro` and states that the legacy `deepseek-chat` and `deepseek-reasoner` names are being retired on 2026-07-24. The LangChain DeepSeek integration documentation still demonstrates the older names, so provider documentation must be authoritative for active model identifiers.

Plan consequence:

- configure model names through environment variables;
- seed the likely low-cost default as `deepseek-v4-flash`;
- retain `deepseek-v4-pro` as an explicit quality choice;
- verify tool calling and structured output with the exact selected model;
- do not hardcode the legacy aliases.

Sources:

- [DeepSeek first API call](https://api-docs.deepseek.com/)
- [DeepSeek models and pricing](https://api-docs.deepseek.com/quick_start/pricing/)
- [DeepSeek tool calls](https://api-docs.deepseek.com/guides/tool_calls/)
- [LangChain ChatDeepSeek integration](https://docs.langchain.com/oss/python/integrations/chat/deepseek)

## Codex surface recommendation

Use Codex Desktop as the primary orchestration surface because the work benefits from a visible long-running task, subagent activity, terminal execution, and consolidated results. Use the IDE extension for exact editor context and in-place diff review.

Sources:

- [ChatGPT desktop app](https://learn.chatgpt.com/docs/app)
- [Codex IDE extension](https://learn.chatgpt.com/docs/codex/ide)

## GPT-5.6 Sol and reasoning recommendation

The main builder remains `gpt-5.6-sol` with `xhigh` reasoning as requested. Higher reasoning effort is slower and uses more tokens, so speed should come from:

- smaller task scope;
- leaner instructions;
- fewer irrelevant tools;
- short context;
- independent read-heavy delegation;
- frozen contracts before parallel work;
- no repeated full-repo reviews.

Do not reduce the main agent to low reasoning merely to make it respond sooner; that risks losing more time to architectural drift and repair. Use lower effort only for straightforward bounded subagent work.

Fast mode is optional. Current Codex documentation states that it increases supported-model speed by about 1.5× and that GPT-5.6 consumes 2.5× standard ChatGPT credits in Fast mode. Enable it only when event-day credit availability is known.

Sources:

- [OpenAI GPT-5.6 model guidance](https://developers.openai.com/api/docs/guides/model-guidance?model=gpt-5.6)
- [Codex speed](https://learn.chatgpt.com/docs/agent-configuration/speed)
- [Codex subagent model and reasoning guidance](https://learn.chatgpt.com/docs/agent-configuration/subagents)

## Research limitation and local environment finding

The official OpenAI documentation MCP could not be added in the current environment because the local Codex CLI rejected the existing global `service_tier = "default"` configuration before loading commands. Research therefore used:

- the freshly fetched official Codex manual;
- live official OpenAI and ChatGPT Learn pages;
- official LangChain/LangGraph documentation;
- official uv, FastAPI, Vite, and DeepSeek documentation; and
- the original Chroma context-rot technical report.

The current project folder is also not yet recognized as a Git repository. Both Git initialization and the global Codex configuration parse issue are included as required pre-hackathon fixes in the plan.
