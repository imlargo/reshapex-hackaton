# Revised AgentSprint Master Plan

Status: authoritative plan, implemented as a neutral starter on July 24, 2026.
Case-specific gates remain intentionally open until the event materials and
DeepSeek credentials are supplied.

This revision incorporates:

- the official AgentSprint judging weights and build-time guidance;
- the supplied Agentic Architecture Toolbox;
- the requirement for a competition-day intake and decision workspace;
- explicit human-team and Codex parallelization;
- DeepSeek tokens as the expected model budget; and
- the fact that the brand and case will be selected later.

Where this document conflicts with documents 01–04, this document controls.

For a concrete simulation of the human and coding workflows, see
[06_IMAGINARY_CASE_WALKTHROUGH.md](./06_IMAGINARY_CASE_WALKTHROUGH.md).

## 1. Outcome

Prepare a neutral starter and a competition-day control room that help a team
of three or four:

1. ingest the instructions and files revealed that morning without losing or
   altering the raw sources;
2. identify the few product and architecture decisions that materially affect
   the result;
3. ask the team targeted questions that produce a distinctive, defensible idea;
4. compare three feasible options plus one or more creative alternatives;
5. select the smallest architecture that can earn a strong score;
6. split independent work across people and bounded Codex workers;
7. integrate one grounded, real, judge-facing path;
8. stop new features early enough to validate and rehearse; and
9. preserve evidence for the pitch, repository review, and technical checklist.

The system should optimize expected score, not architecture size:

```text
expected value = judging value × probability of a stable live demo
```

## 2. What changes from the earlier plan

| Earlier assumption | Revised decision | Reason |
| --- | --- | --- |
| LangGraph was gated | LangChain and a bounded LangGraph are mandatory core infrastructure | Competition requirement; keep the graph minimal so the framework does not consume the sprint |
| RAG is entirely optional | Evidence grounding is required for the target demo; vector RAG is only one way to provide it | “All answers grounded by knowledge tools” is the highest progress milestone |
| Architecture and delivery dominate planning | Product novelty, judge evidence, and the pitch are planned from minute one | Innovation and progress are each 30% of the score |
| React/FastAPI is mandatory | Use it only if the complete shell is green before the event; otherwise use Streamlit/Gradio | The event is too short to repair a presentation stack |
| The context ledger mainly serves code generation | The competition workspace also controls intake, decisions, ownership, testing, score evidence, and the demo | The team needs an operational control room, not only code breadcrumbs |
| Codex scout and verifier are the main parallel roles | Add isolated document/data preparation after branch fan-out, while distinguishing human work, development subagents, and runtime agents | Data cleaning and pitch/test work become useful independent branch tasks even when the product uses one runtime agent |
| Innovation is considered after the base slice | Select one differentiator before the contract freezes | Innovation must shape the main journey rather than appear as a decorative late feature |
| One baseline commit is sufficient | Preserve a short, traceable milestone history | Commit history is explicitly reviewed under code quality |

## 3. Rubric-first strategy

The supplied rubric should be translated into visible evidence before coding.

| Dimension | Weight | Target evidence |
| --- | ---: | --- |
| Progress | 30% | Live end-to-end journey; real model; real tool path; every material claim tied to knowledge-tool evidence |
| Innovation | 30% | One sentence explaining why this is not the obvious chatbot; one central differentiator visible in the journey |
| Technical checklist | 20% | Three to five implemented components, each with a trace, UI cue, test, or artifact proving it works |
| Presentation | 10% | Two-minute story, crisp before/after workflow, rehearsed fallback, prepared judge questions |
| Code quality | 10% | Real integrations, clear boundaries, no committed secrets, simple structure, honest stubs, traceable commits |

The team should maintain a live score-evidence table in
`agentsprint/06_validation/SCORECARD.md`. A component does not count merely because
it is named in the architecture.

### Score priority

1. Reach a stable live demo.
2. Make grounding and provenance visible.
3. Make one innovation central to the user journey.
4. Prove the selected technical components.
5. Polish the story and repository.

Do not sacrifice the first two for extra technical components.

## 4. Planned competition-day control room

Create the following only when implementation is authorized:

