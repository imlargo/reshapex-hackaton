# Option Packs

## Decision: product direction

Constraints/evidence:

- `SRC-001` asks for an agent that adapts documentation preparation,
  relationship discovery, and storage to the information supplied.
- No SICK corpus, user interview, deployment constraint, or target data store
  has been supplied.
- The repository already provides a bounded evidence-grounded agent path.
- This decision selects the product promise, not the implementation. Each
  workstream owner retains authority to research and choose the method inside
  the frozen integration boundaries.

### Option A — fixed document RAG

Use one ingestion and retrieval strategy for all accepted documents.

- Pros: smallest delivery risk and easy to explain.
- Cons: only partially addresses the adaptive behavior in the brief and is
  difficult to distinguish from ordinary document chat.
- Estimated effort: low.

### Option B — adaptive knowledge-base compiler

Inspect the supplied corpus, produce an explainable build decision, create the
knowledge base, and expose grounded results plus provenance. The responsible
owners research and decide the cleaning, retrieval, relation, and storage
approaches after examining the real evidence.

- Pros: directly answers the brief; makes technical decisions visible; gives
  each specialist a meaningful autonomous problem.
- Cons: requires stable seams and measurable evidence for each decision.
- Estimated effort: medium.

### Option C — broad knowledge platform

Create a multi-store, multi-agent platform with semantic retrieval, graph
reasoning, lifecycle management, and several user journeys from the start.

- Pros: high ceiling.
- Cons: unjustified without data; large integration and demo risk.
- Estimated effort: high.

### Creative alternative

A change-impact knowledge agent could prioritize relationships between
versions, dependencies, and affected assets. It becomes the main journey only
if the supplied evidence and user pain support that question.

Scores use 1-5, where 5 is best. Weighted total uses user value 20%,
innovation 20%, trust 15%, demo clarity 15%, data readiness 10%, time 10%, and
risk control 10%.

| Option | User value | Innovation | Trust | Demo | Data ready | Time | Risk control | Weighted total |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| A | 3 | 2 | 5 | 4 | 5 | 5 | 5 | 3.85 |
| B | 5 | 5 | 4 | 5 | 4 | 4 | 4 | **4.55** |
| C | 4 | 5 | 3 | 4 | 2 | 2 | 2 | 3.45 |

Recommendation: Option B.

Decision deadline: before the coordination baseline is committed.

Kill/revisit conditions:

- Fall back to Option A if the adaptive decision cannot be demonstrated
  reliably by the feature-freeze threshold.
- Expand toward Option C only when the corpus and a failed acceptance test
  prove the need.
- Workstream owners may change their internal approach without team approval
  when their public contract and completion evidence remain intact.
