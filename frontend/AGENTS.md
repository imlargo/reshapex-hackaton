## Project Configuration

- **Language**: TypeScript
- **Package Manager**: npm
- **Add-ons**: prettier, eslint, vitest, tailwindcss, sveltekit-adapter, mcp

---

You are able to use the Svelte MCP server, where you have access to comprehensive Svelte 5 and SvelteKit documentation. Here's how to use the available tools effectively:

## Available Svelte MCP Tools:

### 1. list-sections

Use this FIRST to discover all available documentation sections. Returns a structured list with titles, use_cases, and paths.
When asked about Svelte or SvelteKit topics, ALWAYS use this tool at the start of the chat to find relevant sections.

### 2. get-documentation

Retrieves full documentation content for specific sections. Accepts single or multiple sections.
After calling the list-sections tool, you MUST analyze the returned documentation sections (especially the use_cases field) and then use the get-documentation tool to fetch ALL documentation sections that are relevant for the user's task.

### 3. svelte-autofixer

Analyzes Svelte code and returns issues and suggestions.
You MUST use this tool whenever writing Svelte code before sending it to the user. Keep calling it until no issues or suggestions are returned.

### 4. playground-link

Generates a Svelte Playground link with the provided code.
After completing the code, ask the user if they want a playground link. Only call this tool after user confirmation and NEVER if code was written to files in their project.

# AGENTS.md

Guía operativa para agentes de IA trabajando en este proyecto. Estas reglas son obligatorias.

## Documentación de arquitectura

- En `docs/ARCHITECTURE.md` **siempre** existe documentación de arquitectura del proyecto.
- Consultarla como referencia **solo cuando sea necesario** (decisiones estructurales, dudas sobre patrones, features nuevas que toquen varias capas).
- Su contenido **varía entre proyectos**: cada proyecto tiene su propia arquitectura y reglas específicas. Nunca asumir; siempre verificar ahí.

## Proceso de trabajo

- Antes de escribir código: explorar el repo, entender estructura de carpetas, convenciones existentes y código relacionado con la tarea.
- Buscar implementaciones similares ya existentes y seguir el mismo patrón antes de inventar uno nuevo.
- Priorizar simplicidad y patrones ya establecidos por sobre soluciones rápidas o código "por cumplir".
- Ante ambigüedad entre dos enfoques válidos, elegir el que ya predomina en el codebase.
- No introducir dependencias nuevas sin necesidad clara; verificar primero si algo existente resuelve el problema.

## UI / Estilos

- **Tailwind siempre.** CSS custom solo si es estrictamente imposible con utilidades de Tailwind.
- **shadcn primero:** si existe un componente de shadcn aplicable (button, input, dialog, select, etc.), usarlo **en su forma pura**: sin modificar el componente ni agregar clases extra, salvo necesidad estricta. Preservar el estilo base de shadcn.
- `components/ui/` (shadcn) es **intocable** bajo cualquier circunstancia. No editar, no extender, no borrar archivos ahí.
- Componer variantes por fuera (wrappers, props, composición), nunca modificando la fuente de shadcn.

## Arquitectura / Código

- **Services** son los únicos responsables de llamadas a APIs. Nada de `fetch`/HTTP directo en componentes, stores o composables.
- Usar siempre los **tipos genéricos ya definidos** para respuestas paginadas y estructuras comunes de respuesta. No redefinir estos tipos localmente.
- **Prohibido magic strings:** usar enums (o constantes tipadas ya definidas) para valores fijos, keys, rutas de API, estados, etc.
- **Composición sobre herencia** (y sobre cualquier alternativa): componentes pequeños y componibles, funciones/composables reutilizables y combinables. Evitar jerarquías rígidas, componentes monolíticos y abstracciones acopladas.

## Tipos

- **Nunca usar `any`**, sin excepciones (tampoco `as any` para esquivar un error de tipos). Si el tipo real es complejo o viene de una respuesta externa, investigar la fuente (endpoint, store o composable relacionado, tipos ya definidos en `types/`) y tipar explícitamente. Si de verdad se desconoce la forma en tiempo de escritura, usar `unknown` y angostar el tipo antes de operar sobre él — nunca `any` como atajo.
- **Prohibido declarar conjuntos cerrados de valores como union types de strings sueltos** (ej. `type SubcategoryType = 'legal_and_studies' | 'construction_license' | 'validation'`). Declararlos como `enum`:

    ```typescript
    export enum Subcategory {
        LEGAL_AND_STUDIES = 'legal_and_studies',
        CONSTRUCTION_LICENSE = 'construction_license',
        VALIDATION = 'validation'
    }
    ```

- **Antes de crear un tipo o enum nuevo, buscar en `types/` (y en el store/composable relacionado) si ya existe uno equivalente.** Si aparece algo parecido pero no idéntico, verificar con cuidado si de verdad son el mismo concepto de dominio antes de reutilizarlo o fusionarlo — no unificar dos conceptos distintos solo porque comparten algunos valores.
- Si no existe un tipo adecuado, crearlo en `types/` (nunca inline ni duplicado en el archivo que lo consume) y reexportarlo desde donde se necesite.

## Estado

- **Stores = solo estado global compartido.** Implementarlos con **clases**, usando las herramientas nativas del framework (stores de Svelte, o composables/provide-inject en Nuxt/Vue, según el proyecto).
- **Antes de crear un store, evaluar si el estado realmente necesita ser global.** Si es local a una feature o pantalla, usar composables que orquesten la lógica; no crear stores globales innecesarios.
- Los stores no llaman APIs directamente: delegan en services.

## Convenciones de código

- Seguir el naming y la estructura de carpetas existentes en el repo (verificar antes de crear archivos).
- Mantener componentes enfocados: si un componente crece en responsabilidades, extraer subcomponentes o composables.
- La lógica reutilizable vive en composables, no duplicada en componentes.
- **Si una función es probable que se use en más de un componente, no dejarla inline dentro del componente.** Extraerla a la carpeta compartida que corresponda: `utils/` para funciones puras sin estado (formateo, validación, transformación de datos), `composables/` para lógica con estado/reactividad. Antes de crear una nueva, revisar si ya existe algo equivalente ahí.
- NO dejar código muerto, comentarios de debug ni `console.log` en el código final.
- Los cambios deben ser mínimos y acotados a la tarea: NO refactorizar código no relacionado sin que se pida.