```text
agentsprint/
  START_HERE.md
  README.md
  CONTROL.md
  AGENT_PLAYBOOK.md
  REPOSITORY_CONTEXT.md
  REPOSITORY_MAP.md
  .gitignore

  00_inbox/
    DAY_INSTRUCTIONS.md
    LINKS.md
    raw/

  01_case/
    CASE.md
    BRAND.md
    SOURCE_MANIFEST.md
    FACTS_AND_CONSTRAINTS.md
    OPEN_QUESTIONS.md

  02_decisions/
    DECISION_QUEUE.md
    OPTION_PACKS.md
    DECISION_LOG.md
    SCORE_STRATEGY.md

  03_contracts/
    PRIMARY_JOURNEY.md
    ARCHITECTURE.md
    INTERFACES.md
    ACCEPTANCE.md

  04_workstreams/
    TEAM.md
    BOARD.md
    BRANCH_PLAN.md
    tasks/
    handoffs/
    integration/
      MERGE_ORDER.md
      INTEGRATION_LOG.md

  05_knowledge/
    cleaned/
    structured/
    index/
    EVIDENCE_MAP.md

  06_validation/
    SCORECARD.md
    TECHNICAL_CHECKLIST.md
    DEMO_CASES.md
    FAILURE_LOG.md

  07_demo/
    PITCH.md
    RUNBOOK.md
    JUDGE_QA.md

  99_archive/
```

### Folder rules

- `00_inbox/raw/` is append-only during intake. Never “clean” a raw source in
  place.
- `START_HERE.md` contains the single boot prompt that works whether the folder
  is copied into an empty workspace or an organizer-provided repository.
- `AGENT_PLAYBOOK.md` contains the workflow instructions without depending on
  Codex-specific root configuration.
- `REPOSITORY_CONTEXT.md` records the supplied repository's stack, commands,
  entry points, current instructions, protected paths, baseline status, and
  integration constraints.
- `REPOSITORY_MAP.md` records relative repository paths and ownership without
  copying source code into the control room.
- `SOURCE_MANIFEST.md` assigns every useful source an ID, type, origin,
  relevance, owner, and processing status.
- Derived text, tables, images, and chunks go under `05_knowledge/`, retaining
  their source IDs.
- `CONTROL.md` is the single current-state page: clock, stage, chosen journey,
  owners, blockers, next integration point, and cut line.
- `DECISION_QUEUE.md` contains only decisions that block the journey or change
  the score. Minor implementation choices stay with the assigned owner.
- `DECISION_LOG.md` records the chosen option, reason, rejected alternatives,
  owner, timestamp, and revisit trigger.
- `BOARD.md` is the only task board. Do not maintain a second checklist in chat.
- `TEAM.md` records the number of participants, coordinator/integrator, user
  identifiers, selected execution mode, optional branch names, and final
  ownership. It is populated when the actual team is known.
- `tasks/USER-N.md` gives every participant a self-contained implementation
  packet with an exact base commit, optional branch, write scope, frozen
  contracts, acceptance criteria, small test, and handoff format when
  multi-user fan-out is selected. These packets are not required in main-only
  mode.
- `BRANCH_PLAN.md` is used only when branch fan-out is selected. It proves that
  no two participants own the same feature or file. If clean separation is
  impossible, prefer main-only execution or keep the overlapping/shared work
  with the coordinator.
- `MERGE_ORDER.md` is required only for branch fan-out and defines the
  dependency-aware sequential merge order before anyone begins implementation.
- `INTEGRATION_LOG.md` records merge results, conflicts, integrated checks, and
  any rejected branch.
- `ARCHITECTURE.md` and `INTERFACES.md` must be frozen before parallel writers
  touch backend and frontend.
- `PITCH.md` begins as soon as the idea is selected, not after coding ends.
- `99_archive/` receives superseded artifacts so current files remain short.

The application source remains wherever the supplied repository already puts
it. `agentsprint/` is the team's portable operational and evidence layer, not
another application project.

### Drop-in repository compatibility

`agentsprint/` must be copyable as one ordinary folder into the root of an
unknown starter repository. It must work without renaming, moving, or
overwriting any existing source or configuration.

The boot sequence is:

```text
copy agentsprint/ into the supplied repository root
  -> ask the main agent to read agentsprint/START_HERE.md
  -> discover and obey the repository's existing instructions
  -> inspect the existing stack and baseline
  -> populate REPOSITORY_CONTEXT.md and REPOSITORY_MAP.md
  -> continue with case intake and decisions
```

Compatibility rules:

- Never overwrite an existing `AGENTS.md`, `CLAUDE.md`, `.codex/`,
  `.agents/`, `.github/`, `.vscode/`, README, dependency manifest, lockfile, or
  source directory.
