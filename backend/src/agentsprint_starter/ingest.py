from __future__ import annotations

import hashlib
import re
from pathlib import Path

from .schemas import EvidenceRecord

SUPPORTED_SUFFIXES = {".txt", ".md", ".csv", ".json"}


def records_from_uploads(files: list[tuple[str, bytes]]) -> list[EvidenceRecord]:
    records: list[EvidenceRecord] = []
    for source_number, (name, payload) in enumerate(files, start=1):
        suffix = Path(name).suffix.casefold()
        if suffix not in SUPPORTED_SUFFIXES:
            raise ValueError(f"Unsupported source type for {name}.")
        try:
            text = payload.decode("utf-8-sig")
        except UnicodeDecodeError as exc:
            raise ValueError(f"{name} is not valid UTF-8 text.") from exc
        records.extend(records_from_text(name, text, source_number=source_number))
    return records


def records_from_text(
    name: str,
    text: str,
    *,
    source_number: int = 1,
    chunk_size: int = 1800,
) -> list[EvidenceRecord]:
    normalized = re.sub(r"\r\n?", "\n", text).strip()
    if not normalized:
        return []
    source_hash = hashlib.sha256(normalized.encode("utf-8")).hexdigest()[:8].upper()
    source_id = f"SRC-{source_number:02d}-{source_hash}"
    chunks = _chunk_text(normalized, chunk_size)
    return [
        EvidenceRecord(
            evidence_id=f"EVID-{source_number:02d}-{index:03d}",
            source_id=source_id,
            title=name,
            content=chunk,
            location=f"chunk {index}/{len(chunks)}",
            metadata={"filename": name},
        )
        for index, chunk in enumerate(chunks, start=1)
    ]


def _chunk_text(text: str, chunk_size: int) -> list[str]:
    paragraphs = [part.strip() for part in re.split(r"\n\s*\n", text) if part.strip()]
    chunks: list[str] = []
    current = ""
    for paragraph in paragraphs:
        candidates = (
            [
                paragraph[index : index + chunk_size]
                for index in range(0, len(paragraph), chunk_size)
            ]
            if len(paragraph) > chunk_size
            else [paragraph]
        )
        for candidate in candidates:
            joined = f"{current}\n\n{candidate}".strip() if current else candidate
            if current and len(joined) > chunk_size:
                chunks.append(current)
                current = candidate
            else:
                current = joined
    if current:
        chunks.append(current)
    return chunks
