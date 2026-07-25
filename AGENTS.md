# AGENTS.md

Guía operativa para agentes de IA trabajando en este proyecto. Estas reglas son obligatorias.

## Proceso de trabajo

- Antes de escribir código: explorar el repo, entender estructura de carpetas, convenciones existentes y código relacionado con la tarea.
- Buscar implementaciones similares ya existentes y seguir el mismo patrón antes de inventar uno nuevo.
- Priorizar simplicidad y patrones ya establecidos por sobre soluciones rápidas o código "por cumplir".
- Ante ambigüedad entre dos enfoques válidos, elegir el que ya predomina en el codebase. Si ninguno predomina, la primera implementación que se mergee fija el patrón: no abrir un segundo estilo en paralelo.
- **Preferir la solución simple que se entiende a la elegante que hay que estudiar.** Si el código no se puede explicar en voz alta en treinta segundos, es demasiado listo.
- No introducir dependencias nuevas sin necesidad clara; verificar primero si algo existente resuelve el problema.
- Los cambios deben ser mínimos y acotados a la tarea: NO refactorizar código no relacionado sin que se pida.

## Integridad de la implementación

- **Prohibido mockear.** Nada de datos hardcodeados que simulen una respuesta real, `return { fake: true }`, ni implementaciones vacías que aparenten funcionar. Si algo no se puede implementar de verdad todavía, dejar un `TODO` explícito y una función que lance error con mensaje claro. Un stub honesto es aceptable; un mock silencioso no.
- **Nunca versionar secretos.** `.env` en `.gitignore`. Ninguna clave real en código, ejemplos, comentarios ni fixtures.
- **Commits pequeños, frecuentes y con mensaje descriptivo.** Un commit por unidad de trabajo coherente. Nada de commits masivos que mezclen features, refactors y formato.

## Arquitectura / Código

- **Services** son los únicos responsables de llamadas a APIs. Nada de `fetch`/HTTP directo en componentes, stores o composables.
- **El navegador nunca habla con proveedores externos.** Toda llamada a un modelo o servicio con credenciales es server-side; el cliente solo consume rutas propias. Una clave en el bundle es un fallo, no un atajo.
- **El núcleo de dominio no depende del framework.** El código de negocio usa solo imports relativos y `process.env`: nada de `$lib`, `$env`, `$app` ni equivalentes. Debe poder ejecutarse desde una ruta HTTP, un CLI o un script sin cambiar una línea.
- Usar siempre los **tipos genéricos ya definidos** para respuestas paginadas y estructuras comunes de respuesta. No redefinir estos tipos localmente.
- **Prohibido magic strings:** usar enums (o constantes tipadas ya definidas) para valores fijos, keys, rutas de API, estados, etc.
- **Composición sobre herencia** (y sobre cualquier alternativa): componentes pequeños y componibles, funciones/composables reutilizables y combinables. Evitar jerarquías rígidas, componentes monolíticos y abstracciones acopladas.

## Tools de agente

- La `description` de una tool es un prompt, no documentación: describir la **condición de disparo** ("úsala cuando…") y, si hay tools parecidas, cuándo **no** usarla.
- **Los fallos esperados se devuelven como datos, no como excepciones.** "Sin resultados", "entrada ambigua", "fuera de rango" → `{ ok: false, reason }`. Lanzar excepción solo cuando el sistema está roto de verdad (credencial inválida, dependencia caída). Una excepción corta el loop del agente; un objeto estructurado le permite recuperarse.
- Devolver siempre datos estructurados con IDs estables, nunca prosa.
- Acotar el tamaño de la respuesta: seleccionar campos, paginar, y reportar el total real cuando se trunca.

## Tipos

- **Nunca usar `any`**, sin excepciones (tampoco `as any` para esquivar un error de tipos). Si el tipo real es complejo o viene de una respuesta externa, investigar la fuente (endpoint, store o composable relacionado, tipos ya definidos en `types/`) y tipar explícitamente. Si de verdad se desconoce la forma en tiempo de escritura, usar `unknown` y angostar el tipo antes de operar sobre él — nunca `any` como atajo.
- Las uniones discriminadas se angostan por su discriminante (`if (res.ok)`), nunca casteando.
- **Prohibido declarar conjuntos cerrados de valores como union types de strings sueltos** (ej. `type SubcategoryType = 'legal_and_studies' | 'construction_license' | 'validation'`). Declararlos como `enum`:

    ```typescript
    export enum Subcategory {
        LEGAL_AND_STUDIES = 'legal_and_studies',
        CONSTRUCTION_LICENSE = 'construction_license',
        VALIDATION = 'validation'
    }
    ```

