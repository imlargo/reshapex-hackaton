# AgentSprint playbook

Use this workflow after reading `START_HERE.md`. It supplements but never
overrides host-repository instructions.

## 1. Adapt

- Classify the repository as blank, starter, monorepo, or existing product.
- Record manifests, lockfiles, commands, entry points, integrations, protected
  paths, working-tree state, and pre-existing failures.
- Reuse a supplied green stack. Do not replace it merely by preference.

## 2. Intake

- List each supplied file and link.
- Assign `SRC-NNN` IDs before deriving content.
- Sample only enough content to judge format, scope, relevance, blockers, and
  confidentiality.
- Separate organizer facts from team assumptions.
- Preserve raw sources; put derived artifacts under `05_knowledge/`.

## 3. Ask one compact round

1. Who experiences the painful decision/action, and what does it cost today?
2. What exact input can the live demo reliably receive?
3. What grounded recommendation/action proves value in under two minutes?
4. What would the obvious “chat with documents” solution do, and how is ours
   meaningfully different?
5. Which documents, APIs, data, credentials, and team skills exist now?

Ask at most three follow-ups only when they change the journey, architecture,
evidence, ownership, safety behavior, or kill condition.

## 4. Decide

For each consequential decision, write three options and creative
alternatives. Score user value, innovation, grounding, demo clarity, data
readiness, integration time, and failure risk. Recommend the best expected
score, record the choice, and state a revisit trigger.

Default architecture:

```text
deterministic intake
  -> LangChain ChatDeepSeek + 3–6 typed tools
  -> one bounded LangGraph workflow
  -> evidence sufficiency check + at most one repair
  -> structured cited result
  -> judge-facing UI
```

Escalate only when the case proves a need: hybrid retrieval, micro-graph,
additional deterministic business nodes, LangGraph persistence/interrupts,
runtime specialists, or human approval.

## 5. Freeze and divide

- Freeze the request, evidence, tool, result, and UI contracts.
- Ask for the actual participant count.
- Choose main-only whenever tasks overlap, contracts may move, or merge cost is
  unlikely to save time.
- Fan out only independent outcomes with frozen inputs/outputs,
  non-overlapping writable paths, one local check, and no dependency on
  unmerged peer code.
- In fan-out mode, create one packet per assigned user from the exact baseline
  commit and define sequential merge order first.

## 6. Build and prove

- Implement one thin vertical slice before secondary features.
- Make evidence IDs, uncertainty, and failure behavior visible.
- Keep the scorecard current with actual source/test/trace/screenshot proof.
- At T+150 stop features. Run normal, missing-data, contradictory-evidence, and
  tool-failure cases; rehearse the exact journey twice; capture a backup.
