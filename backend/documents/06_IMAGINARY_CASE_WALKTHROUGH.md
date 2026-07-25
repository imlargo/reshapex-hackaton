# Imaginary AgentSprint Walkthrough

Status: planning example only. The repository, company, data, tools, agents, and
application described here are fictional. Nothing in this walkthrough has been
implemented.

This document shows how the revised plan should feel in practice:

1. the human team receives a starter repository and case files;
2. the portable `agentsprint/` folder is added without disturbing that
   repository;
3. one coordinator runs the sprint director through the execution-mode decision
   and pushes that coordination baseline;
4. this fictional team selects branch fan-out because four outcomes are
   genuinely independent; every participant pulls the folder and completes one
   local branch;
5. the coordinator merges the tested branches into one grounded vertical slice;
6. the team validates, cuts scope, and prepares the demonstration.

The walkthrough is deliberately more concrete than the master plan. It is not
a preselected solution for the real event.

## 1. Imaginary morning package

At 8:00 AM, the organizers reveal the fictional brand **Andina Motion**, an OEM
and distributor of industrial motor drives.

The case says:

> Maintenance teams lose time replacing discontinued variable-frequency
> drives. Build an agent that uses the supplied product knowledge to help a
> technician choose and justify a safe replacement.

The organizers provide:

```text
starter-repository/
  README.md
  AGENTS.md
  backend/
    app/
      main.py
      routes.py
  frontend/
    package.json
    src/
      App.tsx
  tests/
  pyproject.toml
  uv.lock
  package-lock.json

case-files/
  event-instructions.pdf
  legacy-drives.pdf
  current-catalog.pdf
  compatibility.csv
  inventory.csv
  safety-bulletin.pdf
```

The starter README says that FastAPI and React already run. Its root
`AGENTS.md` says to use the existing schemas, run `uv run pytest`, and avoid
editing `backend/app/vendor/`.

This is exactly why the control room must be repository-compatible: replacing
the stack or overwriting the repository instructions would waste time and
could break the supplied baseline.

## 2. Adding and distributing the portable folder

Human 1 is selected as coordinator/integrator. Human 1 copies one folder into
the supplied repository:

```text
starter-repository/
  AGENTS.md                 # supplied; unchanged
  backend/                  # supplied; unchanged
  frontend/                 # supplied; unchanged
  tests/                    # supplied; unchanged
  agentsprint/              # team control room
    START_HERE.md
    AGENT_PLAYBOOK.md
    CONTROL.md
    REPOSITORY_CONTEXT.md
    ...
```

The coordinator does not copy a new root `AGENTS.md`, reinitialize Git, replace
lockfiles, or scaffold another backend. The other participants do not run
independent intake/configuration flows.

The human operator starts the main Codex task with:

```text
Read agentsprint/START_HERE.md and act as the sprint director for this
repository. First adapt the control room to the existing repository and ingest
the supplied case. Do not change application code until the first journey,
architecture, and ownership gates are recorded.
```

Human 1 facilitates the decisions with the whole team, populates
`agentsprint/`, freezes the contracts, and learns that the team has four
participants. The execution-mode gate finds four genuinely independent
outcomes, so this example creates four fully separated task packets. This is a
case decision, not a universal requirement.

Human 1 then commits and pushes the coordination baseline. Every participant
pulls or clones that exact commit. At that point all four local repository
copies contain the same `agentsprint/` folder, task definitions, contracts, and
branch plan.

## 3. Repository adaptation in action

The sprint director first reads the supplied root instructions and repository
README, then inspects only the paths needed to understand the existing
application.

It writes the following illustrative content to
`agentsprint/REPOSITORY_CONTEXT.md`:

```md
# Repository context

- Repository mode: starter
- Repository root: `.`
- Existing instructions: `AGENTS.md`
- Existing stack: Python 3.12, FastAPI, React/Vite, uv, npm
- Install: `uv sync --locked`; `npm --prefix frontend ci`
- Backend run: `uv run uvicorn backend.app.main:app --reload`
- Frontend run: `npm --prefix frontend run dev`
- Checks: `uv run pytest`; `npm --prefix frontend run build`
- Backend entry point: `backend/app/main.py`
- Frontend entry point: `frontend/src/App.tsx`
- Protected path: `backend/app/vendor/`
- Existing API convention: Pydantic request/response models in
  `backend/app/schemas.py`
- Baseline: tests and frontend build pass before case changes
- Working tree: clean
- Integration owner: Human 1
```

It writes a concise map to `agentsprint/REPOSITORY_MAP.md`, using
repository-relative paths only.

If the baseline test had already failed, the agent would record that failure
before changing code. It would not silently “fix everything” or blame the case
implementation.

## 4. Case-file intake

The case files are copied into `agentsprint/00_inbox/raw/`. The originals remain
unchanged.

During initial configuration, only Human 1's sprint-director agent inventories
the sources and samples enough content to support the team decisions. No other
participant begins implementation or full document processing yet. Cleaning,
validation, and tool-ready conversion are assigned later to Human 2's branch.

An illustrative source manifest becomes:

| ID | Source | Type | Primary use | Owner | Status |
| --- | --- | --- | --- | --- | --- |
| EVT-01 | event-instructions.pdf | PDF | Official constraints | Human 1 | normalized for decisions |
| LEG-01 | legacy-drives.pdf | PDF | Legacy model specifications | Human 2 | pending branch work |
| CAT-01 | current-catalog.pdf | PDF | Replacement candidates | Human 2 | pending branch work |
| CMP-01 | compatibility.csv | CSV | Valid replacement relations | Human 2 | pending branch work |
| INV-01 | inventory.csv | CSV | Current stock | Human 2 | pending branch work |
| SAF-01 | safety-bulletin.pdf | PDF | Prohibited combinations | Human 2 | pending branch work |

After fan-out, Human 2's branch writes derived text and tables under
`agentsprint/05_knowledge/`, and every record retains its source ID.

## 5. Human-level decision flow

### 5.1 The sprint director asks five questions

The sprint director does not immediately propose GraphRAG or start editing the
backend. It asks:

1. Who has the painful decision, and what does it cost today?
2. What exact input can the live demo reliably receive?
3. What grounded output would prove value in under two minutes?
4. What obvious solution will other teams build, and how should this be
   different?
5. Which data, credentials, and team skills are actually available?

The fictional team answers:

```text
1. A field maintenance technician; today they search several PDFs and call a
   product specialist. A wrong replacement can stop a production line.
2. A discontinued model number plus motor voltage, power, and enclosure needs.
3. A recommended replacement with compatibility reasons, safety warnings,
   evidence, stock status, and a next action.
4. Others may build generic catalog chat. Ours should produce an auditable
   replacement decision, not just answer questions.
5. We have the supplied PDFs/CSVs, DeepSeek tokens, two Python developers, one
   React developer, and one strong presenter/tester. There is no live ERP API.
```

The conditional follow-ups are:

```text
- Should the agent ever recommend a part if safety evidence is missing?
  Answer: No. It must decline or ask for a product specialist.

- Are compatibility relations central enough to justify relational lookup?
  Answer: Yes. The CSV contains explicit replaces/is-compatible-with/
  prohibited-with relations.

- What is the kill condition for the relational differentiator?
  Answer: If the first compatibility path is not working by T+95, replace it
  with direct CSV filtering and keep the same result contract.
```

These answers are recorded; they do not remain only in chat.

### 5.2 Product option pack

The sprint director creates three feasible journeys plus a creative
alternative.

#### Option A — Catalog Q&A

The technician asks questions and receives cited catalog answers.

- Pros: fastest and easiest to ground.
- Cons: obvious; weak action value; little differentiation.
- Risk: low.
- Likely score: strong progress, modest innovation.