- Existing repository instructions and user constraints take precedence over
  `AGENT_PLAYBOOK.md`.
- Do not initialize Git when a real repository already exists. Preserve its
  history, branches, remotes, and unrelated working-tree changes.
- Do not replace the supplied framework with the prepared default merely
  because another stack is preferred. Adapt to the existing stack unless it
  cannot support the selected journey.
- Use repository-relative paths in every control-room artifact. Do not store
  machine-specific absolute paths.
- Discover install, run, test, lint, build, and formatting commands from the
  supplied repository before proposing new ones.
- Record current baseline failures before editing; do not attribute a
  pre-existing failure to event-day changes.
- Treat unknown generated, vendor, migration, lock, and secret files as
  protected until their ownership is understood.
- Keep large derived indexes, caches, virtual environments, build output, and
  secrets out of Git. The folder-level `.gitignore` may ignore only artifacts
  inside `agentsprint/`; changes to the repository's root ignore rules require
  an explicit integration decision.
- Preserve source IDs when derived knowledge artifacts move into application
  storage.
- If the supplied repository already has an operational folder named
  `agentsprint/`, stop and choose a non-conflicting folder name with the team;
  do not merge folders automatically.

### Repository adapter contract

`REPOSITORY_CONTEXT.md` should answer:

```text
repository mode: blank | starter | monorepo | existing product
repository root: .
existing agent instructions:
languages and frameworks:
dependency manifests and lockfiles:
install command:
run command:
test/build/lint commands:
application entry points:
API/UI boundaries:
existing model and tool integrations:
data/document locations:
protected or owner-only paths:
current working-tree state:
baseline checks and pre-existing failures:
shared contracts that must freeze:
allowed write zones by owner:
integration owner:
```

For a blank workspace, the architecture gate selects a minimal stack. For a
starter repository, reuse the provided stack and first make its existing path
run. For a monorepo, record the exact package roots and commands before
assigning file ownership.

## 5. Planned instruction architecture

The portable mode must require no root instruction changes:

```text
agentsprint/
  START_HERE.md
  AGENT_PLAYBOOK.md
  ...
```

The human starts a main task with:

```text
Read agentsprint/START_HERE.md and act as the sprint director for this
repository. First adapt the control room to the existing repository and ingest
the supplied case. Do not change application code until the first journey,
architecture, and ownership gates are recorded.
```

`START_HERE.md` must tell the agent to inspect all applicable existing
repository instructions before acting. The folder playbook supplements those
instructions and never overrides them.

### Optional Codex-native integration

If the team owns the starter repository and wants automatic discovery, it may
later add:

```text
.codex/
  agents/
    scout.toml
    curator.toml
    verifier.toml
.agents/
  skills/
    sprint-director/
      SKILL.md
```

This integration is optional. It must be merged into existing configuration
rather than copied over it. A thin root `AGENTS.md` pointer may be added only
if no organizer rule forbids it and the existing file is preserved.

When root integration is used, the root instructions should state only:

- the rubric-weighted mission;
- the location of `agentsprint/CONTROL.md`;
- the rule that raw sources are immutable;
- the single-writer and frozen-contract rules;
- the evidence-grounding requirement;
- the scope-cut and completion boundary; and
- when to invoke `$sprint-director`.

### `$sprint-director` responsibilities

The main competition agent should:

1. inventory `00_inbox/` and create/update the source manifest;
2. normalize the revealed case and facts before proposing architecture;
3. ask the minimum high-value questions;
4. produce option packs for the genuinely consequential decisions;
5. obtain and record the team's choices;
6. freeze the primary journey and interfaces;
7. ask for the actual participant count and decide whether implementation
   should remain with the main agent or fan out into fully separated branches;
8. in branch mode, assign only the genuinely independent task packets and
   branches; do not invent work merely to involve every participant;
9. commit and push the coordination baseline through the work-division gate;
10. execute either the main-only path or the independent-branch path;
11. in branch mode, collect handoffs and integrate them sequentially;
12. keep the scorecard, technical evidence, and demo artifacts current; and
13. stop new feature work at the demo-freeze time.

It should not monopolize all implementation. It directs the critical path and
delegates isolated work with explicit artifacts and deadlines.

### Development agents are not runtime agents

Keep three concepts separate:

1. **Human workstreams:** team members building, cleaning data, validating, and
   pitching.
2. **Codex development workers:** temporary scouts, curators, coders, or
   verifiers that help build the repository.
