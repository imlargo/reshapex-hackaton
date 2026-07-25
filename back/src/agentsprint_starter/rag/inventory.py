from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

from .contracts import (
    DocumentClass,
    SourceClassification,
    SourceDescriptor,
    SourceInventory,
    SourceStatus,
)

MEDIA_TYPES = {
    ".adoc": "text/asciidoc",
    ".csv": "text/csv",
    ".htm": "text/html",
    ".html": "text/html",
    ".json": "application/json",
    ".md": "text/markdown",
    ".pdf": "application/pdf",
    ".txt": "text/plain",
    ".yaml": "application/yaml",
    ".yml": "application/yaml",
}
STRUCTURED_SUFFIXES = {".csv", ".json", ".yaml", ".yml"}
TEXT_SUFFIXES = {".adoc", ".csv", ".htm", ".html", ".json", ".md", ".txt", ".yaml", ".yml"}


def inventory_from_uploads(
    files: list[tuple[str, bytes]],
    objective: str,
) -> SourceInventory:
    descriptors: list[SourceDescriptor] = []
    classifications: list[SourceClassification] = []

    for position, (name, payload) in enumerate(files, start=1):
        checksum = hashlib.sha256(payload).hexdigest().upper()
        descriptor, classification = _describe(
            name=name,
            size_bytes=len(payload),
            checksum=checksum,
            sample=payload[:16384],
            position=position,
        )
        descriptors.append(descriptor)
        classifications.append(classification)

    return _inventory(objective, descriptors, classifications)


def inventory_from_paths(
    paths: list[Path],
    objective: str,
    *,
    display_root: Path | None = None,
) -> SourceInventory:
    descriptors: list[SourceDescriptor] = []
    classifications: list[SourceClassification] = []
    resolved_root = display_root.resolve() if display_root else None

    for position, path in enumerate(paths, start=1):
        resolved = path.resolve()
        name = (
            resolved.relative_to(resolved_root).as_posix()
            if resolved_root and resolved.is_relative_to(resolved_root)
            else path.name
        )
        digest = hashlib.sha256()
        sample = b""
        with resolved.open("rb") as stream:
            sample = stream.read(16384)
            digest.update(sample)
            while chunk := stream.read(1024 * 1024):
                digest.update(chunk)
        descriptor, classification = _describe(
            name=name,
            size_bytes=resolved.stat().st_size,
            checksum=digest.hexdigest().upper(),
            sample=sample,
            position=position,
        )
        descriptors.append(descriptor)
        classifications.append(classification)

    return _inventory(objective, descriptors, classifications)


def _inventory(
    objective: str,
    descriptors: list[SourceDescriptor],
    classifications: list[SourceClassification],
) -> SourceInventory:
    inventory_seed = "\n".join(
        [objective.strip(), *(source.checksum for source in descriptors)]
    )
    inventory_id = (
        "INV-"
        + hashlib.sha256(inventory_seed.encode("utf-8")).hexdigest()[:12].upper()
    )
    unsupported = [
        source.name
        for source in descriptors
        if source.status is SourceStatus.UNSUPPORTED
    ]
    limitations = [
        (
            "Classification uses file metadata and a bounded sample; semantic "
            "extraction remains the NormalizedKnowledgePackage producer's responsibility."
        )
    ]
    if unsupported:
        limitations.append(f"Unsupported source types: {', '.join(unsupported)}")
    return SourceInventory(
        inventory_id=inventory_id,
        objective=objective,
        sources=descriptors,
        classes=classifications,
        limitations=limitations,
    )


