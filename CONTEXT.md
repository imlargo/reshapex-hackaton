# CONTEXT.md

Leer antes de tocar código. Esto no cambia durante el sprint; `PLAN.md` (si existe) sí.

## Qué es esto

AgentSprint by ReshapeX — hackathon de agentes de IA, Universidad EAFIT, 25 jul 2026,
equipos de 3-4, ~3.5 horas de build. Marca elegida: **SICK** (sensores y seguridad
industrial). El agente final es el ingeniero de aplicaciones que no se va a dormir:
dado un producto SICK por type code, responde specs y precio con citación verificable
a una fuente real — nunca de memoria —, explica en qué se diferencia de un producto
similar, para qué tipo de aplicación es, y qué recomienda dadas unas restricciones,
mostrando también lo descartado y su motivo. Encima de eso, una auditoría de
seguridad: dada una lista de dispositivos instalados en una celda, detecta problemas
que nadie preguntó — nivel de PL/SIL insuficiente, distancia de montaje que no cumple
ISO 13855, dispositivos que superaron su vida útil de misión. Regla que nunca se
negocia: cuando dos fuentes discrepan (ficha del fabricante vs. listado de
distribuidor), el sistema **nunca** elige un valor — lo marca como conflicto, baja la
confianza y escala a un humano. Toda respuesta con confianza bajo el umbral se retiene
para revisión en vez de enviarse.

## Las dos capas — no confundirlas

**Capa 2 — `knowledge/` — la base de conocimiento y su agente de consulta.**
Un pipeline batch (offline, se corre con `uv run build-layer`) que ingiere archivos,
páginas y APIs en fases explícitas — ingest, parse, extract, normalize, reconcile,
validate, publish — y produce `data/layer.json`: hechos tipados con procedencia,
confianza y estado (`verified` / `conflict` / `unreviewed`). Sobre ese archivo vive un
**agente de consulta** (`knowledge/query_agent.py`) que resuelve entidades ambiguas y
responde qué hechos son relevantes a una pregunta. Es la única puerta de entrada a la
capa: nadie fuera de `knowledge/` toca `layer.json` ni `store.py` directamente.

**Capa 1 — `expert/` — el agente SICK que habla con el usuario.**
Sus tools (`get_specs`, `compare_products`, `find_products`, `escalate_to_human`)
llaman al agente de consulta de capa 2 como si fuera una tool más — nunca leen el
JSON ni implementan lógica de búsqueda propia. Este es el agente que responde las tres
preguntas obligatorias del reto y el que se conecta a la interfaz final.

Regla dura: **capa 1 nunca importa nada de `knowledge/pipeline/`.** Si necesita un dato
que la capa no tiene, la respuesta correcta es "no lo sé, escalo" — nunca inventar ni
ir a buscarlo por su cuenta.

## Stack y arquitectura de carpetas

Python 3.12 + `uv` (nunca `pip` suelto) + FastAPI + `pydantic-ai`. Modelo configurable
vía `MODEL=proveedor:modelo` en `.env`. Frontend probablemente SvelteKit, todo corriendo
en local sobre Node — sin desplegar nada.

```
src/sick_agent/
├─ knowledge/              CAPA 2
│  ├─ models.py            Fact, Provenance, FactStatus, KnowledgeLayer
│  ├─ pipeline/             fases 1-7, cada una función pura: list[X] -> list[Y]
│  ├─ store.py              fase 8: carga layer.json, funciones deterministas
│  ├─ query_agent.py        el agente de consulta
│  └─ build.py              orquesta 1->7, entrypoint `uv run build-layer`
├─ expert/                 CAPA 1
│  ├─ core.py               Agent + tools, cada tool llama al query_agent
│  ├─ confidence.py         puerta de confianza
│  └─ prompt.py             voz de marca + reglas duras
├─ agent/trace.py          eventos estructurados, compartido por los dos agentes
├─ api/routes.py           HTTP. Cero lógica de dominio aquí.
└─ cli.py                  REPL — aquí se itera el 80% del tiempo
```

`knowledge/` no importa nada de `expert/` ni de FastAPI. `expert/` no importa nada de
`knowledge/pipeline/` ni de FastAPI. Solo `api/` sabe que existe HTTP. Verificable con
`grep -r "fastapi" src/sick_agent/knowledge src/sick_agent/expert` → debe salir vacío.

## Reglas no negociables (se evalúan directamente)

- **Nada mockeado.** Dato hardcodeado que aparenta ser real = falla de Code Quality.
  Si algo no está listo, un `TODO` explícito y una función que lanza error — nunca un
  `return` que simula funcionar.
- **Toda afirmación factual sale de una tool, con cita.** Nunca de memoria del modelo.
- **Fallo esperado → dato, no excepción.** `ModelRetry` o `{ok: False, reason}`, nunca
  un `raise` que mate el loop del agente.
- **Un hecho en conflicto nunca se afirma.** Se dice que las fuentes discrepan y se
  escala — no se promedia, no se elige el más probable.
- **`.env` en `.gitignore` desde el primer commit.** Ninguna clave real versionada.
- **Commits pequeños y frecuentes**, no uno gigante al final.

## Antes de escribir código

1. Verificar la API contra su documentación oficial, no contra la memoria —
   `pydantic-ai` y el ecosistema de agentes cambian rápido.
2. Revisar si `knowledge/models.py` ya define lo que se necesita antes de crear un
   tipo nuevo.
3. Si la tarea es en `expert/`, confirmar primero que existe un `query_agent`
   (real o con datos fijos) contra el cual programar — no bloquearse esperando el
   pipeline completo.