3. **Runtime product agents:** model-driven specialists inside the demo.

Parallel development does not require a multi-agent product. Add runtime
subagents only if the case has genuinely separable domain roles, tools, or
evidence.

## 6. Intake and questioning flow

### Intake pass

Before asking broad product questions:

1. list every supplied file and link;
2. assign a stable source ID;
3. extract only enough content to identify format, scope, and relevance;
4. flag missing, unreadable, duplicate, or confidential material;
5. separate organizer facts from team assumptions; and
6. create a short case brief.

During initial configuration, the coordinator inventories and samples only
enough source content to make the product and architecture decisions. Full
cleaning, extraction, and indexing wait until work division and become one
participant's independent branch task.

### First question round: five decisions

Ask the team these questions in one compact round:

1. Who experiences the painful decision or action, and what does it cost them
   today?
2. What exact input can the live demo reliably receive?
3. What grounded recommendation or action will prove value in under two
   minutes?
4. What would the obvious competing “chat with the documents” solution do, and
   how will ours be meaningfully different?
5. Which documents, APIs, structured data, credentials, and team skills are
   actually available now?

### Conditional follow-up round

Ask at most three follow-ups selected from:

- What error would be dangerous or embarrassing, and should the system decline,
  retry, or ask for approval?
- Does the answer depend on exact IDs/tables, semantic prose, relations, images,
  or live state?
- Which single differentiator can be implemented and demonstrated by the
  feature-freeze time?
- Which team member owns integration, knowledge/data, UI, and
  verification/pitch?
- What is the explicit kill condition for the riskiest feature?

Do not run an unbounded interview. When an answer does not change the journey,
architecture, evidence, or ownership, choose a reversible default and record it.

## 7. Option-pack protocol

For every consequential segment, the agent should provide:

```text
Decision and failure/capability it addresses
Constraints and evidence available

Option A — lowest-risk baseline
Pros / cons / estimated effort

Option B — best expected score (recommended)
Pros / cons / estimated effort

Option C — higher-upside architecture
Pros / cons / estimated effort

Creative alternative(s)
Why each is genuinely different

Weighted comparison
Recommendation
Decision deadline and kill condition
```

Score options on:

- user value;
- innovation;
- grounding and trust;
- live-demo clarity;
- data readiness;
- integration time; and
- failure risk.

The recommendation should normally maximize expected score, not raw novelty.

## 8. Architecture decision ladders

### 8.1 Overall orchestration

Present these three defaults:

1. **Deterministic LangGraph workflow**
   - Pros: fastest, predictable, easy to test.
   - Cons: limited adaptation.
   - Use when the steps are already known; encode them as explicit graph nodes.
2. **One bounded LangGraph agent with three to six LangChain tools — recommended default**
   - Pros: visibly agentic, flexible, understandable.
   - Cons: needs step limits and good tool contracts.
   - Use when the model must choose which evidence or action is needed.
3. **Expanded LangGraph workflow with selected agent decisions**
   - Pros: strong control and a good technical story.
   - Cons: more state and integration.
   - Use when the real process has checkpoints, routing, or approval.

Creative alternative: parallel domain specialists plus an
evidence-weighted reducer, only when they inspect different evidence or use
different tools.

Default limits:

```text
max_agent_steps = 6
max_retries = 1
tool_timeout = explicit
final_output = validated structure
```

LangGraph always supplies the bounded model → tools → validation → repair/end
control flow. Add checkpoint persistence, interrupts, parallel nodes, or extra
business-stage nodes only when the selected journey needs them.

### 8.2 Knowledge and RAG

Grounding is mandatory for the target demo; vector RAG is conditional.

1. **Direct source/structured lookup**
   - Pros: minimal ingestion, exact and easy to defend.
   - Cons: weak for a large prose corpus.
   - Use for small files, tables, product records, or API data.
2. **Metadata-aware hybrid retrieval with citations — recommended for mixed OEM material**
   - Pros: handles product IDs plus natural-language questions; strong visible
     evidence.
   - Cons: requires clean metadata and fusion.
   - Use when sources mix codes, tables, manuals, and prose.
3. **Adaptive retrieval with one evidence-grade retry**
   - Pros: a visible reliability differentiator.
   - Cons: extra latency and thresholds.
   - Use when weak retrieval is a likely demo failure and reliability is central.

Possible creative sidecars:

