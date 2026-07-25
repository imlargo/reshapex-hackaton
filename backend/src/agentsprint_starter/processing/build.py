from __future__ import annotations

import json
from pathlib import Path

from agentsprint_starter.rag import NormalizedKnowledgePackage

from .inventory import (
    DEFAULT_CORPUS_GLOBS,
    REPRESENTATIVE_GLOBS,
    build_inventory_from_directory,
    inventory_to_json,
)
from .pipeline import process_inventory, write_cleaned_artifacts


def package_to_json(package: NormalizedKnowledgePackage) -> str:
    return json.dumps(package.model_dump(mode="json"), indent=2, ensure_ascii=False)


def evidence_map_markdown(rows: list[dict]) -> str:
    lines = [
        "# Evidence Map\n",
        "| Evidence ID | Source ID | Unit ID | Location | Source name | Verification |\n",
        "| --- | --- | --- | --- | --- | --- |\n",
    ]
    for row in rows:
        line = (
            "| {evidence_id} | {source_id} | {unit_id} | {location} | "
            "`{source_name}` | extracted + normalized |\n"
        )
        lines.append(line.format(**row))
    return "".join(lines)


def build_semantic_artifacts(
    corpus_dir: Path,
    knowledge_dir: Path,
    *,
    package_id: str | None = None,
    representative_only: bool = False,
) -> tuple[NormalizedKnowledgePackage, list[dict]]:
    knowledge_dir = knowledge_dir.resolve()
    corpus_dir = corpus_dir.resolve()
    globs = REPRESENTATIVE_GLOBS if representative_only else DEFAULT_CORPUS_GLOBS

    inventory = build_inventory_from_directory(corpus_dir, include_globs=globs)
    cleaned_dir = knowledge_dir / "cleaned"
    structured_dir = knowledge_dir / "structured"
    cleaned_dir.mkdir(parents=True, exist_ok=True)
    structured_dir.mkdir(parents=True, exist_ok=True)

    write_cleaned_artifacts(inventory, corpus_dir, cleaned_dir)
    outcome = process_inventory(inventory, corpus_dir, package_id=package_id)
    package = outcome.package
    evidence_rows = outcome.evidence_rows

    pkg_name = package.package_id if package_id is None else package_id
    pkg_path = structured_dir / f"{pkg_name}.json"
    pkg_path.write_text(package_to_json(package), encoding="utf-8")
    inv_path = structured_dir / f"{inventory.inventory_id}.json"
    inv_path.write_text(inventory_to_json(inventory), encoding="utf-8")
    map_path = knowledge_dir / "EVIDENCE_MAP.md"
    map_path.write_text(evidence_map_markdown(evidence_rows), encoding="utf-8")

    return package, evidence_rows


def main() -> None:
    repo_root = Path(__file__).resolve().parents[3]
    corpus_dir = repo_root / "contents"
    knowledge_dir = repo_root / "agentsprint" / "05_knowledge"
    package, rows = build_semantic_artifacts(
        corpus_dir,
        knowledge_dir,
        representative_only=False,
    )
    print(
        f"Built {package.package_id}: "
        f"{len(package.content_units)} units, "
        f"{len(package.entities)} entities, "
        f"{len(package.relationships)} relationships, "
        f"{len(rows)} evidence rows"
    )


if __name__ == "__main__":
    main()