#### Option B — Evidence-first replacement advisor

The technician enters an old part and requirements. The system returns a
structured replacement decision with evidence, confidence, unresolved risks,
and stock status.

- Pros: concrete business value; visually demonstrable; strong trust story.
- Cons: needs exact data validation and a structured result.
- Risk: moderate.
- Likely score: best expected total.

#### Option C — Multi-agent maintenance desk

Separate catalog, safety, and inventory agents produce opinions that a
supervisor combines.

- Pros: visually “agentic”; parallel specialist story.
- Cons: extra calls, latency, conflicts, and reducer complexity; roles use much
  of the same data.
- Risk: high.
- Likely score: higher architecture ambition but lower completion probability.

#### Creative alternative — Compatibility-path explainer

Add a small deterministic relation tool that shows:

```text
LegacyDrive-7
  -> replaced_by Drive-X2
  -> requires_enclosure IP55
  -> prohibited_with Firmware<3.1
```

This is not full GraphRAG. It is a micro-graph sidecar derived from the supplied
compatibility table.

The sprint director recommends **Option B plus the compatibility-path
explainer**. The team accepts it because the relation path is central,
implementable, evidence-visible, and different from catalog chat.

The decision log records why Options A and C were rejected and the T+95 kill
condition.

### 5.3 Architecture option pack

The sprint director then presents:

#### Architecture A — Deterministic LangGraph form and rules

- Validate inputs.
- Filter compatibility and inventory tables.
- Format a result with one model call.

Pros: very reliable.  
Cons: model has little real tool-selection responsibility.

#### Architecture B — One bounded LangGraph agent with typed LangChain tools

- DeepSeek chooses among four narrow tools.
- Maximum six steps.
- Evidence is graded once before the final result.

Pros: genuinely agentic, understandable, and bounded.  
Cons: tool contracts and stopping behavior must be tested.

#### Architecture C — Expanded business-stage workflow graph

- Intake → retrieve → safety → inventory → verify → result.
- Add model decisions inside selected nodes.

Pros: clear stages and trace.  
Cons: more state/framework work than the case requires.

All three options use the mandatory LangChain/LangGraph core. They differ in
how much decision-making and business-stage topology the graph contains.

The team selects **Architecture B**. The mandatory LangGraph remains a compact
model → tools → validation graph; an expanded business-stage graph and runtime
subagents fail the necessity gate for this case.

## 6. Frozen journey and contracts

The primary journey is written before parallel coding:

> A technician submits discontinued model `LegacyDrive-7`, 480 V, 15 kW, IP55.
> The agent retrieves specifications, follows the valid replacement relation,
> checks the safety bulletin and stock table, then returns a cited decision
> package or declines when evidence is insufficient.

An illustrative request contract:

```json
{
  "legacy_model": "LegacyDrive-7",
  "voltage_v": 480,
  "power_kw": 15,
  "required_enclosure": "IP55"
}
```

An illustrative final result:

```json
{
  "status": "recommended",
  "recommended_model": "Drive-X2",
  "reasons": [
    {
      "claim": "Drive-X2 is the approved replacement for LegacyDrive-7.",
      "evidence_ids": ["CMP-01:R14"]
    },
    {
      "claim": "The selected variant supports 480 V, 15 kW, and IP55.",
      "evidence_ids": ["CAT-01:P42", "CAT-01:P44"]
    }
  ],
  "compatibility_path": [
    "LegacyDrive-7",
    "replaced_by:Drive-X2",
    "requires:Firmware>=3.1"
  ],
  "safety_warnings": [
    {
      "text": "Do not commission with firmware below 3.1.",
      "evidence_ids": ["SAF-01:P2"]
    }
  ],
  "stock": {
    "status": "available",
    "quantity": 3,
    "evidence_ids": ["INV-01:R8"]
  },
  "confidence": "high",
  "unresolved_risks": [],
  "next_action": "Confirm motor current and request technician approval."
}
```

