# Facts and Constraints

## Organizer facts

- Company: SICK.
- Requested capability: generate an evidence-grounded RAG-style knowledge base
  whose pipeline adapts to the supplied information.
- Team size: three people.
- One teammate is assigned to a web-stack visual experience.
- Usuario 1 is assigned the RAG strategy capability.
- The required flow has nine ordered stages from supplied information through
  validation to a query-ready knowledge base.

## Available evidence and integrations

- `SRC-001` contains only the user brief.
- The repository already contains a bounded LangChain/LangGraph/DeepSeek
  starter with typed evidence tools and a Streamlit fallback.
- No SICK documents, APIs, credentials, official links, or brand assets have
  been supplied.

## Hard constraints

- Build clock: 210 minutes unless organizer material says otherwise.
- Feature freeze target: T+150.
- Material claims require knowledge-tool evidence.
- Raw inputs are append-only and derived artifacts must retain stable source
  IDs.
- Shared schemas, dependency manifests, routing, and integration glue have one
  writer: the coordinator.
- No branch may invent a SICK-specific entity, relationship, product fact, or
  brand treatment.

## Team assumptions

- The existing intake supports `.txt`, `.md`, `.csv`, and `.json`; Usuario 2
  decides whether to preserve, expand, or replace that support after corpus
  research.
- RAG strategy, storage design, indexing, and retrieval technology are
  delegated to Usuario 1. The decision must be evidence-based, reproducible for
  the demo, and compatible with the shared build-result boundary.
- Person labels will be replaced with team member names before branches are
  pushed.
