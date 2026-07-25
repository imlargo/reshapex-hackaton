# Primary Journey

Status: supplied flow frozen; confirm the real persona and corpus before
implementation.

```text
Información suministrada
  → Inventario y clasificación
  → Extracción especializada
  → Normalización
  → Detección de entidades y relaciones
  → Diseño automático del almacenamiento y estrategia RAG
  → Indexación
  → Validación
  → Base de conocimiento lista para consultas
```

## Ownership along the journey

| Stage | Accountable owner |
| --- | --- |
| Information supplied through the web experience | Usuario 3 |
| Inventory and classification | Usuario 1 |
| Specialized extraction | Usuario 2 |
| Normalization | Usuario 2 |
| Entity and relationship detection | Usuario 2 |
| RAG strategy and automatic storage design | Usuario 1 |
| Indexing and query/retrieval boundary | Usuario 1 |
| Knowledge-base validation | Usuario 3 |
| Query-ready user experience and readiness sign-off | Usuario 3; integrated by Usuario 1 |

The flow and cross-stage records are frozen; implementation methods are not.
Each owner researches and selects the strongest approach inside their authority.

## Two-minute judge path

- Starting screen: create a knowledge base from supplied SICK material.
- User action: provide a small corpus and its intended use.
- Visible behavior: stage progress, RAG/storage decision, quality status, and
  provenance appear without revealing hidden chain-of-thought.
- Result reveal: query-ready knowledge base followed by one cited answer or
  relationship view.
- Innovation sentence: "It does not just chat with documents; it determines and
  executes how this corpus should become a knowledge base."
- Trust sentence: "Every material result points back to supplied evidence, and
  the validation gate blocks unsupported knowledge."