The insufficient-evidence response uses the same schema but sets
`status: "needs_review"`, provides no unsupported part recommendation, and
identifies the missing evidence.

Once these contracts are recorded in `agentsprint/03_contracts/`, only the
integrator may change them during the slice.

## 7. Human workstream and branch assignment

Before assigning branches, the sprint director compares the two modes:

```text
Main-only:
- valid if the implementation is small or coupled;
- no artificial task division;
- Human 1's main agent owns the whole code path.

Branch fan-out:
- knowledge tool, core agent, UI, and validation artifacts have frozen
  contracts and non-overlapping files;
- each has a meaningful small test;
- expected time saved exceeds merge cost.
```

For this imaginary case, branch fan-out passes. If the UI and backend both
needed continuous schema changes, the team would choose main-only instead and
Human 1 would implement the entire slice without creating coding branches.

At T+35, `agentsprint/04_workstreams/BOARD.md` contains:

| ID | Owner and branch | Complete outcome | Exclusively owned paths | Small test | Deadline |
| --- | --- | --- | --- | --- | ---: |
| W1 | Human 1 — `feature/core-agent` | Bounded DeepSeek loop, shared schemas, route, integration glue | `backend/app/agent/`, assigned route/schema files, shared manifests | Backend import plus tool-loop smoke | T+100 |
| W2 | Human 2 — `feature/knowledge-tool` | Clean sources and complete deterministic knowledge/tool module | `agentsprint/05_knowledge/`, `backend/app/case_data/` | Knowledge-tool lookup smoke | T+80 |
| W3 | Human 3 — `feature/judge-ui` | Complete input, trace, evidence, and result UI against frozen fixtures | Explicitly listed `frontend/src/` files | Production frontend build | T+95 |
| W4 | Human 4 — `feature/validation-demo` | Demo cases, score evidence, runbook, pitch, and a standalone API smoke fixture | `agentsprint/06_validation/`, `agentsprint/07_demo/`, assigned test file | Named validation smoke | T+85 |

The board also states:

- Human 1 owns integration and shared schemas.
- Human 2 does not edit UI or route schemas.
- Human 3 does not change backend contracts.
- Human 4 does not repair another user's feature.
- Dependency manifests, lockfiles, root configuration, shared routing, and
  cross-feature glue belong to Human 1.
- No writable file appears in two task packets.
- A worker who needs a shared-contract change records the blocker and returns it
  to Human 1 instead of changing the contract.

The task packets are:

```text
agentsprint/04_workstreams/tasks/USER-01.md
agentsprint/04_workstreams/tasks/USER-02.md
agentsprint/04_workstreams/tasks/USER-03.md
agentsprint/04_workstreams/tasks/USER-04.md
```

Each packet names the same illustrative fan-out base:

```text
coordination baseline: a1b2c3d
```

Human 1 pushes `a1b2c3d` before anyone starts implementation. For a
three-person team, the sprint director would combine validation/demo with the
UI or coordinator task—whichever creates no file overlap.

## 8. Agentic coding workflow

### 8.1 Coordinator finishes configuration and fans out

Before code implementation, Human 1's sprint-director agent:

1. confirms the supplied baseline still passes;
2. records the case, choices, and architecture;
3. freezes the typed tool and final-result contracts;
4. writes all four task packets and branch names;
5. verifies every writable path has exactly one owner;
6. defines merge order and branch tests;
7. commits and pushes baseline `a1b2c3d`; and
8. tells every participant to pull that exact commit.

Human 1's initial configuration responsibility ends at this work-division
push. Human 1 then creates `feature/core-agent` in their own local copy and asks
their coding agent to implement the complete coordinator packet.

The coding agent does not rebuild the existing FastAPI app, migrate to another
frontend, or add a vector database merely because those appeared in an earlier
generic plan.

It does not rebuild the existing FastAPI app, migrate to another frontend, or
add a vector database merely because those appeared in an earlier generic plan.

