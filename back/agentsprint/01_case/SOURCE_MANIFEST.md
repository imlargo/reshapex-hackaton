# Source Manifest

Raw sources are immutable. Derived artifacts retain their source IDs.

| ID | Type | Origin/path | Relevance | Owner | Status | Confidentiality |
| --- | --- | --- | --- | --- | --- | --- |
| SRC-001 | user brief | Codex conversation, 2026-07-25 | Defines SICK, the nine-stage knowledge-base flow, the three-person team, the web owner, owner autonomy, and Usuario 1 ownership of RAG strategy | coordinator | received | team internal |
| SRC-002 | user clarification | Codex conversation, 2026-07-25 | Confirms objective-first document upload and a basic local database when selected as best fit | coordinator | received | team internal |
| SRC-003 | corpus manifest | `contents/MANIFEST.json`, commit `1e987e9` | Inventories the six-layer SICK research corpus and stable PDF identifiers | Usuario 2; consumed by Usuario 1 | received | public-source research; internal hackathon use |
| SRC-004 | SICK PDF corpus | `contents/pdfs/`, commit `1e987e9` | 25 product, operating, technical, overview, and safety documents used to profile document/storage needs | Usuario 2; consumed by Usuario 1 | received | public-source research; internal hackathon use |
| SRC-005 | SICK support corpus | `contents/knowledge_base/`, commit `1e987e9` | 19 HTML support articles plus KA identifiers and URLs | Usuario 2; consumed by Usuario 1 | received | public-source research; internal hackathon use |
| SRC-006 | SICK GitHub corpus | `contents/github/`, commit `1e987e9` | Repository inventory and representative technical documentation | Usuario 2; consumed by Usuario 1 | received | public-source research; internal hackathon use |
| SRC-007 | portal and URL research | `contents/portals/`, `contents/url_patterns/`, commit `1e987e9` | Portal layers and stable URL patterns relevant to source classification and provenance | Usuario 2; consumed by Usuario 1 | received | public-source research; internal hackathon use |

The committed `contents/` tree is treated as immutable source material. Its
machine-readable manifests retain file-level IDs and URLs. No DeepSeek
credential or organizer-only material has been received; never place a key in
this manifest or in the corpus.
