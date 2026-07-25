# SICK URL Patterns — Indexer Reference

Patterns discovered during corpus research (2026-07-24/25).

## PDF — Datasheets

```
https://www.sick.com/media/pdf/{d1}/{d2}/{d3}/dataSheet_{SKU}_{orderNo}_en.pdf
```

Example:
```
https://www.sick.com/media/pdf/7/17/117/dataSheet_WTB4S-3N2131_1042061_en.pdf
```

- `{d1}/{d2}/{d3}` — path shards derived from order number or internal ID
- `{SKU}` — type code (e.g. WTB4S-3N2131)
- `{orderNo}` — numeric order number (e.g. 1042061)

## PDF — Operating Instructions / Technical Information

```
https://www.sick.com/media/docs/{d1}/{d2}/{d3}/{type}_{name}_{lang}_im{8digits}.pdf
```

Types: `operating_instructions`, `technical_information`, `special_information`, `product_segment_overview`, `product_information`, `quickstart`, `online_help`

Document ID: `im` + 7 digits (displayed as IM########)

Examples:
```
.../operating_instructions_sig200_rest_api_en_im0084724.pdf
.../technical_information_photoelectric_sensors_sick_smart_sensors_io_link_en_im0077697.pdf
```

## PDF — Product Overviews

```
https://www.sick.com/media/productoverview/{d1}/{d2}/{d3}/productoverview_{family}_{id}_en.pdf
```

Example:
```
https://www.sick.com/media/productoverview/1/01/401/productoverview_W4_g577401_en.pdf
```

## Knowledge Base Articles

```
https://support.sick.com/sick-knowledgebase/article/?code=KA-{5digits}
```

Example: `KA-09480`, `KA-09665`, `KA-10741`

## Product ID Portal

```
https://pid.sick.com/{part_number}/{serial_number}
```

## Catalog Search

```
https://www.sick.com/us/en/search?text={part_number_or_keyword}
https://www.sick.com/{FAMILY_CODE}   # e.g. /W4
https://www.sick.com/{order_number}  # e.g. /1042040
```

## GitHub Raw Content

```
https://raw.githubusercontent.com/SICKAG/{repo}/{branch}/{path}
```

Default branches vary: `main` (Sensor Starter Kits) or `master` (SDK docs).

## Metadata extraction hints

| Field | Where to find |
| --- | --- |
| Order number | Datasheet filename, catalog page, ordering table |
| IM document ID | PDF filename suffix `_im########` |
| SKU / type code | Datasheet filename, product page title |
| Protocol | Operating instructions filename (profinet, ethernet_ip, io_link) |
| Firmware version | KB articles (KA-* release notes) |
| Product family | Product overview PDFs, W4/WTB naming |

## CDN alternate host

Some older links use:
```
https://cdn.sick.com/media/docs/...
```

Prefer `www.sick.com` URLs when both resolve.
