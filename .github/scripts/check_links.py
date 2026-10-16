#!/usr/bin/env python3
"""Light link checker for the portfolio hub.

Scans every Markdown file in the repository and verifies that local relative
links (paths that do not start with http://, https://, mailto:, or #) resolve
to an existing file or directory. Exits non-zero on the first broken link.

Run from the repository root: python .github/scripts/check_links.py
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")


def collect_markdown_files(root: Path) -> list[Path]:
    return sorted(
        p
        for p in root.rglob("*.md")
        if ".git" not in p.parts and "node_modules" not in p.parts
    )


def is_external_or_anchor(target: str) -> bool:
    return (
        target.startswith(("http://", "https://", "mailto:", "#", "tel:"))
        or target == ""
    )


def resolve_target(root: Path, source: Path, target: str) -> bool:
    # Strip optional heading anchor (#...) from the path portion.
    path_part = target.split("#", 1)[0]
    if not path_part:
        return True
    candidate = (source.parent / path_part).resolve()
    # Links that point outside this repository (e.g. ../ai-marketing-shared
    # sibling repos planned or already shipped) are intentional and are not
    # verifiable from this checkout.
    if not candidate.is_relative_to(root):
        return True
    try:
        return candidate.exists()
    except OSError:
        return False


def main() -> int:
    errors: list[str] = []
    checked = 0
    for md in collect_markdown_files(ROOT):
        rel = md.relative_to(ROOT)
        try:
            text = md.read_text(encoding="utf-8")
        except OSError as exc:
            errors.append(f"{rel}: cannot read ({exc})")
            continue
        for line_no, line in enumerate(text.splitlines(), start=1):
            for match in LINK_RE.finditer(line):
                target = match.group(1).strip()
                if is_external_or_anchor(target):
                    continue
                checked += 1
                if not resolve_target(ROOT, md, target):
                    errors.append(f"{rel}:{line_no}: broken link -> {target}")

    if errors:
        print("Broken links found:")
        for err in errors:
            print(f"  - {err}")
        print(f"Checked {checked} local links; {len(errors)} broken.")
        return 1

    print(f"OK: checked {checked} local links across markdown files.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
