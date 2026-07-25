# SICK Documentation Corpus — ReshapeX Hackathon

Research corpus gathered for **Usuario 2 (semantic processing)** and the SICK knowledge-base compiler agent.
Curated by **Jeronimo0228** for the ReshapeX AgentSprint hackathon.

> **Purpose:** Representative multi-layer documentation for extraction, normalization, entity/relationship detection, and RAG grounding tests.
> **Brand:** SICK AG — industrial sensors, safety, machine vision, sensor integration.
> **Research date:** 2026-07-24 / 2026-07-25

---

## Structure

```
contents/
├── README.md                 ← this file
├── MANIFEST.json             ← machine-readable inventory
├── download_results.json     ← download log (status + sizes)
├── portals/PORTALS.md        ← 6-layer portal map
├── url_patterns/URL_PATTERNS.md  ← URL conventions for crawlers/indexers
├── pdfs/
│   ├── datasheets/           ← SKU-level data sheets (WTB4 family, AssetHub)
│   ├── technical_information/← IO-Link, PSS, compact format, CSS/CSx
│   ├── operating_instructions/← SIG200, SIG350, safety, vision, encoders
│   ├── product_overviews/    ← W4 family + machine vision segment
│   └── guides/               ← Guide for Safe Machinery
├── knowledge_base/           ← 19 support.sick.com KB articles (HTML)
│   ├── INDEX.md / INDEX.json
│   └── KA-*.html
└── github/                   ← SICKAG org inventory + key READMEs
    ├── SICKAG_repositories.json
    └── *.md / *.adoc
```

---

## Source layers (6 capas)

| Layer | Base URL | Local artifacts |
| --- | --- | --- |
| 1 — Catalog | https://www.sick.com | PDFs (datasheets, overviews) |
| 2 — Product ID | https://pid.sick.com/{P/N}/{S/N} | Documented in `portals/PORTALS.md` |
| 3 — Support KB | https://support.sick.com/knowledgebase/ | `knowledge_base/KA-*.html` |
| 4 — GitHub | https://github.com/SICKAG | `github/SICKAG_repositories.json` |
| 5 — Cloud services | AssetHub, Function Block Factory | Portal refs + AssetHub datasheet |
| 6 — Desktop tools | SOPAS ET, Safety Designer, Nova | Referenced in KB + operating instructions |

See `portals/PORTALS.md` for full portal inventory and drift signals per layer.

---

## Key demo SKUs / documents

| Artifact | SKU / ID | Relevance |
| --- | --- | --- |
| W4 product overview | Family W4 | Ordering tables, product families |
| WTB4S-3N2131 datasheet | Order 1042061 | Photoelectric mini, specs |
| WTB4FP-1G312120ZZZ | Order 1120711 | Background suppression variant |
| WTB4FT-31311120ZZZ | Order 1113180 | Foreground suppression variant |
| IM0077697 | IO-Link photoelectric | ISDU, Smart Sensor parameters |
| IM0084724 | SIG200 REST API | Integration / gateway |
| IM0086162 | SIG200 Profinet | PLC integration (demo RFQ use case) |
| IM0104623 | Compact format spec | Binary telegram / data format |
| KA-09480, KA-09665, KA-10741 | KB articles | Firmware, integration, troubleshooting |

---

## Suggested entity types (from corpus)

- `ProductSKU`, `OrderNumber`, `ProductFamily`, `Protocol`, `Specification`, `Accessory`, `FirmwareVersion`, `DocumentID`

## Suggested relationship predicates

- `has_order_number`, `belongs_to_family`, `supports_protocol`, `compatible_with`, `requires_module`, `supersedes`, `operates_in_temp_range`

---

## Usage notes for Usuario 2

1. **Do not treat HTML KB files as final clean text** — run extraction/normalization pipeline on them.
2. **PDFs are authoritative** for specs and ordering; KB for drift/firmware/release notes.
3. **Lineage:** map each extracted unit back to `source_id` (file path under `contents/`) and page/section in `location`.
4. **Register in project manifest:** when moving to `agentsprint/00_inbox/raw/`, append entries to `SOURCE_MANIFEST.md` (coordinate with Usuario 1).

---

## External references (not downloaded)

- IO-Link IODD finder: https://ioddfinder.io-link.com/
- SICK Sensor Starter Kits docs site: https://sickag.github.io/SICK-Sensor-Starter-Kits
- SICK AppSpace Coding Starter Kit org: https://github.com/SICKAppSpaceCodingStarterKit (~50 repos)

---

## License / attribution

All documents © SICK AG. This folder is for **hackathon research and internal team use** only.
Downloaded from publicly accessible SICK portals on 2026-07-25.
