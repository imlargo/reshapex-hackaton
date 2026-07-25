# Rehearsal Case

Our agent helps a service coordinator choose a safe triage action for a pump
using exact asset data, maintenance rules, and cited service guidance.

## Five answers

1. The coordinator loses 15–30 minutes cross-checking three sources; a wrong
   decision can cause downtime or unsafe intervention.
2. Demo input: asset ID plus one symptom selected from a short reliable list.
3. Output: shutdown / inspect / escalate, cited evidence, unresolved risk, and
   a work-order-ready next step.
4. A document chatbot summarizes manuals. This agent cross-checks the exact
   meter and component compatibility, grades evidence, and declines when the
   asset/symptom combination is unsupported.
5. Available now: CSV, manual, bulletin, DeepSeek key, Python/Streamlit skills;
   no live action API.

## Follow-ups

- Dangerous error: authorizing continued operation when a shutdown bulletin
  applies; the system must escalate/decline.
- Evidence shape: exact IDs/table values plus prose.
- Kill condition: if exact asset lookup and one cited result are not green at
  T+100, cut compatibility and demonstrate inspection triage only.