- a small reranker;
- parent-section expansion;
- page/image evidence previews;
- an exact SQL/specification tool; or
- a micro relational graph.

Every final result should expose:

```text
recommendation or answer
evidence IDs and citations
confidence or evidence grade
unresolved risk
next action
insufficient-evidence behavior
```

### 8.3 Micro-graph alternative

Do not implement full GraphRAG in a four-hour sprint. A case may justify a
small relational sidecar when compatibility, replacement, hierarchy, sequence,
or fault dependencies are central.

Use:

```text
entities table/file
relations table/file
deterministic neighbor/path lookup tool
hybrid document retrieval for descriptive context
relation path shown as evidence
```

This is a strong creative option for queries such as compatible parts,
replacement chains, component-to-failure relationships, or procedural
dependencies. Reject it if the team cannot name a relationship question that
ordinary retrieval answers poorly.

### 8.4 Reliability differentiator

Preferred default:

```text
retrieve evidence
  -> grade sufficiency
  -> retry once with a targeted query if weak
  -> generate a structured decision
  -> verify citation IDs
  -> answer with confidence or decline/escalate
```

This is normally more defensible than adding several runtime agents.

## 9. DeepSeek plan

Use DeepSeek as the expected primary provider, but keep provider configuration
explicit and testable.

### Default policy

- Primary: `deepseek-v4-flash`.
- Use non-thinking mode for fast routing, simple tool selection, extraction,
  and formatting unless representative tests prove a quality problem.
- Consider `deepseek-v4-pro` and thinking mode only for a high-value synthesis
  or difficult decision where the quality gain is visible.
- Do not expose private reasoning in the UI.
- Never silently fall back to a fake model or a second provider.
- If a backup provider is prepared, switching must be an explicit operator
  choice.

### Integration choice

Use LangChain's `ChatDeepSeek` integration with typed LangChain tools/messages
inside a compiled LangGraph `StateGraph`. Keep the wrapper small and verify the
current DeepSeek model name and thinking/tool behavior directly because
integration documentation may lag provider changes.

If thinking mode and tool calls are combined, the loop must preserve the
provider's required `reasoning_content` field across the tool-call turn.
Otherwise, explicitly disable thinking for the bounded tool loop.

### Token and latency controls

- Send only the evidence selected for the current step.
- Return concise structured tool results rather than whole documents.
- Set maximum steps, retries, output tokens, and tool timeouts.
- Track per-run input/output tokens and latency in traces.
- Reuse stable system/tool prefixes where the provider cache can help.
- Test one representative long-document case; a large advertised context window
  is not permission to dump the entire corpus into every request.

### Required preflight

Before the event:

1. confirm the account balance or granted token budget;
2. verify the exact active model name;
3. make one real non-thinking call;
4. make one real typed tool call;
5. validate one structured result;
6. verify streaming if the UI depends on it;
7. test the timeout/error presentation;
8. record actual token usage and latency; and
9. keep the key only in ignored environment configuration.

## 10. Coordinator, execution-mode gate, and optional fan-out

### Mandatory operating model

One participant is the **coordinator/integrator**. That participant runs the
initial configuration flow from repository adaptation through work division:

```text
adapt supplied repository
  -> ingest case and sources
  -> facilitate product/architecture decisions
  -> freeze contracts
  -> ask for final participant count
  -> choose main-only or branch fan-out
  -> if fan-out: generate only genuinely independent task packets
  -> if fan-out: define branches and merge order
  -> commit and push the coordination baseline
```

After that push, every participant has `agentsprint/` in their own clone or
local repository copy. The selected execution mode controls what happens next.

### Execution-mode gate

#### Mode A — Main-only implementation

Keep all implementation with the coordinator's main agent when any of these is
true:

- the critical path is small enough for one agent;
- tasks would edit the same files or feature;
- contracts are likely to change during implementation;
- workers would depend on unmerged peer code;
- merge/test overhead is unlikely to save wall-clock time; or
- the coordinator can finish more reliably without fan-out.

In this mode:

- the coordinator may implement the entire product on the current shared/main
  development branch;
- per-user coding branches and task packets are unnecessary;
- other participants may help with product decisions, manual testing, source
  review, or presentation, but they do not concurrently edit the same feature;
- the main agent runs the small boundary checks and the full end-to-end test;
  and
- `TEAM.md` records why main-only execution was selected.

#### Mode B — Independent branch fan-out

Use branch fan-out only when at least two implementation tasks are genuinely
independent:

- frozen inputs and outputs;
- non-overlapping writable files;
- no dependency on unmerged peer implementation;
- a self-contained completion condition;
- a small local test; and
- expected time saved exceeds coordination and merge cost.

When this gate passes, each assigned participant creates their branch from the
exact coordination-baseline commit and asks their local agent to fully
implement only that task. There is no real-time co-editing of the same feature
and no pair of agents working concurrently on overlapping files.

### Participant count

The actual number is decided at the competition. `TEAM.md`, `BOARD.md`,
`BRANCH_PLAN.md`, and the task packets are generated only after that number is
known.

The sprint director does not have to assign a coding deliverable to every
participant. It must prefer reliability and clean separation over equal
workload. Shared contracts, cross-cutting code, ambiguous boundaries, and final
integration remain with the coordinator. If too little independent work
remains, choose main-only mode.

Illustrative four-person split when fan-out passes:

| User | Branch | Fully owned outcome |
| --- | --- | --- |
| Coordinator | `feature/core-agent` | Shared contracts, agent/API critical path, integration |
| User 2 | `feature/knowledge-tool` | Source processing and knowledge/tool module |
| User 3 | `feature/judge-ui` | UI against the frozen request/result contracts |
| User 4 | `feature/validation-demo` | Independent checks, score evidence, runbook, pitch |

For three participants, combine validation/demo with the UI branch or keep it
with the coordinator—whichever avoids file overlap. If that still creates
coupling, select main-only mode. Do not split one feature between two
participants just to make workloads appear equal.

### Coordination-baseline commit

Before implementation, the coordinator commits and pushes:

- normalized case and facts;
- selected journey and differentiator;
- selected architecture and knowledge path;
- frozen request, tool, evidence, result, and UI contracts;
- repository context and baseline status;
- participant list and ownership;
- the selected execution mode;
- in branch mode, each task packet, branch name, allowed/forbidden paths, and
  merge order;
- deadlines, kill conditions, and feature-freeze time.

In branch mode, every branch records the exact base commit SHA. No participant
starts from an older local copy.

### Task-packet contract

When branch fan-out is selected, each `tasks/USER-N.md` contains:

```text
user and branch
base commit SHA
single owned outcome
why the task matters to the judge journey
allowed files/directories
forbidden/shared files
frozen input/output contracts
available sources and credentials
implementation completion criteria
one required small test or build check
expected commit(s)
handoff file and evidence
deadline
blocker and kill-condition behavior
```

Worker boot prompt:

```text
Read the repository instructions, agentsprint/START_HERE.md, and only your
assigned task packet. Create or switch to the specified branch from the exact
base commit. Fully implement the packet within its allowed paths, run the named
small test, commit the result, and write the required handoff. Do not edit
another user's feature, shared contracts, or integration files.
```

### Independent branch execution

This subsection applies only to Mode B.

Every participant:

1. pulls the coordination-baseline commit;
2. creates or checks out the assigned branch;
3. verifies the starting baseline relevant to their task;
4. asks their local agent to implement the complete task packet;
5. runs the packet's small test/build check;
6. reviews the branch diff for out-of-scope changes;
7. commits and pushes the branch; and
8. writes `handoffs/USER-N.md` with the commit SHA, files changed, test result,
   assumptions, and integration notes.

Participants do not merge their own branches into the integration branch and
do not modify another participant's branch.

If a worker discovers that the frozen contract is insufficient, they stop the
affected part and record a contract-change request. They do not independently
change the shared contract. The coordinator either absorbs the necessary change
or rejects/cuts the dependent feature.

### Branch separation rules

These rules apply only to Mode B.

- One user owns one feature outcome.
- One writable file belongs to one branch during fan-out.
- Read access may overlap; write ownership may not.
- Shared schemas, root configuration, dependency manifests, lockfiles, routing,
  orchestration state, and cross-feature glue default to the coordinator.
- A worker may add a dependency only when the task packet explicitly assigns
  the relevant manifest/lockfile; otherwise the coordinator performs it during
  integration.
- Do not use multiple agents inside one branch to work on the same feature
  unless they are read-only helpers managed by that branch owner.
- No branch continuously rebases onto incomplete peer work.
- No branch assumes an unmerged peer implementation; it codes against the
  frozen contract, fixtures, or a minimal local adapter within its own scope.

### Sequential fan-in

This subsection applies only to Mode B. Main-only execution skips directly to
the integrated journey and trust checks.