### 8.2 Typed tool design

The imaginary product exposes:

```text
lookup_legacy_spec(model_id)
  -> exact specifications + evidence IDs

search_current_catalog(requirements)
  -> candidate records + evidence IDs

trace_compatibility(legacy_id, candidate_id)
  -> valid relation path or explicit failure + evidence IDs

check_inventory(model_id)
  -> stock result + evidence ID
```

Safety evidence can either be a fifth narrow tool or mandatory metadata returned
by the compatibility tool. The team chooses the design that produces fewer
ambiguous calls.

Every tool has:

- typed inputs and concise structured outputs;
- source/evidence IDs;
- a timeout;
- an actionable error;
- no hidden model call; and
- deterministic behavior for the supplied data.

### 8.3 DeepSeek loop

The illustrative runtime is:

```text
validate request deterministically
  -> DeepSeek V4 Flash, non-thinking mode
  -> tool request
  -> execute typed tool
  -> append concise result
  -> repeat, maximum 6 steps
  -> grade evidence sufficiency
  -> retry retrieval once if the grade is weak
  -> validate final structured result
  -> verify every cited evidence ID exists
  -> return result or needs_review
```

The model does not receive entire PDFs. It receives relevant structured tool
results and selected evidence excerpts.

### 8.4 Independent local branch agents

Every participant starts from `a1b2c3d`, checks out only the assigned branch,
and gives their local agent this shape of instruction:

```text
Read the repository instructions, agentsprint/START_HERE.md, and your assigned
USER-N task packet. Work only on the named branch and allowed paths. Fully
implement the outcome, run the required small test, review the diff, commit and
push it, and write the handoff. Do not modify shared contracts or another
user's feature.
```

The branch agents are bounded:

#### Human 2 branch agent

```text
Input:
LEG-01, CAT-01, CMP-01, INV-01, SAF-01

Output:
cleaned artifacts, schema notes, rejected rows, source lineage, and one
handoff to the integrator

Write scope:
agentsprint/05_knowledge/ and the explicitly assigned case-data module

Required test:
one deterministic legacy-model/compatibility lookup
```

#### Human 3 branch agent

```text
Input:
frozen request/result schema and existing React conventions

Output:
input form, visible tool timeline, compatibility path, evidence cards,
warning state, and production-build result

Write scope:
explicit frontend files only

Required test:
npm production build using frozen result fixtures
```

#### Human 4 branch agent

```text
Input:
primary journey, acceptance criteria, named commands

Output:
pass/fail evidence, first blocking failure, and smallest repair action

Write scope:
validation/demo artifacts and one explicitly assigned smoke file only

Required test:
the named smoke against frozen fixtures
```

Each person reviews their own branch diff, commits, pushes, and writes a handoff
containing the commit SHA and test output. Nobody merges into the integration
branch. These are local development agents; the running application still
contains one product agent.

## 9. Sequential merge and first integrated run

At T+100, the handoffs are:

| Branch | Commit | Local evidence |
| --- | --- | --- |
| `feature/knowledge-tool` | `b2c3d4e` | Knowledge lookup smoke passes |
| `feature/core-agent` | `c3d4e5f` | Backend import and tool-loop smoke pass |
| `feature/judge-ui` | `d4e5f6a` | Production frontend build passes |
| `feature/validation-demo` | `e5f6a7b` | Validation fixture smoke passes |

Human 1 creates `integration/demo` from `a1b2c3d` and merges in the recorded
order:

```text
feature/knowledge-tool
  -> feature/core-agent
  -> feature/judge-ui
  -> feature/validation-demo
```

Human 1 alone resolves integration conflicts and shared glue. A branch with
out-of-scope edits would be rejected or trimmed before merge.

At T+122, after all four accepted branches are present, the first integrated
trace looks like:

