from __future__ import annotations

from agentsprint_starter.rag import (
    AdaptiveRagCompiler,
    ContentUnit,
    KnowledgeBaseRequest,
    KnowledgeEntity,
    KnowledgeRelationship,
    NormalizedKnowledgePackage,
    ProcessingReport,
    RagStrategyPlan,
    SourceDescriptor,
    SourceInventory,
    StorageTopology,
)

from .cases import DEMO_CASES
from .models import CandidatePlan, DemoCase, DemoOutcome, DemoStage, StorageMode

PLAN_LABELS: dict[StorageMode, str] = {
    "vector": "Vectorial",
    "relational": "Relacional",
    "simple_graph": "Grafo simple",
    "complex_graph": "Grafo complejo",
}


def list_cases() -> tuple[DemoCase, ...]:
    return DEMO_CASES


def get_case(case_id: str) -> DemoCase:
    for case in DEMO_CASES:
        if case.case_id == case_id:
            return case
    raise KeyError(f"Unknown demo case: {case_id}")


def simulate_case(case_id: str) -> DemoOutcome:
    case = get_case(case_id)
    compiler = AdaptiveRagCompiler()
    request = KnowledgeBaseRequest(objective=case.objective)
    uploads = [
        (
            f"{position:02d}_{evidence.evidence_id.casefold()}.md",
            f"{evidence.supports}\n\n{evidence.excerpt}".encode(),
        )
        for position, evidence in enumerate(case.evidence, start=1)
    ]
    inventory = compiler.inventory(request, uploads)
    package = _normalized_package(case, inventory.inventory_id, inventory.sources)
    compiled = compiler.compile(request, inventory, package)
    plan = compiled.plan
    actual_storage = plan.storage.topology.value
    if actual_storage != case.expected_storage:
        compiled.index.close()
        raise RuntimeError(
            f"Fixture {case.case_id} selected {actual_storage}, "
            f"expected {case.expected_storage}."
        )

    tool_result = compiled.tools.execute(
        "search_evidence",
        {"query": case.question, "limit": 6},
    )
    retrieved_ids = [
        evidence["evidence_id"] for evidence in tool_result.get("evidence", [])
    ]
    candidates = _candidate_plans(compiler, request, inventory, package, plan)
    selected = next(candidate for candidate in candidates if candidate.status == "selected")
    outcome = DemoOutcome(
        case=case,
        selected_plan=selected,
        candidates=candidates,
        stages=_stages(
            case=case,
            selected=selected,
            inventory_sources=len(inventory.sources),
            signals=plan.selection_signals.model_dump(mode="json"),
            index_location=plan.index.location,
            retrieved=len(retrieved_ids),
        ),
        confidence="alta" if retrieved_ids and plan.index.status == "ready" else "media",
        validation_status="APROBADO PARA DEMO",
        inventory_id=inventory.inventory_id,
        plan_id=plan.plan_id,
        index_id=plan.index.index_id,
        index_location=plan.index.location,
        decision_mode="automatic",
        selection_signals=plan.selection_signals.model_dump(mode="json"),
        retrieved_evidence_ids=retrieved_ids,
        plan_dump=plan.model_dump(mode="json"),
    )
    compiled.index.close()
    return outcome


def _candidate_plans(
    compiler: AdaptiveRagCompiler,
    automatic_request: KnowledgeBaseRequest,
    inventory: SourceInventory,
    package: NormalizedKnowledgePackage,
    automatic_plan: RagStrategyPlan,
) -> list[CandidatePlan]:
    selected_topology = automatic_plan.storage.topology
    candidates: list[CandidatePlan] = []
    for requested in StorageTopology:
        if requested is selected_topology:
            resolved_plan = automatic_plan
            status = "selected"
        else:
            requested_compilation = compiler.compile(
                KnowledgeBaseRequest(
                    objective=automatic_request.objective,
                    preferred_storage=requested,
                ),
                inventory,
                package,
            )
            resolved_plan = requested_compilation.plan
            status = (
                "available"
                if resolved_plan.storage.topology is requested
                else "gated"
            )
            requested_compilation.index.close()

        limitations = [
            limitation
            for limitation in resolved_plan.strategy.limitations
            if not limitation.startswith("The selected adapter is local")
        ]
        gate_note = (
            limitations[-1]
            if limitations
            else resolved_plan.strategy.selection_rationale
        )
        candidates.append(
            CandidatePlan(
                requested_storage=requested.value,
                resolved_storage=resolved_plan.storage.topology.value,
                label=PLAN_LABELS[requested.value],
                algorithm=resolved_plan.strategy.search_algorithm.value,
                eligible=resolved_plan.storage.topology is requested,
                status=status,
                gate_note=gate_note,
            )
        )
    return candidates