The coordinator creates or checks out a clean integration branch from the
coordination baseline and then:

1. verifies every handoff and required small test result;
2. rejects branches with scope leakage until they are corrected or trimmed;
3. merges branches in the predefined dependency order;
4. resolves integration conflicts alone;
5. runs the relevant boundary check after each merge;
6. runs the first full end-to-end journey only after all accepted branches are
   present;
7. performs narrow integration repairs in coordinator-owned files;
8. records all outcomes in `INTEGRATION_LOG.md`; and
9. merges the green integration branch to the final shared branch.

The independent branch tests prove each part locally. Only the coordinator's
integrated run proves the product works end to end.

## 11. Event-day clock

Assume 210 minutes and preserve the official shape of the build:

### T+00 to T+10 — Intake

- Load the day's instructions, files, and links.
- Create the source manifest and flag blockers.
- Do not code the case yet.

### T+10 to T+25 — Choose the idea

- Answer the five critical questions.
- Generate three candidate journeys and creative alternatives.
- Score them against value, rubric, data readiness, and risk.
- Select the primary journey and one differentiator.

Gate 1 at T+25:

- “Our agent helps ___ do ___ using ___ evidence/action.”
- The team can explain why it is not the obvious chatbot.

### T+25 to T+35 — Freeze, choose execution mode, and push

- Choose the simplest architecture that supports the journey.
- Freeze request, evidence, result, and UI contracts.
- Confirm the participant count.
- Decide main-only versus branch fan-out using the execution-mode gate.
- If fan-out passes, generate only the fully separated task packets and record
  branches, allowed/forbidden paths, and merge order.
- Commit and push the coordination baseline.
- Start the pitch skeleton.

Gate 2 at T+35:

- contracts frozen;
- knowledge path selected;
- the execution mode and rationale are recorded;
- if fan-out is selected, every assigned coder has a branch, exact base commit,
  task packet, small test, and deadline;
- in fan-out mode, no writable file or feature is owned by two users;
- risky feature has a kill condition.

### T+35 to T+100 — Implement the selected mode

- Main-only: the coordinator's main agent fully implements the vertical slice
  and runs its small boundary checks.
- Fan-out: assigned users pull the coordination baseline, implement only their
  task packets on independent branches, run their small tests, commit, push,
  and write handoffs.
- In neither mode do multiple users edit the same feature in real time.

Branch gate at T+100:

- main-only: the main implementation passes its local boundary checks; or
- fan-out: every accepted branch has a commit SHA, small-test evidence, clean
  ownership, and handoff;
- incomplete or overlapping fan-out work is cut or returned before integration.

### T+100 to T+125 — Integration or first complete run

- Main-only: run the first complete journey and repair only the smallest
  blocking boundary.
- Fan-out: the coordinator creates a clean integration branch, merges accepted
  branches in order, runs a boundary check after every merge, resolves shared
  glue, and then runs the first complete journey.

Gate 3 at T+125:

- real input reaches a real result through the intended model and at least one
  real knowledge/action tool;
- the result is visible in the UI.

If this gate fails, the coordinator cuts or repairs the smallest blocking
integration point; no second user starts shared-feature editing.

### T+125 to T+150 — Make the integrated result trustworthy

- Attach citations/evidence IDs.
- Add validation and insufficient-evidence behavior.
- Add at most one bounded repair/retrieval retry.
- Run normal, missing-data, contradictory-evidence, and tool-failure cases.
- Capture technical-checklist proof.

Gate 4 at T+150:

- grounded happy path passes;
- the failure behavior is honest and visible;
- no critical unknown remains in the judge journey.

### T+150 to T+185 — Demo freeze and rehearsal

- Stop feature work.
- Finish the result presentation and runbook.
- Rehearse the two-minute story and judge questions.
- Run the exact judge journey twice.
- Capture a backup screenshot/video/result.

### T+185 to T+210 — Contingency and submission

- Repair only demo blockers.
- Review secrets and repository status.
- Verify commit history and startup commands.
- Submit or prepare the final local demo.

## 12. Commit and evidence plan

Because repository quality and traceable history are scored:

1. create a clearly labeled pre-event neutral-starter commit;
2. coordinator commits and pushes the case, contracts, execution-mode
   decision, and coordination baseline;
3. main-only: coordinator commits the complete slice and local checks; or
4. fan-out: each assigned participant commits their feature and small-test
   evidence, then the coordinator creates integration commit(s) in documented
   merge order;
