import pytest

from agentsprint_starter.schemas import EvidenceRecord
from agentsprint_starter.tools import EvidenceStore, ToolExecutionError, ToolRegistry


@pytest.fixture
def registry() -> ToolRegistry:
    return ToolRegistry(
        EvidenceStore(
            [
                EvidenceRecord(
                    evidence_id="EVID-A01",
                    source_id="SRC-A",
                    title="Pump inspection interval",
                    content="Inspect the pump every 500 operating hours.",
                ),
                EvidenceRecord(
                    evidence_id="EVID-B01",
                    source_id="SRC-B",
                    title="Safety notice",
                    content="Isolate electrical power before opening the pump.",
                ),
            ]
        )
    )


def test_search_is_ranked_and_bounded(registry: ToolRegistry) -> None:
    result = registry.execute("search_evidence", {"query": "pump inspection", "limit": 1})

    assert result["count"] == 1
    assert result["evidence"][0]["evidence_id"] == "EVID-A01"


def test_registry_exposes_typed_langchain_tools(registry: ToolRegistry) -> None:
    assert {tool.name for tool in registry.langchain_tools} == {
        "search_evidence",
        "get_evidence",
        "list_sources",
    }
    search = registry.get_langchain_tool("search_evidence")
    assert search is not None
    assert search.args_schema is not None


def test_unknown_tool_fails_honestly(registry: ToolRegistry) -> None:
    with pytest.raises(ToolExecutionError, match="Unknown tool"):
        registry.execute("invent_answer", {})


def test_duplicate_evidence_ids_are_rejected() -> None:
    record = EvidenceRecord(
        evidence_id="EVID-DUP",
        source_id="SRC",
        title="Title",
        content="Content",
    )
    with pytest.raises(ValueError, match="unique"):
        EvidenceStore([record, record])
