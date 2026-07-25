# Failure Log

| Timestamp | Case/run | Symptom | Root cause | Repair/cut | Regression proof | Owner |
| --- | --- | --- | --- | --- | --- | --- |
| pre-event | real preflight | cannot run | `LLM_API_KEY` unset | configure ignored `.env` | `scripts/real_preflight.py` | operator |
| pre-event | first verification | smoke import failed | project lacked build backend | add Hatch wheel configuration | smoke green | coordinator |
| pre-event | first verification | skill validator lacked YAML parser | validation dependency absent | add locked PyYAML dev dependency | skill valid | coordinator |
