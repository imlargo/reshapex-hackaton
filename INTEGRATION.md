# Integración frontend ↔ backend (ReshapeX)

Monorepo con:

- `frontend/` — SvelteKit (Usuario 3)
- `backend/` — backend Python `agentsprint-starter` (`codex/semantic-processing`, tip `f3d76dd+`)
- `contents/` — corpus SICK compartido

## Arranque local

Terminal 1 — API de conocimiento (puerto 8001):

```bash
chmod +x scripts/run-knowledge-api.sh
cp backend/.env.example backend/.env   # configurar CLAUDE_API_KEY o LLM_API_KEY
./scripts/run-knowledge-api.sh
```

Terminal 2 — frontend (puerto 3000):

```bash
cd frontend
cp .env.example .env
npm install
npm run dev
```

Abrir `http://localhost:3000/knowledge/ingest` y ejecutar el pipeline.

## Contrato

El frontend llama rutas server-side propias:

| Ruta SvelteKit | Proxy a Python |
|----------------|----------------|
| `GET /api/knowledge/health` | `GET /api/health` |
| `POST /api/knowledge/build` | `POST /api/knowledge/build` |
| `POST /api/knowledge/query` | `POST /api/knowledge/query` |

Variables server-only en `frontend/.env`:

- `KNOWLEDGE_API_URL` — default `http://127.0.0.1:8001`
- `KNOWLEDGE_CORPUS_DIR` — default `contents` (dentro de `backend/`, 57 fuentes SICK)

## Rama

`integrate/backend-semantic-processing` — sincroniza `backend/` y conecta la UI de ingestión al servicio real.