```text
1. request_validated
2. lookup_legacy_spec("LegacyDrive-7")
   -> 480 V, 15 kW; LEG-01:P18
3. search_current_catalog(...)
   -> Drive-X2, Drive-Z4; CAT-01:P42, CAT-01:P51
4. trace_compatibility("LegacyDrive-7", "Drive-X2")
   -> valid path; CMP-01:R14; firmware constraint SAF-01:P2
5. check_inventory("Drive-X2")
   -> available: 3; INV-01:R8
6. evidence_grade
   -> sufficient
7. structured_result_validated
8. citation_ids_verified
```

The UI shows the recommendation, compatibility path, safety warning, stock, and
clickable or expandable evidence. It does not show private chain-of-thought.

This reaches the first useful vertical-slice gate.

## 10. Trust and failure testing

The verifier has prepared:

| Case | Expected behavior |
| --- | --- |
| Valid legacy model and requirements | Grounded recommendation |
| Unknown model | `needs_review`; no invented replacement |
| Candidate fits power but violates voltage | Candidate rejected |
| Compatibility path exists but safety bulletin is missing | No recommendation; missing evidence named |
| Inventory tool fails | Compatibility answer remains, stock marked unavailable/unknown |
| Prompt injection inside a PDF | Treated as source content, not an instruction |
| Contradictory catalog and compatibility table | Conflict surfaced and escalated |

### Example failure

At T+132, an integrated test reveals that the model recommends `Drive-Z4` because its prose
description is semantically similar, even though the compatibility table has no
valid relation.

The coordinator owns the narrow integration repair:

1. make a valid compatibility path a deterministic requirement for
   `status: recommended`;
2. reject results whose evidence lacks a compatibility source ID;
3. rerun that exact failure;
4. rerun the happy path; and
5. record the repair in `agentsprint/04_workstreams/integration/INTEGRATION_LOG.md`.

The team does not respond by adding a second supervisor agent or rebuilding the
retrieval stack, and no second user begins editing the same backend feature.

### Example scope cut

Suppose the compatibility-path visual is still broken at T+95. The kill
condition fires:

- retain direct CSV compatibility validation;
- return the matched relation row as evidence;
- remove the interactive graph visual;
- keep the structured recommendation and trust behavior.

The differentiator becomes an evidence-first replacement decision rather than
a graph visualization. The stable demo remains more important.

## 11. Branch and commit sequence selected for this case

The supplied Git history is preserved. Illustrative event-day commits are:

```text
main/coordinator:
  a1b2c3d case: freeze Andina Motion contracts and branch plan

feature/knowledge-tool:
  b2c3d4e feat: implement grounded replacement knowledge tools

feature/core-agent:
  c3d4e5f feat: implement bounded replacement agent and API

feature/judge-ui:
  d4e5f6a feat: display replacement evidence and safety decision

feature/validation-demo:
  e5f6a7b test: add judge cases, score evidence, and runbook

integration/demo:
  f6a7b8c merge: integrate independent AgentSprint workstreams
  a7b8c9d fix: require verified compatibility path for recommendations
  b8c9d0e demo: freeze integrated runbook and judge journey
```

The baseline starter commit remains visible before these commits. Secrets,
derived indexes, virtual environments, and local build output are not committed.

Human 1 integrates every branch in the predetermined dependency order:

```text
case data/tool
  -> backend runner and route
  -> frontend result view
  -> trust repair
  -> demo artifacts
```

## 12. Score evidence in action

An illustrative `SCORECARD.md` contains:

| Dimension | Claim | Proof |
| --- | --- | --- |
| Progress | Live request reaches grounded answer | Recorded judge journey and successful trace |
| Progress | All material claims use knowledge tools | Evidence IDs attached to every reason/warning |
| Innovation | Agent produces an auditable replacement decision | Structured decision package and compatibility path |
| Technical | Typed tool calling works | Tool trace plus tool contract |
| Technical | Evidence validation works | Missing/contradictory evidence cases |
| Technical | Bounded repair works | One weak-evidence retry trace |
| Technical | Structured output validation works | Validated result and rejected malformed case |
| Code quality | Real integrations and clean secrets | Source inspection, environment configuration, commits |
| Presentation | Clear two-minute story | Rehearsed runbook and prepared judge Q&A |