def _normalized_package(
    case: DemoCase,
    inventory_id: str,
    sources: list[SourceDescriptor],
) -> NormalizedKnowledgePackage:
    structured = case.case_id == "repository-inventory"
    content_units = [
        ContentUnit(
            unit_id=f"UNIT-DEMO-{position:03d}",
            source_id=sources[position - 1].source_id,
            content=f"{evidence.supports}\n\n{evidence.excerpt}",
            location=evidence.location,
            metadata={
                "title": evidence.title,
                "format": "record" if structured else "prose",
                "structured": structured,
                "source_url": evidence.url,
            },
            evidence_ids=[evidence.evidence_id],
        )
        for position, evidence in enumerate(case.evidence, start=1)
    ]
    entities, relationships = _semantic_fixture(case.case_id)
    return NormalizedKnowledgePackage(
        package_id=f"PKG-DEMO-{case.case_id.upper()}",
        inventory_id=inventory_id,
        content_units=content_units,
        entities=entities,
        relationships=relationships,
        processing_report=ProcessingReport(
            accepted=len(content_units),
            failed=0,
            warnings=[],
            method_summary=(
                "Prepared semantic fixture grounded in the committed SICK corpus; "
                "used only by the local concept demo."
            ),
        ),
    )


def _semantic_fixture(
    case_id: str,
) -> tuple[list[KnowledgeEntity], list[KnowledgeRelationship]]:
    if case_id == "lidar-support":
        return (
            [
                _entity("challenge", "Challenge-Response", "AuthenticationMethod"),
                _entity("token", "Session Token", "AuthenticationMethod"),
                _entity("websocket", "WebSocket /apievents", "Protocol"),
                _entity("rest", "REST API", "Protocol"),
                _entity("binary", "Binary transfer", "Operation"),
                _entity("events", "Real-time events", "Operation"),
            ],
            [],
        )
    if case_id == "rfh5xx-integration":
        evidence_api = "EVID-KA08582-01"
        evidence_plc = "EVID-KA09345-01"
        entities = [
            _entity("rfh5xx", "RFH5xx", "ProductFamily"),
            _entity("sig200", "SIG200", "Gateway"),
            _entity("rest", "REST API", "Protocol"),
            _entity("insomnia", "Insomnia", "Tool"),
            _entity("siemens", "Siemens TIA", "PLCPlatform"),
            _entity("omron", "Omron Sysmac Studio", "PLCPlatform"),
            _entity("rockwell", "Rockwell Studio 5000", "PLCPlatform"),
            _entity("mitsubishi", "Mitsubishi GX Works3", "PLCPlatform"),
        ]
        relationships = [
            _relationship("rfh5xx", "connects_through", "sig200", evidence_api),
            _relationship("sig200", "exposes", "rest", evidence_api),
            _relationship("insomnia", "calls", "rest", evidence_api),
            _relationship("rfh5xx", "has_function_block_for", "siemens", evidence_plc),
            _relationship("rfh5xx", "has_function_block_for", "omron", evidence_plc),
            _relationship("rfh5xx", "has_function_block_for", "rockwell", evidence_plc),
            _relationship("rfh5xx", "has_function_block_for", "mitsubishi", evidence_plc),
        ]
        return entities, relationships
    if case_id == "repository-inventory":
        return [], []
    if case_id == "nova-impact":
        release = "EVID-KA09640-01"
        custom = "EVID-KA09513-01"
        hub = "EVID-KA09388-01"
        entities = [
            _entity("nova210", "Nova 2.10.0", "Release"),
            _entity("nova-api", "Nova Tool API", "API"),
            _entity("custom-tools", "Custom Nova tools", "ToolFamily"),
            _entity("nova-tools", "Nova tools", "ToolFamily"),
            _entity("visionary-t", "Visionary-T Mini AP", "ProductFamily"),
            _entity("inspector63", "InspectorP63x", "ProductFamily"),
            _entity("inspector85", "Inspector85x", "ProductFamily"),
            _entity("inspector83", "Inspector83x", "ProductFamily"),
            _entity("firmware", "Firmware release notes", "DocumentFamily"),
            _entity("release-hub", "SICK Nova release hub", "DocumentHub"),
        ]
        pairs = [
            ("nova210", "includes", "nova-tools", release),
            ("nova210", "documented_by", "release-hub", hub),
            ("nova-tools", "extends", "nova-api", release),
            ("nova-api", "used_by", "custom-tools", custom),
            ("custom-tools", "targets", "visionary-t", custom),
            ("custom-tools", "targets", "inspector63", custom),
            ("custom-tools", "targets", "inspector85", custom),
            ("nova210", "lists", "visionary-t", release),
            ("nova210", "lists", "inspector63", release),
            ("nova210", "lists", "inspector85", release),
            ("nova210", "lists", "inspector83", release),
            ("visionary-t", "validated_by", "firmware", release),
            ("inspector63", "validated_by", "firmware", release),
            ("inspector85", "validated_by", "firmware", release),
            ("firmware", "linked_from", "release-hub", hub),
        ]
        return (
            entities,
            [
                _relationship(subject, predicate, target, evidence)
                for subject, predicate, target, evidence in pairs
            ],
        )
    raise KeyError(f"Unknown semantic fixture: {case_id}")


