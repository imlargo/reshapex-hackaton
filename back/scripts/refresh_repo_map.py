from __future__ import annotations

import argparse
from pathlib import Path

EXCLUDED_DIRS = {
    ".git",
    ".venv",
    "__pycache__",
    ".pytest_cache",
    ".ruff_cache",
    "node_modules",
    "dist",
    "build",
}
EXCLUDED_FILES = {"uv.lock"}


def build_map(root: Path, max_depth: int = 4) -> str:
    lines = ["# Repository Map", "", "Generated structural map; source remains in place.", ""]
    for path in sorted(root.rglob("*")):
        relative = path.relative_to(root)
        if any(part in EXCLUDED_DIRS for part in relative.parts):
            continue
        if len(relative.parts) > max_depth or path.name in EXCLUDED_FILES:
            continue
        suffix = "/" if path.is_dir() else ""
        lines.append(f"- `{relative.as_posix()}{suffix}`")
    lines.extend(
        [
            "",
            "## Entry points",
            "",
            "- UI: `app.py`",
            "- Runtime package: `src/agentsprint_starter/`",
            "- Deterministic smoke: `scripts/smoke.py`",
            "- Real-provider preflight: `scripts/real_preflight.py`",
            "- Sprint boot: `agentsprint/START_HERE.md`",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        default="agentsprint/REPOSITORY_MAP.md",
        help="Repository-relative output path.",
    )
    args = parser.parse_args()
    root = Path.cwd().resolve()
    output = (root / args.output).resolve()
    if root not in output.parents:
        raise SystemExit("Output must remain inside the repository.")
    output.write_text(build_map(root), encoding="utf-8")
    print(f"Updated {output.relative_to(root)}")


if __name__ == "__main__":
    main()
