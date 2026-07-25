from __future__ import annotations

import json
import sys
from pathlib import Path

import yaml

REQUIRED_PATHS = [
    "agentsprint/START_HERE.md",
    "agentsprint/AGENT_PLAYBOOK.md",
    "agentsprint/REPOSITORY_CONTEXT.md",
    "agentsprint/REPOSITORY_MAP.md",
    "agentsprint/CONTROL.md",
    "agentsprint/00_inbox/DAY_INSTRUCTIONS.md",
    "agentsprint/00_inbox/LINKS.md",
    "agentsprint/01_case/CASE.md",
    "agentsprint/01_case/BRAND.md",
    "agentsprint/01_case/SOURCE_MANIFEST.md",
    "agentsprint/01_case/FACTS_AND_CONSTRAINTS.md",
    "agentsprint/01_case/OPEN_QUESTIONS.md",
    "agentsprint/02_decisions/DECISION_QUEUE.md",
    "agentsprint/02_decisions/OPTION_PACKS.md",
    "agentsprint/02_decisions/DECISION_LOG.md",
    "agentsprint/02_decisions/SCORE_STRATEGY.md",
    "agentsprint/03_contracts/PRIMARY_JOURNEY.md",
    "agentsprint/03_contracts/ARCHITECTURE.md",
    "agentsprint/03_contracts/INTERFACES.md",
    "agentsprint/03_contracts/ACCEPTANCE.md",
    "agentsprint/04_workstreams/TEAM.md",
    "agentsprint/04_workstreams/BOARD.md",
    "agentsprint/04_workstreams/BRANCH_PLAN.md",
    "agentsprint/04_workstreams/tasks/TEMPLATE.md",
    "agentsprint/04_workstreams/handoffs/TEMPLATE.md",
    "agentsprint/04_workstreams/integration/MERGE_ORDER.md",
    "agentsprint/04_workstreams/integration/INTEGRATION_LOG.md",
    "agentsprint/05_knowledge/EVIDENCE_MAP.md",
    "agentsprint/06_validation/SCORECARD.md",
    "agentsprint/06_validation/TECHNICAL_CHECKLIST.md",
    "agentsprint/06_validation/DEMO_CASES.md",
    "agentsprint/06_validation/FAILURE_LOG.md",
    "agentsprint/07_demo/PITCH.md",
    "agentsprint/07_demo/RUNBOOK.md",
    "agentsprint/07_demo/JUDGE_QA.md",
    ".agents/skills/sprint-director/SKILL.md",
    ".agents/skills/sprint-director/agents/openai.yaml",
]


def main() -> int:
    root = Path.cwd()
    missing = [path for path in REQUIRED_PATHS if not (root / path).is_file()]
    if missing:
        print(json.dumps({"status": "failed", "missing": missing}, indent=2))
        return 1

    skill_path = root / ".agents/skills/sprint-director/SKILL.md"
    text = skill_path.read_text(encoding="utf-8")
    if not text.startswith("---\n") or "\n---\n" not in text[4:]:
        print("FAILED: sprint-director SKILL.md has invalid frontmatter boundaries.")
        return 1
    frontmatter_text = text.split("---", 2)[1]
    frontmatter = yaml.safe_load(frontmatter_text)
    if set(frontmatter) != {"name", "description"}:
        print("FAILED: skill frontmatter must contain only name and description.")
        return 1
    if frontmatter["name"] != "sprint-director":
        print("FAILED: skill name does not match its directory.")
        return 1

    openai_yaml = yaml.safe_load(
        (root / ".agents/skills/sprint-director/agents/openai.yaml").read_text(
            encoding="utf-8"
        )
    )
    default_prompt = openai_yaml.get("interface", {}).get("default_prompt", "")
    if "$sprint-director" not in default_prompt:
        print("FAILED: skill UI default prompt must mention $sprint-director.")
        return 1

    print(
        json.dumps(
            {
                "status": "ok",
                "required_files": len(REQUIRED_PATHS),
                "skill": frontmatter["name"],
                "portable_boot": "agentsprint/START_HERE.md",
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
