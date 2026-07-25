# Sprint Control

Status: `CASE SHAPED / COORDINATION BASELINE NOT COMMITTED`

| Field | Current value |
| --- | --- |
| Clock / feature freeze | Not started / T+150 |
| Stage | Gate 2 preparation |
| Primary journey | Supplied information → inventory/classification → specialized extraction → normalization → entities/relations → RAG/storage design → indexing → validation → query-ready KB |
| Central differentiator | Evidence-grounded adaptive knowledge-base compiler, not fixed document chat |
| Coordinator / integrator | Usuario 1; real name pending |
| Execution mode | Independent branch fan-out after C-01 and coordination-baseline commit |
| Current blocker | Real SICK corpus, five intake answers, participant names, and DeepSeek key are absent |
| Next integration point | Resolve C-01, confirm boundary v0.1, commit baseline, then copy exact SHA into all packets |
| Scope cut line | No feature implementation or feature branches before the baseline; no complexity unsupported by owner research |

## Gate status

- [x] Gate 1 — provisional value sentence and non-obvious differentiator selected
- [ ] Gate 2 — real inputs confirmed, contracts accepted, baseline committed,
  and exact branch SHA recorded
- [ ] Gate 3 — real input reaches a visible result through model + real tool
- [ ] Gate 4 — grounding and honest failure cases pass
- [ ] Demo freeze — exact judge journey passes twice and backup exists

## Ownership rule

Each owner has authority over the method inside their assigned phases and write
scope. Usuario 1 owns adaptive RAG strategy and shared integration; that role
does not prescribe Usuario 2 or Usuario 3 internal choices.

## Current starter evidence

- Streamlit remains a verified fallback while Usuario 3 owns the independent web
  experience.
- The runtime uses LangChain `ChatDeepSeek`, typed LangChain tools/messages, and
  a compiled bounded LangGraph `StateGraph`.
- The deterministic smoke is dependency-injected and cannot become a silent
  application fallback.
- Locked Python 3.12 restore, lint, tests, deterministic smoke, control-room
  validation, secrets scan, and a live Streamlit health probe were green in the
  neutral starter baseline.
- The real-provider preflight stops explicitly because `LLM_API_KEY` is absent;
  no fallback is used.
