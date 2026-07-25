# Open Questions

Ask only questions that change the journey, architecture, grounding, ownership,
safety behavior, or kill condition.

| Priority | Question | Why it blocks | Owner | Deadline | Resolution |
| --- | --- | --- | --- | --- | --- |
| P0 | Which SICK role owns this knowledge base, and what decision/action is slow or risky today? | Final value story and acceptance criteria | team | before implementation | provisional: knowledge owner/technical specialist |
| P0 | Which exact files, languages, sizes, tables, scans, links, and credentials will the demo receive? | Parsers, retrieval design, storage choice, and demo reliability | team | before implementation | only `.txt`, `.md`, `.csv`, and `.json` are currently safe |
| P0 | Which grounded result proves value in under two minutes: a built KB, a cited answer, a relationship view, or all three? | Primary judge path | team | before implementation | provisional: build summary + cited answer + focused relation view |
| P1 | What would the current/obvious document-chat workflow do, and which failure matters most? | Differentiator and kill condition | team | T+20 | provisional differentiator: adaptive knowledge-base compiler |
| P1 | Which SICK sources, APIs, data policies, deployment targets, model credentials, and team skills are available? | Grounding, privacy, storage, and ownership | team | T+20 | DeepSeek key and SICK sources are not present in this checkout |
| P1 | Must data remain on-premise or within a named region? | Can eliminate managed vector/graph options | coordinator | before storage adapter selection | open |
| P1 | Which relationship questions must the demo answer? | Determines what Usuario 2 must extract and what RAG strategies Usuario 1 must evaluate | Usuarios 1 and 2 | before relation extraction | open |