- **Excepción: los schemas de validación de entrada de tools.** `z.enum([...])` produce una union y así debe quedar — es lo que se convierte en JSON Schema para el modelo. No sustituirlo por un `enum` de TypeScript dentro de un `inputSchema`. Si el conjunto también se usa en el dominio, declarar el `enum` y derivar el schema de él, no duplicar los valores.
- **Antes de crear un tipo o enum nuevo, buscar en `types/` (y en el store/composable relacionado) si ya existe uno equivalente.** Si aparece algo parecido pero no idéntico, verificar con cuidado si de verdad son el mismo concepto de dominio antes de reutilizarlo o fusionarlo — no unificar dos conceptos distintos solo porque comparten algunos valores.
- Si no existe un tipo adecuado, crearlo en `types/` (nunca inline ni duplicado en el archivo que lo consume) y reexportarlo desde donde se necesite.

## UI / Estilos

- **Tailwind siempre.** CSS custom solo si es estrictamente imposible con utilidades de Tailwind.
- **shadcn primero:** si existe un componente de shadcn aplicable (button, input, dialog, select, etc.), usarlo **en su forma pura**: sin modificar el componente ni agregar clases extra, salvo necesidad estricta. Preservar el estilo base de shadcn.
- `components/ui/` (shadcn) es **intocable** bajo cualquier circunstancia. No editar, no extender, no borrar archivos ahí.
- Componer variantes por fuera (wrappers, props, composición), nunca modificando la fuente de shadcn.

## Estado

- **Stores = solo estado global compartido.** Implementarlos con **clases**, usando las herramientas nativas del framework (runes/stores de Svelte, o composables/provide-inject en Vue, según el proyecto).
- **Antes de crear un store, evaluar si el estado realmente necesita ser global.** Si es local a una feature o pantalla, usar composables o estado local del componente; no crear stores globales innecesarios.
- Los stores no llaman APIs directamente: delegan en services.

## Convenciones de código

- Seguir el naming y la estructura de carpetas existentes en el repo (verificar antes de crear archivos).
- Mantener componentes enfocados: si un componente crece en responsabilidades, extraer subcomponentes o composables.
- La lógica reutilizable vive en composables, no duplicada en componentes.
- **Si una función es probable que se use en más de un componente, no dejarla inline dentro del componente.** Extraerla a la carpeta compartida que corresponda: `utils/` para funciones puras sin estado (formateo, validación, transformación de datos), `composables/` para lógica con estado/reactividad. Antes de crear una nueva, revisar si ya existe algo equivalente ahí.
- **Nada de `console.log` en el código final.** Los eventos que importan van por el logger estructurado del proyecto, con tipo, etiqueta y datos. Un `console.log` es información que se pierde; un evento estructurado es información que se puede consultar.
- NO dejar código muerto ni comentarios de debug.
- Los comentarios explican **por qué**, no qué. Documentar decisiones de diseño, no describir la línea siguiente.

## APIs y dependencias

- **Verificar la API contra su documentación oficial antes de usarla, no contra la memoria.** Las librerías del ecosistema de IA rompen compatibilidad seguido; una firma recordada de una versión anterior compila mal o falla en runtime.
- Puntos concretos donde la memoria suele estar desactualizada (verificados al 25/07/2026):
    - `ai@^7`: la clase es **`ToolLoopAgent`**, no `Agent`.
    - `generateObject` está **deprecado** → `generateText` con `output: Output.object({ schema })`.
    - `stepCountIs` es alias de `isStepCount`.
    - `@ai-sdk/svelte@^5` depende de `ai@7.0.37` exacto; peer `svelte@^5.31`.
    - Svelte 5 usa runes (`$state`, `$props`, `$derived`); en el cliente se renderiza `message.parts`, no `message.content`.
- Ante cualquier duda de API, la documentación oficial gana sobre cualquier tutorial o ejemplo previo.