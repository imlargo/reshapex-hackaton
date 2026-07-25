from pathlib import Path

from agentsprint_starter.rag import (
    DocumentClass,
    SourceStatus,
    inventory_from_paths,
    inventory_from_uploads,
)


def test_inventory_is_objective_first_stable_and_classified() -> None:
    files = [
        ("dataSheet_WTB4_en.pdf", b"%PDF representative bytes"),
        ("SICKAG_repositories.json", b'[{"html_url": "https://example.test"}]'),
    ]
    objective = "Compare product specifications and supported protocols."

    first = inventory_from_uploads(files, objective)
    second = inventory_from_uploads(files, objective)

    assert first.inventory_id == second.inventory_id
    assert [source.source_id for source in first.sources] == [
        source.source_id for source in second.sources
    ]
    assert first.classes[0].document_class is DocumentClass.DATASHEET
    assert first.classes[1].document_class is DocumentClass.REPOSITORY_METADATA
    assert all(source.status is SourceStatus.ACCEPTED for source in first.sources)


def test_inventory_reports_unsupported_files_without_hiding_them() -> None:
    inventory = inventory_from_uploads(
        [("scan.exe", b"not a document")],
        "Build a support knowledge base.",
    )

    assert inventory.sources[0].status is SourceStatus.UNSUPPORTED
    assert inventory.classes[0].document_class is DocumentClass.UNSUPPORTED
    assert "scan.exe" in inventory.limitations[-1]


def test_path_inventory_preserves_relative_names(tmp_path: Path) -> None:
    corpus = tmp_path / "corpus"
    corpus.mkdir()
    source = corpus / "manual_es.md"
    source.write_text("Manual del sensor para instalación.", encoding="utf-8")

    inventory = inventory_from_paths(
        [source],
        "Responder preguntas de instalación.",
        display_root=corpus,
    )

    assert inventory.sources[0].name == "manual_es.md"
    assert inventory.classes[0].language == "es"
