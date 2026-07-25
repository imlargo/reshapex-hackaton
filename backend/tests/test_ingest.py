from agentsprint_starter.ingest import records_from_text, records_from_uploads


def test_ingest_assigns_stable_ids_and_locations() -> None:
    text = "First paragraph.\n\nSecond paragraph."
    first = records_from_text("source.md", text, source_number=2, chunk_size=20)
    second = records_from_text("source.md", text, source_number=2, chunk_size=20)

    assert [item.evidence_id for item in first] == [item.evidence_id for item in second]
    assert first[0].source_id == second[0].source_id
    assert all(item.location.startswith("chunk ") for item in first)


def test_ingest_rejects_unsupported_binary() -> None:
    try:
        records_from_uploads([("manual.pdf", b"%PDF")])
    except ValueError as exc:
        assert "Unsupported source type" in str(exc)
    else:
        raise AssertionError("Expected unsupported source type to fail.")
