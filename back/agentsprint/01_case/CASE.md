# Normalized Case

## One-sentence value hypothesis

Our agent helps a SICK knowledge owner turn supplied mixed documentation into a
queryable, cited knowledge base by profiling the corpus, proposing and applying
the right cleaning, chunking, relationship, retrieval, and storage strategy.

## Pain today

- User: a SICK knowledge owner or technical specialist; exact role remains to
  be confirmed.
- Current workflow: assumed manual inspection and preparation of heterogeneous
  sources before they can support reliable search or question answering.
- Cost/delay/risk: unknown until the team interviews the user; do not present a
  number in the pitch without a source.
- Exact demo input: a small supplied corpus plus a one-sentence knowledge-base
  objective. The existing starter accepts text, Markdown, CSV, and JSON; Person
  2 has authority to revise format support after inspecting the real corpus.
- Judge-visible output: corpus profile, transformation plan, relation taxonomy,
  storage recommendation, build-quality report, and a cited answer from the
  generated knowledge base.

## Obvious alternative

- "Chat with documents" would chunk every file the same way and expose a chat
  box over one fixed index.
- Our meaningful difference: a **knowledge-base compiler** that first inspects
  the evidence, then produces an explainable build plan and typed provenance
  before answering. It can decline unsupported relations and recommend a
  different storage topology when the source shape warrants it.

## Organizer facts

- The target company is SICK.
- The requested product is an agent that generates RAG-style knowledge bases
  from supplied information.
- The supplied flow is: information supplied → inventory and classification →
  specialized extraction → normalization → entity and relationship detection →
  automatic storage design → indexing → validation → knowledge base ready for
  queries.
- The team has three participants.
- One participant will own a web-stack visual experience and should receive one
  additional compatible responsibility.
- Usuario 1 owns the research, selection, and implementation boundary for the
  RAG types the agent may use.
- Each owner must have authority to investigate and choose the best approach
  for the challenges discovered in their part of the flow.

## Team assumptions

- The first vertical slice needs a bounded sample corpus and a reproducible
  knowledge package; the responsible owners select their internal methods.
- A web frontend can progress against frozen JSON examples while Streamlit
  remains a demo fallback. Owner: Usuario 3; validate with a contract test.
- Domain-specific SICK entities and relations must be derived from supplied
  sources, not invented from general knowledge. Owner: Usuario 2.
