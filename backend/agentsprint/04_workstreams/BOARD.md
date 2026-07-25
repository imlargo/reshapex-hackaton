# Work Board

This is the only sprint task board. Owners control method and subtask
decomposition inside their outcome.

| ID | Outcome | Owner | Depends on | Write scope | Small check | Deadline | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C-01 | Confirm persona, demo input/result, sources, constraints, and names | team | `SRC-001` | case/decision files via Usuario 1 | five-question round resolved | before implementation | open |
| C-02 | Freeze and commit coordination baseline; place exact SHA in packets | Usuario 1 | C-01 | shared contracts/control room | Gate 2 checklist | before branches | blocked by C-01 |
| U1-R | Investigate corpus classification plus candidate RAG, storage, indexing, and retrieval strategies; select approach | Usuario 1 | C-02 + sample corpus | Usuario 1 paths | owner decision note + risky-assumption experiment | T+45 | blocked |
| U2-R | Investigate extraction, normalization, entity, and relationship challenges; select approach | Usuario 2 | C-02 + sample corpus | Usuario 2 paths | owner decision note + risky-assumption experiment | T+45 | blocked |
| U3-R | Investigate web journey, validation, readiness, and trust-comprehension challenges; select approach | Usuario 3 | C-02 | Usuario 3 paths | owner decision note + interaction/validation experiment | T+45 | blocked |
| U1-B | Deliver inventory plus adaptive RAG/storage/index/query outcome and bounded runtime boundary | Usuario 1 | U1-R | Usuario 1 paths | deterministic query boundary smoke | T+100 | blocked |
| U2-B | Deliver normalized semantic package with grounded entities/relationships | Usuario 2 | U2-R | Usuario 2 paths | representative corpus check | T+100 | blocked |
| U3-B | Deliver validation gate and web intake/query/trust experience | Usuario 3 | U3-R | Usuario 3 paths | validation fixture + production build | T+100 | blocked |
| V-01 | Sequentially integrate semantic processing, adaptive RAG/runtime, then web/validation | Usuario 1 | U1-B, U2-B, U3-B | coordinator integration paths | boundary check after each merge | T+125 | blocked |
| T-01 | Prove real provider/tool/result and honest failure cases | Usuario 1 with owner evidence | V-01 | validation artifacts via Usuario 1 | normal, missing, contradictory, tool-failure cases | T+150 | blocked |
| D-01 | Freeze, rehearse twice, and capture backup | team | T-01 | demo artifacts via Usuario 1 | exact journey passes twice | T+185 | blocked |
