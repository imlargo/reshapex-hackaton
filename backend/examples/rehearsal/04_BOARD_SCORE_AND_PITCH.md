# Rehearsal Board, Score, and Pitch

| ID | Outcome | Owner | Dependency | Check | Deadline |
| --- | --- | --- | --- | --- | --- |
| R-1 | normalize sources with IDs | source reviewer | baseline | spot-check 3 records | T+55 |
| R-2 | implement complete triage slice | coordinator | frozen contracts | deterministic + real boundary | T+100 |
| R-3 | run failure cases | verifier | R-2 | failure table | T+150 |
| R-4 | rehearse and capture backup | presenter + team | R-3 | path twice | T+185 |

Score evidence: a real model/tool/cited result; evidence-grade retry/decline as
the central innovation; typed lookup, validation, and trace; a two-minute
before/after story; locked setup, no credentials, honest unavailable API, and
milestone commits.

Pitch thesis: “Service coordinators should not ask a manual chatbot whether a
pump is safe. Northstar Triage cross-checks the exact asset and current service
evidence, shows why it recommends shutdown/inspection/escalation, and refuses
to overclaim when evidence is weak.”
