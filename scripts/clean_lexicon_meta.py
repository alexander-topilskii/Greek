#!/usr/bin/env python3
"""Remove editor/meta parentheticals from lexicon table cells (one-off or batch)."""
from __future__ import annotations

import re
import sys
from pathlib import Path

# Ordered: longer/more specific first
META_PATTERNS: tuple[re.Pattern[str], ...] = (
    re.compile(
        r"\s*\(стр\.\s*[0-9–—]+[^)]*(?:\)|$)",
        re.IGNORECASE,
    ),
    re.compile(
        r"\s*\(в упр\.\s*[^)]+\)",
        re.IGNORECASE,
    ),
    re.compile(
        r"\s*\(заголовок[^)]*\)",
        re.IGNORECASE,
    ),
    re.compile(
        r"\s*\(фрагмент[^)]*\)",
        re.IGNORECASE,
    ),
    re.compile(
        r"\s*\(омограф[^)]*\)",
        re.IGNORECASE,
    ),
    re.compile(
        r"\s*\(иллюстр\.\s*[^)]+\)",
        re.IGNORECASE,
    ),
    re.compile(
        r"\s*\(пример[^)]*\)",
        re.IGNORECASE,
    ),
    re.compile(
        r"\s*\(имя[^)]*\)",
        re.IGNORECASE,
    ),
    re.compile(
        r"\s*\(фамилия\)",
    ),
    re.compile(
        r"\s*\(рубрика\)",
    ),
    re.compile(
        r"\s*\(вывеска\)",
    ),
    re.compile(
        r"\s*\(название[^)]*\)",
    ),
    re.compile(
        r"\s*\(марка\)",
    ),
    re.compile(
        r"\s*\(метафора[^)]*\)",
    ),
    re.compile(
        r"\s*\(игра[^)]*\)",
    ),
    re.compile(
        r"\s*\(ном\.\)",
    ),
    re.compile(
        r"\s*\(3 л\.\)",
    ),
    re.compile(
        r"\s*\(варианты\)",
    ),
    re.compile(
        r"\s*\(контекст\)",
    ),
    re.compile(
        r"\s*\(о\)\s*",
    ),
    re.compile(
        r"\s*\(т\)\s*",
    ),
    re.compile(
        r"\s*\(в задании\)",
    ),
    re.compile(
        r"\s*\(в блоке[^)]*\)",
    ),
    re.compile(
        r"\s*\(к упр\.\s*[^)]+\)",
    ),
    re.compile(r"\s*\(стиль\)"),
    re.compile(
        r"\s*\(заголовки[^)]*\)",
        re.IGNORECASE,
    ),
    re.compile(r"\s*\(к вам\)"),
    re.compile(r"\s*\(вариант\)", re.IGNORECASE),
    re.compile(
        r"\s*\(предлог[^)]*\)",
    ),
    re.compile(r"\s*\(аудио\)", re.IGNORECASE),
    re.compile(r"\s*\(мнемоника[^)]*\)"),
    re.compile(r"\s*\(облачка[^)]*\)"),
    re.compile(r"\s*\(блок[^)]*\)"),
    re.compile(r"\s*\(вы\)", re.IGNORECASE),
    re.compile(
        r"\s*\(после [^)]+\)",
    ),
    re.compile(r"\s*\(район\)", re.IGNORECASE),
    re.compile(r"\s*\(разг\.\)"),
    re.compile(r"\s*\(предмет\)", re.IGNORECASE),
    re.compile(r"\s*\(на коллаже\)", re.IGNORECASE),
    re.compile(
        r"\s*\(кит\.\s*[^)]+\)",
    ),
    re.compile(
        r"\s*\(в вузе\)",
    ),
    re.compile(
        r"\s*\(в диалоге\)",
    ),
)


NUM_EXERCISE = re.compile(r"\s*\([0-9]+[.][0-9][^)]*\)")


def clean_table_row(line: str) -> str:
    s = line
    for p in META_PATTERNS:
        s = p.sub("", s)
    s = NUM_EXERCISE.sub("", s)
    s = re.sub(r"  +", " ", s)
    s = re.sub(r"\s+\|", " |", s)
    return s


def main() -> None:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else None
    if not path or not path.is_file():
        print("Usage: clean_lexicon_meta.py <path/to/lexicon.md>", file=sys.stderr)
        sys.exit(1)
    text = path.read_text(encoding="utf-8")
    out: list[str] = []
    for line in text.splitlines(keepends=True):
        raw = line.rstrip("\n\r")
        if raw.lstrip().startswith("|") and raw.count("|") >= 2:
            raw = clean_table_row(raw)
            out.append(raw + "\n")
        else:
            out.append(line)
    path.write_text("".join(out), encoding="utf-8")


if __name__ == "__main__":
    main()