5. coordinator commits grounding/trust repairs; and
6. commit the demo freeze and final documentation.

Do not manufacture dozens of empty commits. Each milestone should correspond to
a working or decision-stable state. Keep all case-specific work distinguishable
from the neutral starter.

For each selected technical component, capture:

- its purpose;
- the failure/capability that justified it;
- source files;
- a trace, screenshot, output, or test proving it works;
- its latency/token tradeoff; and
- what would change in production.

## 13. Pre-event implementation order

When implementation is authorized, use this order:

1. initialize and verify Git, secrets handling, and toolchain;
2. implement the portable `agentsprint/` control-room templates and repository
   adapter;
3. implement the short root instructions and `$sprint-director` skill;
4. confirm the competition agent can ingest a sample instruction file and
   produce the case, questions, option pack, decisions, and work board;
5. choose and fully verify exactly one UI path:
   - existing green React/FastAPI shell, or
   - Streamlit/Gradio fallback;
6. implement the smallest LangChain/LangGraph DeepSeek runner with dependency
   injection, explicit graph nodes, and explicit limits;
7. implement typed knowledge-tool interfaces and evidence/result schemas
   without preloading a company-specific corpus;
8. verify one real DeepSeek call, tool call, structured result, error, and token
   trace;
9. verify the clean startup and one deterministic smoke path;
10. create the neutral baseline commit and rehearse the event-day intake flow.

Do not prebuild brand-specific prompts, runtime multi-agent roles, full
GraphRAG, long-term memory, or a large vector stack before the company and case
are selected.

## 14. Architecture selection summary

The default starting point is:

```text
revealed case and sources
  -> deterministic intake and validation
  -> LangChain ChatDeepSeek + 3–6 typed tools
  -> bounded LangGraph model/tool/validation workflow
  -> evidence-grade node with at most one repair
  -> structured decision package with citations and uncertainty
  -> judge-facing UI
```

Escalate only when the case proves the need:

```text
small/exact data       -> direct lookup or SQL/spec tool
mixed docs and IDs     -> metadata-aware hybrid retrieval
weak retrieval risk    -> one adaptive retry or rerank
central relationships  -> micro-graph sidecar
fixed business stages  -> deterministic workflow nodes
branch/checkpoint need  -> add checkpointer/interrupts to the existing LangGraph
distinct domain roles  -> parallel runtime specialists + reducer
consequential action   -> human approval
```

## 15. Final decision flow

```text
Ingest raw instructions and files
  -> normalize facts, constraints, and available evidence
  -> ask five high-value team questions
  -> generate 3 options + creative alternatives
  -> select one journey and one differentiator
  -> choose the simplest grounded architecture
  -> freeze interfaces
  -> ask for participant count
  -> coordinator commits and pushes the coordination baseline
  -> every user pulls it into their own copy
  -> choose implementation mode:
       main-only -> main agent implements and tests the complete slice
       fan-out   -> create independent tasks/branches
                 -> assigned users implement and small-test branches
                 -> users push handoffs
                 -> coordinator integrates sequentially
  -> run the first real end-to-end path
  -> add citations, validation, and one bounded repair
  -> freeze features
  -> rehearse, capture evidence, and submit
```

Key decisions:

- The brand remains intentionally undecided until later.
- LangChain and a bounded LangGraph are mandatory; advanced graph features are
  conditional.
- Grounding through a knowledge tool is mandatory for the score target; vector
  RAG is conditional.
- DeepSeek V4 Flash is the primary low-cost path; Pro/thinking is an explicit
  quality escalation.
- One central differentiator is selected before coding and judged by expected
  score.
- A micro relational graph is a case-specific creative sidecar, not a default
  GraphRAG build.
- One coordinator runs configuration through work division and pushes the
  coordination baseline before implementation.
- Every participant has `agentsprint/` in their repository copy, but coding
  branches are created only when independent fan-out passes the gate.
- Human work, local coding agents, and runtime product agents are planned
  separately.
- Main-only implementation is valid whenever it is simpler or safer.
- When branch fan-out is used, writers start from the exact frozen baseline,
  use non-overlapping ownership, and never work on the same feature in real
  time.
- The coordinator owns shared code, sequential integration, conflicts, and the
  full end-to-end test, even when that produces an intentionally larger task.
- Feature work stops at T+150 so the last 35 minutes remain for the demo, with
  a final contingency window.
- The repository must show real integrations, evidence, secrets discipline, and
  a traceable milestone history.
