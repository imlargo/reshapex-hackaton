from __future__ import annotations

from pathlib import Path

from agentsprint_starter.rag import SourceInventory, inventory_from_paths

DEFAULT_CORPUS_GLOBS = (
    "pdfs/**/*.pdf",
    "knowledge_base/KA-*.html",
)

REPRESENTATIVE_GLOBS = (
    "pdfs/datasheets/dataSheet_WTB4S*.pdf",
    "pdfs/datasheets/dataSheet_WTB4FP*.pdf",
    "pdfs/product_overviews/productoverview_W4*.pdf",
    "pdfs/operating_instructions/operating_instructions_SIG200_Profinet*.pdf",
    "pdfs/technical_information/technical_information_photoelectric*.pdf",
    "knowledge_base/KA-09480.html",
)


def collect_corpus_paths(
    corpus_dir: Path,
    *,
    include_globs: tuple[str, ...] = DEFAULT_CORPUS_GLOBS,
) -> list[Path]:
    corpus_dir = corpus_dir.resolve()
    paths: list[Path] = []
    for pattern in include_globs:
        paths.extend(sorted(corpus_dir.glob(pattern)))
    return sorted({path.resolve() for path in paths if path.is_file()})


def build_inventory_from_directory(
    corpus_dir: Path,
    *,
    objective: str = (
        "Build a cited SICK knowledge base for SKU lookup, protocol compatibility, "
        "and product-family relationships."
    ),
    include_globs: tuple[str, ...] = DEFAULT_CORPUS_GLOBS,
) -> SourceInventory:
    paths = collect_corpus_paths(corpus_dir, include_globs=include_globs)
    return inventory_from_paths(paths, objective, display_root=corpus_dir)


def resolve_source_path(corpus_dir: Path, source_name: str) -> Path:
    return corpus_dir / source_name


def inventory_to_json(inventory: SourceInventory) -> str:
    return inventory.model_dump_json(indent=2)


def stable_evidence_id(source_id: str, chunk_number: int, content: str) -> str:
    import hashlib

    digest = hashlib.sha256(content.encode("utf-8")).hexdigest()[:8].upper()
    safe_source = source_id.replace("/", "-").upper()
    return f"EVID-{safe_source}-{chunk_number:04d}-{digest}"


def package_id_for_inventory(inventory_id: str) -> str:
    import hashlib

    suffix = hashlib.sha256(inventory_id.encode("utf-8")).hexdigest()[:12].upper()
    return f"PKG-{suffix}"
