from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

SECRET_FILE_NAMES = {".env", "secrets.toml", "credentials.json"}
TOKEN_PATTERNS = [
    re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b"),
    re.compile(r"\bAIza[A-Za-z0-9_-]{30,}\b"),
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
]


def main() -> int:
    tracked = subprocess.run(
        ["git", "ls-files", "-z", "--cached", "--others", "--exclude-standard"],
        check=True,
        capture_output=True,
    ).stdout.decode("utf-8").split("\0")
    failures: list[str] = []
    for raw_path in filter(None, tracked):
        path = Path(raw_path)
        if path.name in SECRET_FILE_NAMES:
            failures.append(f"tracked secret-shaped file: {raw_path}")
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        for pattern in TOKEN_PATTERNS:
            if pattern.search(text):
                failures.append(f"possible credential in: {raw_path}")
                break
    if failures:
        print("\n".join(f"FAILED: {failure}" for failure in failures))
        return 1
    print(f"OK: scanned {len(list(filter(None, tracked)))} tracked files; no secret pattern found.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
