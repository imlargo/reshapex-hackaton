from __future__ import annotations

import re

from .extract import RawSegment

MAX_UNIT_CHARS = 1800


def normalize_segments(
    segments: list[RawSegment],
    *,
    source_id: str,
    source_name: str,
) -> tuple[list[dict], list[str]]:
    units: list[dict] = []
    warnings: list[str] = []
    unit_counter = 0

    for segment in segments:
        cleaned = _clean_text(segment.text)
        if not cleaned:
            warnings.append(f"{source_name}: empty segment at {segment.location}")
            continue
        for index, chunk in enumerate(_chunk_text(cleaned, MAX_UNIT_CHARS), start=1):
            unit_counter += 1
            location = segment.location
            if len(_chunk_text(cleaned, MAX_UNIT_CHARS)) > 1:
                location = f"{segment.location} chunk {index}"
            units.append(
                {
                    "unit_id": f"UNIT-TMP-{unit_counter:04d}",
                    "source_id": source_id,
                    "content": chunk,
                    "location": location,
                    "metadata": {
                        **segment.metadata,
                        "source_name": source_name,
                    },
                }
            )
    return units, warnings


def _clean_text(text: str) -> str:
    text = re.sub(r"\r\n?", "\n", text)
    text = re.sub(r"[ \t]+\n", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = re.sub(r"[^\S\n]+", " ", text)
    return text.strip()


def _chunk_text(text: str, chunk_size: int) -> list[str]:
    paragraphs = [part.strip() for part in re.split(r"\n\s*\n", text) if part.strip()]
    chunks: list[str] = []
    current = ""
    for paragraph in paragraphs:
        candidate = paragraph if not current else f"{current}\n\n{paragraph}"
        if len(candidate) <= chunk_size:
            current = candidate
            continue
        if current:
            chunks.append(current)
        if len(paragraph) <= chunk_size:
            current = paragraph
            continue
        chunks.extend(
            paragraph[index : index + chunk_size] for index in range(0, len(paragraph), chunk_size)
        )
        current = ""
    if current:
        chunks.append(current)
    return chunks or [text[:chunk_size]]
