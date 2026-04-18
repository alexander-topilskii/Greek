#!/usr/bin/env python3
"""Remove repo-navigation headers from Markdown: breadcrumbs and quick-link tables.

Skips root Readme.md. lesson_*_digitized.md: drop everything after H1 until first <a id=.
Other files: repeatedly strip Readme-style breadcrumb lines and following | tables.
"""

from __future__ import annotations

import argparse
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]


def strip_lesson_digitized(lines: list[str]) -> list[str] | None:
    if not lines or not lines[0].startswith("#"):
        return None
    anchor_i = next((i for i, ln in enumerate(lines) if '<a id="' in ln), None)
    if anchor_i is None:
        return None
    return [lines[0], ""] + lines[anchor_i:]


def strip_leading_nav_blocks(lines: list[str]) -> list[str]:
    if not lines or not lines[0].startswith("#"):
        return lines
    i = 1
    changed = False
    while i < len(lines):
        while i < len(lines) and not lines[i].strip():
            i += 1
        if i >= len(lines):
            break
        ln = lines[i]
        if ln.strip().startswith("**[") and "Readme" in ln and ("→" in ln or "\u2192" in ln):
            changed = True
            i += 1
            continue
        if ln.strip().startswith("|"):
            changed = True
            while i < len(lines) and lines[i].strip().startswith("|"):
                i += 1
            continue
        break
    if not changed:
        return lines
    return [lines[0], ""] + lines[i:]


def strip_quick_links_table_once(lines: list[str]) -> list[str]:
    """Remove the first markdown table whose header row mentions «Быстрые ссылки» (repo nav)."""
    for i, ln in enumerate(lines):
        if not ln.strip().startswith("|"):
            continue
        if "Быстрые ссылки" not in ln:
            continue
        j = i
        while j < len(lines) and lines[j].strip().startswith("|"):
            j += 1
        return lines[:i] + lines[j:]
    return lines


def process_file(path: Path, dry_run: bool) -> bool:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    rel = path.relative_to(REPO)
    new_lines: list[str] | None = None
    if rel.name.endswith("_digitized.md") and "lesson_digitized" in rel.parts:
        new_lines = strip_lesson_digitized(lines)
        if new_lines is None:
            return False
    else:
        cur = lines
        while True:
            nxt = strip_leading_nav_blocks(cur)
            if nxt != cur:
                cur = nxt
                continue
            nxt = strip_quick_links_table_once(cur)
            if nxt != cur:
                cur = nxt
                continue
            break
        if cur == lines:
            return False
        new_lines = cur

    ends_nl = text.endswith("\n")
    new_text = "\n".join(new_lines) + ("\n" if ends_nl else "")
    if dry_run:
        print(f"would strip: {rel}")
        return True
    path.write_text(new_text, encoding="utf-8")
    print(f"stripped: {rel}")
    return True


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    count = 0
    for path in sorted(REPO.rglob("*.md")):
        if ".git" in path.parts:
            continue
        if path.name == "Readme.md" and path.parent == REPO:
            continue
        if process_file(path, args.dry_run):
            count += 1
    print(f"done, touched {count} files")


if __name__ == "__main__":
    main()
