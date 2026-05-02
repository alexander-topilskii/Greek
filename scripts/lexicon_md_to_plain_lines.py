#!/usr/bin/env python3
"""Convert lexicon/lexicon.md from Markdown tables to plain lines: «греч. - перевод».

Skips headings, rules (---), breadcrumbs, table headers and separator rows.
Each output line ends with two spaces so Markdown → HTML keeps line breaks.

Usage:
  python3 scripts/lexicon_md_to_plain_lines.py          # dry-run, show counts
  python3 scripts/lexicon_md_to_plain_lines.py --write  # overwrite all lexicon.md
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
BOOK_PAGES = REPO / "book/pages"

SEP_ROW = re.compile(r"^[-:\s|]+$")


def table_cells(line: str) -> list[str] | None:
    s = line.strip()
    if not s.startswith("|") or not s.endswith("|"):
        return None
    inner = s[1:-1]
    parts = inner.split("|")
    return [p.strip() for p in parts]


def is_header_row(a: str, b: str) -> bool:
    if "ελληνικά" in a and "по-русски" in b:
        return True
    if a == "Проверить" and not b:
        return True
    return False


def is_separator_cells(a: str, b: str) -> bool:
    return bool(SEP_ROW.match(a)) and bool(SEP_ROW.match(b))


def extract_pairs(lines: list[str]) -> list[str]:
    out: list[str] = []
    for line in lines:
        raw = line.rstrip("\n")
        stripped = raw.strip()
        if not stripped:
            continue
        if stripped.startswith("#"):
            continue
        if stripped == "---":
            continue
        if stripped.startswith("**[") and "Readme" in stripped:
            continue
        cells = table_cells(raw)
        if cells is None:
            continue
        if len(cells) < 2:
            continue
        a, b = "", ""
        if len(cells) == 2:
            a, b = cells[0], cells[1]
        else:
            # rare: extra pipes insidecell — join middle
            a, b = cells[0], cells[-1]

        if not a:
            continue
        if is_separator_cells(a, b):
            continue
        if is_header_row(a, b):
            continue

        if b:
            line_out = f"{a} - {b}"
        else:
            line_out = a
        # CommonMark hard line break for markdown→html
        out.append(line_out + "  ")
    return out


def convert_file(path: Path, *, write: bool) -> tuple[int, int]:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    pairs = extract_pairs(lines)
    new_body = "\n".join(pairs)
    if new_body and not new_body.endswith("\n"):
        new_body += "\n"
    if write:
        path.write_text(new_body, encoding="utf-8")
    return len(pairs), len(lines)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument(
        "--write",
        action="store_true",
        help="write converted text into each lexicon.md",
    )
    args = ap.parse_args()

    paths = sorted(BOOK_PAGES.glob("lesson_*/lexicon/lexicon.md"))
    if not paths:
        raise SystemExit(f"No lexicon.md under {BOOK_PAGES}")
    total_pairs = 0
    for p in paths:
        n_pairs, n_lines = convert_file(p, write=args.write)
        total_pairs += n_pairs
        print(f"{p.relative_to(REPO)}: {n_pairs} lines (from {n_lines} input lines)")
    print(f"Total: {total_pairs} glossary lines in {len(paths)} files")
    if not args.write:
        print("Dry-run only. Pass --write to overwrite files.")


if __name__ == "__main__":
    main()
