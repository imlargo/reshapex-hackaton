# Merge Order

Usuario 1 alone merges, resolves shared glue, and proves the integrated
end-to-end journey.

| Order | Branch/commit | Dependency reason | Boundary check after merge | Status |
| ---: | --- | --- | --- | --- |
| 1 | `codex/semantic-processing` | Establishes the normalized semantic package behind its frozen boundary | representative corpus check plus package schema validation | pending |
| 2 | `codex/adaptive-rag` | Connects inventory, selected RAG/storage/index strategy, query runtime, and semantic package | RAG decision evidence plus deterministic model/tool/query smoke | pending |
| 3 | `codex/web-validation` | Replaces fixtures with validation and the integrated web boundary | validation gate, production build, primary journey, honest error state | pending |

Workers hand off commits and evidence but never merge their own branch.
