# Demo Cases

| Case | Input/evidence | Expected behavior | Automated/manual proof | Result |
| --- | --- | --- | --- | --- |
| Grounded happy path | adequate matching evidence | cited structured result | `scripts/smoke.py`; real preflight | deterministic green |
| Missing data | no relevant evidence | low confidence / insufficient / next evidence action | `test_missing_evidence...` | automated green |
| Contradictory evidence | two incompatible sources | expose uncertainty; do not overclaim | `test_contradictory_evidence...` | automated green |
| Tool failure/timeout | explicit tool error or timeout | honest insufficient result or visible error | runner failure/timeout tests | automated green |
| Malformed result | invented ID/schema drift | one repair then stop | runner repair tests | automated green |
