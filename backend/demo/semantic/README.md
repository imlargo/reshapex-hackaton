# Semantic Studio — demo conceptual local

Esta rama presenta un recorrido interactivo y reproducible de cómo funcionaría
el compilador de bases de conocimiento. No llama a DeepSeek, no provisiona una
base externa y no afirma que el procesamiento completo ya exista.

Sí ejecuta una simulación determinista y visible sobre casos preparados a
partir de `SRC-003`–`SRC-007`:

1. inventario de fuentes;
2. extracción y normalización simuladas;
3. comparación explicable entre almacenamiento vectorial, relacional, grafo
   simple y grafo complejo;
4. selección del algoritmo de búsqueda apropiado;
5. artefacto local consultable;
6. respuesta de agente con evidencia real y límites visibles.

## Ejecutar

```powershell
uv sync --locked
uv run streamlit run demo/semantic/app.py
```

Abrir la URL local indicada por Streamlit, elegir un caso y pulsar
`Ejecutar agente semántico`.

## Casos preparados

| Caso | Plan esperado | Algoritmo |
| --- | --- | --- |
| Soporte LiDAR | Vectorial | `tfidf_cosine` |
| Compatibilidad RFH5xx | Grafo simple | `breadth_first_search` |
| Inventario GitHub | Relacional | `sql_filter_bm25` |
| Impacto Nova 2.10 | Grafo complejo | `personalized_pagerank` |

Los paquetes semánticos de los cuatro casos son fixtures preparados. La
clasificación, selección, compuertas, índices y llamadas a `search_evidence`
sí usan la implementación real de `agentsprint_starter.rag`. Los IDs, títulos,
metadatos, enlaces y fragmentos de evidencia corresponden al corpus
comprometido en `codex/semantic-processing` en `1e987e9`.
