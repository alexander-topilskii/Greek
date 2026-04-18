#!/usr/bin/env python3
"""Patch assemble_voice_lesson_*.py and build_voice_lesson_*.py for shifted line indices."""

from __future__ import annotations

import re
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]

# 0-based index of the first line containing `<a id="` when numeric slices were authored.
ANCHOR_LINE_BASE: dict[int, int] = {
    1: 25,
    2: 29,
    3: 25,
    4: 26,
    5: 22,
    6: 29,
    7: 29,
    8: 29,
    9: 29,
    10: 25,
    11: 33,
    12: 31,
    13: 31,
    14: 31,
    15: 26,
    16: 34,
    17: 28,
    18: 30,
    19: 30,
    20: 26,
}

OLD_SL_BLOCK = r"""    lines = digit_path.read_text(encoding="utf-8").splitlines()

    def sl(a: int, b: int) -> str:
        return "\n".join(lines[a:b]).rstrip()
"""


def strip_assemble_output_nav(lines: list[str]) -> list[str]:
    title_i = next(
        (i for i, l in enumerate(lines) if l.strip().startswith("ln(f\"# ") and "{mic}" in l),
        None,
    )
    if title_i is None:
        raise ValueError("no ln(f\"# title line")
    if title_i + 1 >= len(lines) or lines[title_i + 1].strip() != "ln()":
        raise ValueError("expected ln() after title")
    j = title_i + 2
    while j < len(lines):
        s = lines[j].strip()
        if s.startswith("ln(\"###") or s.startswith("ln(f\"###"):
            break
        j += 1
    else:
        raise ValueError("no ln(### block start")
    return lines[: title_i + 2] + lines[j:]


def patch_assemble(path: Path) -> None:
    m = re.search(r"assemble_voice_lesson_(\d+)\.py$", path.name)
    if not m:
        return
    n = int(m.group(1))
    base = ANCHOR_LINE_BASE[n]
    text = path.read_text(encoding="utf-8")
    if "_slice_shift" in text:
        print("skip (already patched)", path.name)
        return
    if OLD_SL_BLOCK not in text:
        raise SystemExit(f"OLD_SL_BLOCK not found in {path}")
    new_sl = (
        "    lines = digit_path.read_text(encoding=\"utf-8\").splitlines()\n"
        f"    ANCHOR_LINE_BASE = {base}\n"
        "    _cur_anchor = next(i for i, ln in enumerate(lines) if '<a id=\"' in ln)\n"
        "    _slice_shift = ANCHOR_LINE_BASE - _cur_anchor\n\n"
        "    def sl(a: int, b: int) -> str:\n"
        r'        return "\n".join(lines[a - _slice_shift : b - _slice_shift]).rstrip()'
        + "\n"
    )
    text = text.replace(OLD_SL_BLOCK, new_sl, 1)
    pl = text.splitlines()
    pl2 = strip_assemble_output_nav(pl)
    path.write_text("\n".join(pl2) + "\n", encoding="utf-8")
    print("patched", path.name)


def patch_build(path: Path) -> None:
    m = re.search(r"build_voice_lesson_(\d+)\.py$", path.name)
    if not m:
        return
    n = int(m.group(1))
    base = ANCHOR_LINE_BASE[n]
    text = path.read_text(encoding="utf-8")
    if "_line_shift" in text:
        print("skip (already patched)", path.name)
        return
    marker = '    L = DIG.read_text(encoding="utf-8").splitlines()\n'
    if marker not in text:
        raise SystemExit(f"L = DIG.read not found in {path}")
    insert = (
        marker
        + f"    ANCHOR_LINE_BASE = {base}\n"
        + "    _cur_anchor = next(i for i, ln in enumerate(L) if '<a id=\"' in ln)\n"
        + "    _line_shift = ANCHOR_LINE_BASE - _cur_anchor\n\n"
        + "    def _dl(n: int) -> str:\n"
        + "        return L[n - _line_shift]\n\n"
    )
    text = text.replace(marker, insert, 1)
    text = re.sub(r"\bL\[(\d+)\]", r"_dl(\1)", text)
    path.write_text(text, encoding="utf-8")
    print("patched", path.name)


def main() -> None:
    scripts = REPO / "scripts"
    for path in sorted(scripts.glob("assemble_voice_lesson_*.py")):
        patch_assemble(path)
    for path in sorted(scripts.glob("build_voice_lesson_*.py")):
        patch_build(path)


if __name__ == "__main__":
    main()
