from __future__ import annotations

from .models import DemoCase, SourceEvidence

DEMO_CASES: tuple[DemoCase, ...] = (
    DemoCase(
        case_id="lidar-support",
        short_name="Soporte LiDAR",
        title="De documentación dispersa a una respuesta operativa",
        eyebrow="CASO 01 · BÚSQUEDA SEMÁNTICA",
        objective=(
            "Responder preguntas de integración LiDAR en lenguaje natural, "
            "con pasos concretos y evidencia rastreable."
        ),
        question=(
            "¿Cuándo debo usar Challenge-Response, un Session Token o "
            "WebSocket para comunicarme con el dispositivo?"
        ),
        description=(
            "El objetivo prioriza significado y recuperación de pasajes entre "
            "artículos técnicos heterogéneos."
        ),
        expected_storage="vector",
        selection_reason=(
            "La consulta combina conceptos expresados en documentos distintos y no "
            "requiere filtros exactos ni recorridos de relaciones. Un índice vectorial "
            "local ofrece el camino más corto hacia pasajes relevantes y citables."
        ),
        documents=[
            "KA-10741 · LiDAR authentication",
            "KA-10726 · WebSocket Event API",
            "KA-09665 · REST API integration",
        ],
        document_count=3,
        simulated_chunks=2,
        simulated_entities=6,
        simulated_relations=0,
        answer=(
            "Usa Challenge-Response para escribir variables JSON. Obtén un Session "
            "Token cuando vayas a transferir archivos binarios. Para eventos en tiempo "
            "real, suscríbete a /apievents por WebSocket en lugar de consultar "
            "periódicamente la REST API."
        ),
        caveat=(
            "La demo no prueba conectividad con un equipo físico ni valida una versión "
            "concreta de firmware."
        ),
        evidence=[
            SourceEvidence(
                evidence_id="EVID-KA10741-01",
                source_id="SRC-005 / KA-10741",
                title="LiDAR: Challenge & Response and Session Token Authentication",
                location="Overview and authentication comparison",
                excerpt=(
                    "Writing a JSON variable uses Challenge-Response; binary file "
                    "transfers require a short-lived session token in the HTTP header."
                ),
                url=(
                    "https://support.sick.com/sick-knowledgebase/article/"
                    "?code=KA-10741"
                ),
                supports="Elección entre Challenge-Response y Session Token.",
            ),
            SourceEvidence(
                evidence_id="EVID-KA10726-01",
                source_id="SRC-005 / KA-10726",
                title="WebSocket Event API (/apievents)",
                location="Overview",
                excerpt=(
                    "The device exposes real-time events through a persistent WebSocket "
                    "connection; subscriptions avoid polling the REST API."
                ),
                url=(
                    "https://support.sick.com/sick-knowledgebase/article/"
                    "?code=KA-10726"
                ),
                supports="Uso de WebSocket para eventos push.",
            ),
        ],
        artifact_rows=[
            {
                "rank": "1",
                "evidence": "KA-10741",
                "match": "96%",
                "reason": "Autenticación y tokens",
            },
            {
                "rank": "2",
                "evidence": "KA-10726",
                "match": "91%",
                "reason": "Eventos WebSocket",
            },
            {
                "rank": "3",
                "evidence": "KA-09665",
                "match": "78%",
                "reason": "Contexto REST",
            },
        ],
    ),
    DemoCase(
        case_id="rfh5xx-integration",
        short_name="Compatibilidad RFH5xx",
        title="De productos y protocolos a una ruta de integración",
        eyebrow="CASO 02 · GRAFO SIMPLE",
        objective=(
            "Encontrar la relación y la ruta verificable entre equipos, protocolos, "
            "herramientas y recursos de integración para PLC."
        ),
        question=(
            "¿Cómo se conecta RFH5xx con SIG200 y qué recursos existen para "
            "integrarlo con distintos PLC?"
        ),
        description=(
            "La pregunta pide relaciones directas entre entidades conocidas; un recorrido "
            "acotado es más explicable que similitud de texto."
        ),
        expected_storage="simple_graph",
        selection_reason=(
            "El valor está en las conexiones RFH5xx → SIG200 → REST API y "
            "RFH5xx → bloques de función → plataformas PLC. Son relaciones directas de "
            "uno o dos saltos; no hay evidencia que justifique un grafo complejo."
        ),
        documents=[
            "KA-08582 · RFH5xx with SIG200 REST API",
            "KA-09345 · IO-Link Function Blocks",
            "IM0084724 · SIG200 REST API instructions",
        ],
        document_count=3,
        simulated_chunks=2,
        simulated_entities=8,
        simulated_relations=7,
        answer=(
            "RFH5xx puede utilizarse con SIG200 y controlarse mediante la REST API de "
            "SIG200; el artículo incluye una colección de comandos para Insomnia. Para "
            "integración PLC hay bloques de función descargables para Siemens TIA, Omron "
            "Sysmac Studio, Rockwell Studio 5000 y Mitsubishi GX Works3."
        ),
        caveat=(
            "La relación indica disponibilidad documental; la demo no certifica "
            "compatibilidad para una referencia de hardware o versión concreta."
        ),
        evidence=[
            SourceEvidence(
                evidence_id="EVID-KA08582-01",
                source_id="SRC-005 / KA-08582",
                title="AN: RFH5xx with SIG200 REST API",
                location="Application note summary",
                excerpt=(
                    "The application note uses RFH5xx in combination with SIG200 and "
                    "controls the device through the SIG200 REST API, with Insomnia examples."
                ),
                url=(
                    "https://support.sick.com/sick-knowledgebase/article/"
                    "?code=KA-08582"
                ),
                supports="Ruta RFH5xx → SIG200 → REST API.",
            ),
            SourceEvidence(
                evidence_id="EVID-KA09345-01",
                source_id="SRC-005 / KA-09345",
                title="RFH5xx / RFU610 IO-Link / CLV61x IO-Link: Function Blocks",
                location="RFH5xx function-block table",
                excerpt=(
                    "RFH5xx function blocks are listed for Siemens TIA, Omron Sysmac "
                    "Studio, Rockwell Studio 5000 and Mitsubishi GX Works3."
                ),
                url=(
                    "https://support.sick.com/sick-knowledgebase/article/"
                    "?code=KA-09345"
                ),
                supports="Plataformas PLC con recursos descargables.",
            ),
        ],
        artifact_rows=[
            {
                "source": "RFH5xx",
                "relation": "se controla mediante",
                "target": "SIG200 REST API",
            },
            {
                "source": "RFH5xx",
                "relation": "tiene bloque para",
                "target": "Siemens TIA",
            },
            {
                "source": "RFH5xx",
                "relation": "tiene bloque para",
                "target": "Omron · Rockwell · Mitsubishi",
            },
        ],
    ),
    DemoCase(
        case_id="repository-inventory",
        short_name="Inventario GitHub",
        title="De metadatos técnicos a un inventario consultable",
        eyebrow="CASO 03 · BASE RELACIONAL",
        objective=(
            "Filtrar repositorios por lenguaje, tipo de driver, familia de producto y "
            "fecha de actualización."
        ),
        question=(
            "¿Qué repositorios C++ del corpus apoyan scanners de seguridad o "
            "sensores de guiado de línea?"
        ),
        description=(
            "Los campos son estables y la consulta exige filtros exactos; una tabla local "
            "es suficiente y verificable."
        ),
        expected_storage="relational",
        selection_reason=(
            "Nombre, lenguaje, descripción y fecha ya tienen forma tabular. Los filtros "
            "exactos dominan sobre la similitud semántica, por lo que un índice relacional "
            "local evita complejidad y produce resultados reproducibles."
        ),
        documents=["SICKAG_repositories.json · 57 repository records"],
        document_count=1,
        simulated_chunks=3,
        simulated_entities=0,
        simulated_relations=0,
        answer=(
            "El filtro devuelve sick_safetyscanners y sick_safetyscanners_base para "
            "scanners láser de seguridad, además de sick_line_guidance para los sensores "
            "OLS10, OLS20 y MLS sobre CANopen. Los tres registros declaran C++."
        ),
        caveat=(
            "El resultado refleja el snapshot local del corpus; no consulta el estado "
            "actual de GitHub."
        ),
        evidence=[
            SourceEvidence(
                evidence_id="EVID-GH-SAFETY-01",
                source_id="SRC-006 / SICKAG_repositories.json",
                title="sick_safetyscanners",
                location="repository record",
                excerpt="ROS driver for SICK safety laser scanners · language: C++.",
                url="https://github.com/SICKAG/sick_safetyscanners",
                supports="Driver C++ para scanners láser de seguridad.",
            ),
            SourceEvidence(
                evidence_id="EVID-GH-SAFETYBASE-01",
                source_id="SRC-006 / SICKAG_repositories.json",
                title="sick_safetyscanners_base",
                location="repository record",
                excerpt="CPP (C++) Driver for SICK safety laser scanners.",
                url="https://github.com/SICKAG/sick_safetyscanners_base",
                supports="Segundo driver C++ de scanners de seguridad.",
            ),
            SourceEvidence(
                evidence_id="EVID-GH-LINE-01",
                source_id="SRC-006 / SICKAG_repositories.json",
                title="sick_line_guidance",
                location="repository record",
                excerpt=(
                    "ROS support for OLS10, OLS20 and MLS line-guidance sensors "
                    "using a CANopen interface · language: C++."
                ),
                url="https://github.com/SICKAG/sick_line_guidance",
                supports="Proyecto C++ para sensores de guiado de línea.",
            ),
        ],
        artifact_rows=[
            {
                "repositorio": "sick_safetyscanners",
                "lenguaje": "C++",
                "tipo": "ROS driver · safety scanners",
            },
            {
                "repositorio": "sick_safetyscanners_base",
                "lenguaje": "C++",
                "tipo": "Base driver · safety scanners",
            },
            {
                "repositorio": "sick_line_guidance",
                "lenguaje": "C++",
                "tipo": "ROS · OLS10/OLS20/MLS · CANopen",
            },
        ],
    ),
    DemoCase(
        case_id="nova-impact",
        short_name="Impacto Nova 2.10",
        title="De una actualización a sus rutas de impacto",
        eyebrow="CASO 04 · GRAFO COMPLEJO",
        objective=(
            "Evaluar la ruta de impacto multi-salto de una actualización de SICK Nova "
            "sobre herramientas, familias de dispositivos y documentación relacionada."
        ),
        question=(
            "Si adoptamos Nova 2.10.0 y mantenemos herramientas personalizadas, "
            "¿qué rutas de dependencia debemos revisar antes del cambio?"
        ),
        description=(
            "Este caso fuerza relaciones densas, ciclos de compatibilidad y varios "
            "saltos; es el único que supera el gate del grafo complejo."
        ),
        expected_storage="complex_graph",
        selection_reason=(
            "La revisión conecta versión → herramientas Nova → familias de producto → "
            "firmware y vuelve a documentación de desarrollo. La densidad y los caminos "
            "multi-salto justifican un grafo ponderado; una BFS corta perdería rutas de "
            "impacto y un índice vectorial no preservaría dependencias."
        ),
        documents=[
            "KA-09640 · SICK Nova 2.10.0 release",
            "KA-09388 · SICK Nova releases",
            "KA-09513 · SICK Nova custom tool development",
            "Firmware release articles for related product families",
        ],
        document_count=4,
        simulated_chunks=3,
        simulated_entities=10,
        simulated_relations=15,
        answer=(
            "La ruta prioritaria simulada es Nova 2.10.0 → herramientas Nova → "
            "herramientas personalizadas → familias Inspector y Visionary-T Mini AP. "
            "Antes del cambio se deben contrastar las notas de firmware de cada familia "
            "y volver a validar las herramientas personalizadas contra la Nova Tool API."
        ),
        caveat=(
            "Las rutas son una simulación de análisis de impacto basada en relaciones "
            "visibles del corpus; no constituyen una matriz oficial de compatibilidad."
        ),
        evidence=[
            SourceEvidence(
                evidence_id="EVID-KA09640-01",
                source_id="SRC-005 / KA-09640",
                title="SICK Nova 2.10.0 release",
                location="Release summary, products and related articles",
                excerpt=(
                    "The release article names Nova tools and product families including "
                    "Visionary-T Mini AP, InspectorP63x, Inspector85x and Inspector83x; "
                    "it links related firmware and custom-tool articles."
                ),
                url=(
                    "https://support.sick.com/sick-knowledgebase/article/"
                    "?code=KA-09640"
                ),
                supports="Nodos de versión, herramientas, familias y artículos relacionados.",
            ),
            SourceEvidence(
                evidence_id="EVID-KA09513-01",
                source_id="SRC-005 / KA-09513",
                title="SICK Nova custom tool development",
                location="Article summary and product list",
                excerpt=(
                    "The article links the Nova Tool API, sample tools and tutorials for "
                    "building custom Nova tools, alongside supported product-family entries."
                ),
                url=(
                    "https://support.sick.com/sick-knowledgebase/article/"
                    "?code=KA-09513"
                ),
                supports="Ruta entre API, herramientas personalizadas y familias.",
            ),
            SourceEvidence(
                evidence_id="EVID-KA09388-01",
                source_id="SRC-005 / KA-09388",
                title="SICK Nova releases",
                location="Release hub summary and product list",
                excerpt=(
                    "The release hub links Nova release details and downloads for the Nova "
                    "API, Machine Vision Viewer, .NET SDK and Nova-related resources."
                ),
                url=(
                    "https://support.sick.com/sick-knowledgebase/article/"
                    "?code=KA-09388"
                ),
                supports="Hub que conecta versiones con herramientas y recursos.",
            ),
        ],
        artifact_rows=[
            {
                "path": "Nova 2.10.0 → Nova Tool API → custom tools",
                "weight": "0.94",
                "action": "Revalidar API y ejemplos",
            },
            {
                "path": "Nova 2.10.0 → Inspector families → firmware notes",
                "weight": "0.89",
                "action": "Contrastar versión por familia",
            },
            {
                "path": "Nova 2.10.0 → Visionary-T Mini AP → firmware",
                "weight": "0.84",
                "action": "Revisar compatibilidad declarada",
            },
        ],
    ),
)
