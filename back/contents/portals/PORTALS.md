# SICK Documentation Portals — 6-Layer Map

Research inventory for RAG corpus design and grounding-health drift detection.

## Layer 1 — sick.com Catalog

| Resource | URL | Format | Notes |
| --- | --- | --- | --- |
| US catalog | https://www.sick.com/us/en/catalog/ | HTML | Product categories, variants |
| Product search | https://www.sick.com/us/en/search?text={part_number} | HTML | SKU lookup |
| Family shortlinks | https://www.sick.com/W4 | HTML | Family landing pages |
| Product page pattern | https://www.sick.com/us/en/catalog/products/{category}/p/p{productId} | HTML | Tabs: Downloads, Technical |
| Datasheet PDF pattern | https://www.sick.com/media/pdf/{d1}/{d2}/{d3}/dataSheet_{SKU}_{orderNo}_en.pdf | PDF | Primary specs source |
| Operating instructions | https://www.sick.com/media/docs/{d1}/{d2}/{d3}/operating_instructions_*_en_im{8digits}.pdf | PDF | IM document numbers |
| Technical information | https://www.sick.com/media/docs/{d1}/{d2}/{d3}/technical_information_*_en_im{8digits}.pdf | PDF | Protocols, formats |
| Product overviews | https://www.sick.com/media/productoverview/.../productoverview_{family}_*.pdf | PDF | Family ordering tables |

**Drift signals:** EOL notices, new order numbers, spec table changes, marketing text updates.

---

## Layer 2 — pid.sick.com (Product ID)

| Resource | URL | Format |
| --- | --- | --- |
| Product hub | https://pid.sick.com/{part_number}/{serial_number} | HTML + downloads |

Per-device hub: datasheets, CAD, certificates, firmware, software bundles.
**Drift signals:** Firmware version bumps, cert updates, per-serial documentation changes.

---

## Layer 3 — support.sick.com Knowledge Base

| Resource | URL | Format |
| --- | --- | --- |
| KB home | https://support.sick.com/knowledgebase/ | HTML |
| Article pattern | https://support.sick.com/sick-knowledgebase/article/?code=KA-{5digits} | HTML |

**Content types:** firmware release notes, integration guides, troubleshooting, compatibility matrices, software updates.

**Drift signals:** Release notes, firmware restrictions (e.g. cannot downgrade), protocol errata.

Local copies: `../knowledge_base/KA-*.html` (19 articles indexed).

---

## Layer 4 — GitHub (SICKAG + AppSpace)

| Resource | URL | Format |
| --- | --- | --- |
| Main org | https://github.com/SICKAG | Code + docs |
| Repo inventory | ../github/SICKAG_repositories.json | JSON (57 repos) |
| Sensor Starter Kits | https://github.com/SICKAG/SICK-Sensor-Starter-Kits | Markdown + mkdocs |
| Starter kits site | https://sickag.github.io/SICK-Sensor-Starter-Kits | HTML docs |
| AppSpace org | https://github.com/SICKAppSpaceCodingStarterKit | ~50 repos |
| Key SDK docs | SICK-AppSpace-SDK-Docs, SICK-App-Designer-Docs | AsciiDoc |

**Notable repos:** sick_scan_xd, sick_safetyscanners2, sick_safevisionary_ros2, ScanSegmentAPI, sick_line_guidance.

**Drift signals:** API changes, ROS driver updates, deprecated endpoints.

---

## Layer 5 — Cloud / Digital Services

| Service | URL | Notes |
| --- | --- | --- |
| SICK AssetHub | https://www.sick.com/us/en/catalog/digital-services-and-solutions/software/sick-assethub/ | Digital twin / asset management |
| Function Block Factory | https://fbf.cloud.sick.com | IO-Link configurator |
| LiveConnect | Referenced in KB | Remote device access |

Local: AssetHub datasheet in `../pdfs/datasheets/`.

---

## Layer 6 — Desktop Engineering Tools

| Tool | Documentation source |
| --- | --- |
| SOPAS ET | sick.com product page + KB articles |
| Safety Designer | IM0064028 (local PDF) |
| Nova | KB + sick.com software catalog |
| SOPASair | Mobile variant, KB references |

SOPAS ET page: https://www.sick.com/cn/en/catalog/digital-services-and-solutions/software/sopas-engineering-tool/p/p367244

---

## IO-Link Ecosystem

| Resource | URL |
| --- | --- |
| IODD finder | https://ioddfinder.io-link.com/ |
| SICK IO-Link tech info | IM0077697 (local PDF) |
| PSS tech info | IM0079055 (local PDF) |

---

## Recommended crawl priority for Usuario 2

1. **P0:** Datasheets + W4 overview (ordering, SKUs)
2. **P0:** SIG200 Profinet + REST API (integration demo)
3. **P1:** IO-Link technical information (protocol entities)
4. **P1:** KB firmware/release articles (drift testing)
5. **P2:** Machine vision / safety overviews (breadth)
