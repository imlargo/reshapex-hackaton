from __future__ import annotations

import hashlib
import html
import re
import subprocess
from dataclasses import dataclass
from pathlib import Path

TEXT_SUFFIXES = {".txt", ".md", ".csv", ".json"}
HTML_SUFFIXES = {".html", ".htm"}
PDF_SUFFIXES = {".pdf"}


@dataclass(frozen=True)
class RawSegment:
    text: str
    location: str
    metadata: dict[str, str | int | float | bool]


@dataclass(frozen=True)
class ExtractionResult:
    segments: list[RawSegment]
    warnings: list[str]
    failed: bool = False


def extract_file(path: Path) -> ExtractionResult:
    suffix = path.suffix.casefold()
    if suffix in TEXT_SUFFIXES:
        return _extract_text_file(path)
    if suffix in HTML_SUFFIXES:
        return _extract_html_file(path)
    if suffix in PDF_SUFFIXES:
        return _extract_pdf_file(path)
    return ExtractionResult(
        segments=[],
        warnings=[f"Unsupported media type for {path.name}"],
        failed=True,
    )


def file_checksum(path: Path) -> str:
    digest = hashlib.sha256()
    digest.update(path.read_bytes())
    return digest.hexdigest()[:16]


def detect_document_class(path: Path) -> str:
    name = path.name.casefold()
    if "datasheet" in name:
        return "datasheet"
    if "productoverview" in name or "product_overview" in name:
        return "product_overview"
    if "operating_instructions" in name:
        return "operating_instructions"
    if "technical_information" in name:
        return "technical_information"
    if name.startswith("ka-"):
        return "knowledge_base_article"
    if path.suffix.casefold() in HTML_SUFFIXES:
        return "knowledge_base_article"
    return "general_document"


def detect_language(text: str, path: Path) -> str:
    name = path.name.casefold()
    if "_es_" in name or name.endswith("_es.pdf") or name.endswith("_es.html"):
        return "es"
    if "es_im" in name:
        return "es"
    sample = text[:2000].lower()
    if any(token in sample for token in (" der ", " und ", " mit ", " für ")):
        return "de"
    return "en"


def _extract_text_file(path: Path) -> ExtractionResult:
    try:
        text = path.read_text(encoding="utf-8-sig")
    except UnicodeDecodeError:
        return ExtractionResult(
            segments=[],
            warnings=[f"{path.name} is not valid UTF-8 text"],
            failed=True,
        )
    normalized = re.sub(r"\r\n?", "\n", text).strip()
    if not normalized:
        return ExtractionResult(segments=[], warnings=[f"{path.name} is empty"], failed=True)
    return ExtractionResult(
        segments=[RawSegment(text=normalized, location="full document", metadata={"pages": 1})],
        warnings=[],
    )


def _extract_html_file(path: Path) -> ExtractionResult:
    raw = path.read_text(encoding="utf-8", errors="ignore")
    stripped = re.sub(r"(?is)<(script|style).*?>.*?</\1>", " ", raw)
    stripped = re.sub(r"(?is)<br\s*/?>", "\n", stripped)
    stripped = re.sub(r"(?is)</(p|div|li|h\d|tr)>", "\n", stripped)
    stripped = re.sub(r"(?is)<[^>]+>", " ", stripped)
    text = html.unescape(re.sub(r"[ \t]+", " ", stripped))
    text = re.sub(r"\n\s*\n+", "\n\n", text).strip()
    if not text:
        return ExtractionResult(
            segments=[],
            warnings=[f"{path.name} produced no readable text after HTML stripping"],
            failed=True,
        )
    return ExtractionResult(
        segments=[RawSegment(text=text, location="html body", metadata={"pages": 1})],
        warnings=[],
    )


def _extract_pdf_file(path: Path) -> ExtractionResult:
    try:
        completed = subprocess.run(
            ["pdftotext", "-layout", str(path), "-"],
            capture_output=True,
            check=True,
            text=True,
            timeout=120,
        )
    except (subprocess.CalledProcessError, FileNotFoundError, subprocess.TimeoutExpired) as exc:
        return ExtractionResult(
            segments=[],
            warnings=[f"pdftotext failed for {path.name}: {exc}"],
            failed=True,
        )
    text = re.sub(r"\r\n?", "\n", completed.stdout).strip()
    if not text:
        return ExtractionResult(
            segments=[],
            warnings=[f"{path.name} produced no text (possible scan-only PDF)"],
            failed=True,
        )
    page_chunks = _split_pdf_pages(text)
    segments = [
        RawSegment(
            text=chunk,
            location=f"page {index}/{len(page_chunks)}",
            metadata={"page": index, "pages": len(page_chunks)},
        )
        for index, chunk in enumerate(page_chunks, start=1)
        if chunk.strip()
    ]
    warnings: list[str] = []
    if len(segments) > 40:
        warnings.append(f"{path.name} split into {len(segments)} page segments")
    return ExtractionResult(segments=segments, warnings=warnings)


def _split_pdf_pages(text: str) -> list[str]:
    if "\f" in text:
        return [part.strip() for part in text.split("\f") if part.strip()]
    return _chunk_by_length(text, 3500)


def _chunk_by_length(text: str, size: int) -> list[str]:
    paragraphs = [part.strip() for part in re.split(r"\n\s*\n", text) if part.strip()]
    chunks: list[str] = []
    current = ""
    for paragraph in paragraphs:
        candidate = paragraph if not current else f"{current}\n\n{paragraph}"
        if len(candidate) <= size:
            current = candidate
            continue
        if current:
            chunks.append(current)
        if len(paragraph) <= size:
            current = paragraph
            continue
        chunks.extend(paragraph[index : index + size] for index in range(0, len(paragraph), size))
        current = ""
    if current:
        chunks.append(current)
    return chunks or [text[:size]]