def _describe(
    *,
    name: str,
    size_bytes: int,
    checksum: str,
    sample: bytes,
    position: int,
) -> tuple[SourceDescriptor, SourceClassification]:
    suffix = Path(name).suffix.casefold()
    supported = suffix in MEDIA_TYPES
    source_id = f"SRC-{position:03d}-{checksum[:8]}"
    document_class = (
        _document_class(name, suffix, sample) if supported else DocumentClass.UNSUPPORTED
    )
    status = SourceStatus.ACCEPTED if supported else SourceStatus.UNSUPPORTED
    message = (
        "Accepted for inventory; content extraction is a downstream stage."
        if supported
        else f"Unsupported source type: {suffix or 'no extension'}."
    )
    language = _language(name, suffix, sample)
    signals = {
        "suffix": suffix or "(none)",
        "likely_structured": suffix in STRUCTURED_SUFFIXES,
        "likely_prose": suffix not in STRUCTURED_SUFFIXES and supported,
        "relationship_cues": _relationship_cues(name, sample),
    }
    descriptor = SourceDescriptor(
        source_id=source_id,
        name=name,
        media_type=MEDIA_TYPES.get(suffix, "application/octet-stream"),
        size_bytes=size_bytes,
        checksum=checksum,
        status=status,
        message=message,
    )
    classification = SourceClassification(
        source_id=source_id,
        document_class=document_class,
        language=language,
        signals=signals,
    )
    return descriptor, classification


def _document_class(name: str, suffix: str, sample: bytes) -> DocumentClass:
    normalized_name = name.casefold().replace("-", "_")
    if "datasheet" in normalized_name or "data_sheet" in normalized_name:
        return DocumentClass.DATASHEET
    if "operating_instruction" in normalized_name:
        return DocumentClass.OPERATING_INSTRUCTION
    if "technical_information" in normalized_name:
        return DocumentClass.TECHNICAL_INFORMATION
    if re.search(r"(?:^|[/_])ka[_-]?\d+", normalized_name):
        return DocumentClass.KNOWLEDGE_ARTICLE
    if "productoverview" in normalized_name or "product_overview" in normalized_name:
        return DocumentClass.PRODUCT_OVERVIEW
    if "guide" in normalized_name:
        return DocumentClass.GUIDE
    if "repositories" in normalized_name:
        return DocumentClass.REPOSITORY_METADATA
    if suffix in STRUCTURED_SUFFIXES:
        if suffix == ".json" and _looks_like_repository_inventory(sample):
            return DocumentClass.REPOSITORY_METADATA
        return DocumentClass.STRUCTURED_DATA
    if suffix in {".adoc", ".md"}:
        return DocumentClass.SOFTWARE_DOCUMENTATION
    return DocumentClass.GENERAL_DOCUMENT


def _looks_like_repository_inventory(sample: bytes) -> bool:
    try:
        value = json.loads(sample.decode("utf-8-sig"))
    except (UnicodeDecodeError, json.JSONDecodeError):
        return False
    serialized = json.dumps(value)[:8000].casefold()
    return "clone_url" in serialized or "html_url" in serialized


def _language(name: str, suffix: str, sample: bytes) -> str:
    lower_name = name.casefold()
    if re.search(r"(?:^|[_-])es(?:[._-]|$)", lower_name):
        return "es"
    if re.search(r"(?:^|[_-])en(?:[._-]|$)", lower_name):
        return "en"
    if suffix not in TEXT_SUFFIXES:
        return "unknown"
    try:
        text = sample.decode("utf-8-sig").casefold()
    except UnicodeDecodeError:
        return "unknown"
    spanish = len(re.findall(r"\b(?:el|la|los|las|para|con|sensor|documento)\b", text))
    english = len(re.findall(r"\b(?:the|and|for|with|sensor|document)\b", text))
    if spanish > english:
        return "es"
    if english:
        return "en"
    return "unknown"


def _relationship_cues(name: str, sample: bytes) -> int:
    text = name
    try:
        text += " " + sample.decode("utf-8-sig")
    except UnicodeDecodeError:
        pass
    cues = {
        "compatible",
        "dependency",
        "depends",
        "family",
        "protocol",
        "relation",
        "requires",
        "supports",
    }
    lowered = text.casefold()
    return sum(lowered.count(cue) for cue in cues)