def _entity(entity_id: str, label: str, entity_type: str) -> KnowledgeEntity:
    return KnowledgeEntity(id=entity_id, label=label, type=entity_type)


def _relationship(
    subject: str,
    predicate: str,
    target: str,
    evidence_id: str,
) -> KnowledgeRelationship:
    return KnowledgeRelationship(
        subject_id=subject,
        predicate=predicate,
        object_id=target,
        evidence_ids=[evidence_id],
        confidence="high",
    )


def _stages(
    *,
    case: DemoCase,
    selected: CandidatePlan,
    inventory_sources: int,
    signals: dict[str, int | float | bool],
    index_location: str,
    retrieved: int,
) -> list[DemoStage]:
    return [
        DemoStage(
            number=1,
            name="Inventario",
            summary=f"{inventory_sources} fuentes clasificadas por el core.",
            artifact="SourceInventory con checksums e IDs estables",
        ),
        DemoStage(
            number=2,
            name="Paquete semántico",
            summary=f"{signals['content_units']} unidades normalizadas y trazables.",
            artifact="NormalizedKnowledgePackage validado",
        ),
        DemoStage(
            number=3,
            name="Relaciones",
            summary=(
                f"{signals['entities']} entidades · "
                f"{signals['relationships']} relaciones · "
                f"{signals['cycle_surplus']} ciclos excedentes."
            ),
            artifact="Señales calculadas por selection_signals()",
        ),
        DemoStage(
            number=4,
            name="Selección adaptativa",
            summary=f"{selected.label} en modo automático.",
            artifact=selected.algorithm,
        ),
        DemoStage(
            number=5,
            name="Indexación local",
            summary="Índice real del core construido en memoria.",
            artifact=index_location,
        ),
        DemoStage(
            number=6,
            name="Tool call y validación",
            summary=f"{retrieved} evidencias recuperadas por search_evidence.",
            artifact="ToolRegistry real · sin proveedor LLM",
        ),
    ]