The team claims only components it can prove.

## 13. Two-minute demonstration

### Opening

> A technician replacing a discontinued drive currently searches multiple
> manuals and calls a specialist. A plausible but incompatible replacement can
> stop a production line.

### Live action

1. Enter `LegacyDrive-7`, 480 V, 15 kW, IP55.
2. Run the agent.
3. Show the typed knowledge tools executing.
4. Reveal `Drive-X2`.
5. Expand the compatibility path, safety warning, and evidence.
6. Show current stock and the required next approval.

### Trust moment

Change the enclosure requirement to an unsupported value. The agent declines to
recommend a part and identifies the missing compatible evidence.

### Close

> This is not catalog chat. It is a bounded, evidence-first replacement
> decision that tells the technician what is known, what is unsafe, and what
> must happen next.

## 14. Human versus agent responsibilities

Because this fictional case selected Mode B, the responsibilities below include
branch fan-out. In Mode A, the coordinator/main agent would absorb all coding,
small tests, and integration responsibilities.

### Humans decide together before fan-out

- target user and pain;
- primary journey;
- central differentiator;
- acceptable safety behavior;
- architecture escalation;
- work ownership;
- risky-feature kill conditions;
- feature freeze; and
- final pitch claims.

### Coordinator/integrator owns

- repository adaptation and baseline;
- intake and decision recording;
- final participant count;
- frozen contracts;
- one non-overlapping task packet and branch per assigned coder in this
  fan-out;
- the coordination-baseline push;
- all shared/overlapping implementation;
- sequential merges and conflict resolution;
- integration repairs;
- the full end-to-end test; and
- demo freeze.

### Sprint director facilitates and records

- source inventory;
- high-value questions;
- option packs and comparisons;
- dependency-aware work board;
- contract freeze;
- checkpoints and scope cuts;
- score evidence; and
- demo readiness.

### Each participant and local coding agent execute

- bounded code mapping;
- isolated document cleaning;
- one complete assigned branch outcome;
- only the packet's writable paths;
- the named small test/build check;
- a reviewed commit and pushed branch; and
- a concise handoff with commit SHA and evidence.

No participant implements or repairs another participant's feature in real
time.

### Runtime product agent performs

- bounded tool selection;
- evidence gathering;
- decision synthesis;
- structured answer generation; and
- escalation when evidence is insufficient.

The runtime agent does not decide the team's product strategy or rewrite its
own architecture during the demonstration.

## 15. End-to-end summary

```text
Organizer starter repository + case files
  -> coordinator copies in portable agentsprint/ folder
  -> coordinator reads repository instructions and verifies baseline
  -> team manifests evidence and answers five product questions
  -> compare 3 journeys + creative alternative
  -> select journey, architecture, and differentiator
  -> freeze request/result/tool/UI contracts
  -> confirm participant count
  -> compare main-only with branch fan-out
  -> this case passes fan-out
  -> create one non-overlapping task packet and branch per participant
  -> coordinator commits and pushes the coordination baseline
  -> all participants pull it into their own copies
  -> every local coding agent fully implements and small-tests one branch
  -> participants commit, push, and hand off their branches
  -> coordinator merges branches sequentially
  -> run the first integrated real tool path
  -> validate citations and insufficient-evidence behavior
  -> repair one reproduced failure
  -> cut risky extras at their deadline
  -> freeze features at T+150
  -> rehearse, capture evidence, and submit
```

The main lesson is that the control room does not predetermine the real
solution or force parallel work. It makes the team's product decisions
explicit, chooses main-only or safe fan-out based on the actual case, and keeps
the implementation tied to a grounded live demo.
