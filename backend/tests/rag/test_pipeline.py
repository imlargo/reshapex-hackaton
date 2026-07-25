from agentsprint_starter.config import Settings
from agentsprint_starter.rag import AdaptiveRagCompiler, KnowledgeBaseRequest
from agentsprint_starter.testing import DeterministicChatModel

from .factories import make_package


def test_compiler_exposes_index_through_typed_tools_and_langgraph() -> None:
    compiler = AdaptiveRagCompiler()
    request = KnowledgeBaseRequest(objective="Answer inspection questions.")
    inventory = compiler.inventory(
        request,
        [("inspection.md", b"The inspection threshold is 500 operating hours.")],
    )
    package = make_package(
        contents=["The inspection threshold is 500 operating hours."],
        inventory_id=inventory.inventory_id,
    )

    compiled = compiler.compile(request, inventory, package)
    tool_result = compiled.tools.execute(
        "search_evidence",
        {"query": "inspection threshold", "limit": 1},
    )
    runner = compiled.create_runner(
        DeterministicChatModel(),
        settings=Settings(_env_file=None),
    )
    outcome = runner.run("What is the inspection threshold?")

    assert tool_result["evidence"][0]["evidence_id"] == "EVID-TEST-001"
    assert outcome.result.citations[0].evidence_id == "EVID-TEST-001"
    assert any(event.kind == "tool" for event in outcome.trace.events)


def test_compiler_rejects_a_package_from_another_inventory() -> None:
    compiler = AdaptiveRagCompiler()
    request = KnowledgeBaseRequest(objective="Answer support questions.")
    inventory = compiler.inventory(request, [("support.md", b"Support content.")])
    package = make_package(
        contents=["Support content."],
        inventory_id="INV-OTHER000001",
    )

    try:
        compiler.compile(request, inventory, package)
    except ValueError as exc:
        assert "does not reference" in str(exc)
    else:
        raise AssertionError("Expected cross-inventory compilation to fail.")
