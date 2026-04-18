#!/usr/bin/env python3
"""Apply verified page-number renames for book/pages/lesson_*/raw/*.png (two-phase)."""
from __future__ import annotations

import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "modules" / "pages"

# (folder name, unique filename substring) -> page int
# Substrings match Screenshot*... or exact names like 14.png
MAP: dict[tuple[str, str], int] = {
    ("lesson 1", "14.png"): 14,
    ("lesson 1", "15.png"): 15,
    ("lesson 1", "6.10.18"): 16,
    ("lesson 1", "6.10.23"): 17,
    ("lesson 1", "6.10.28"): 18,
    ("lesson 1", "6.10.34"): 19,
    ("lesson 1", "6.10.42"): 20,
    ("lesson 1", "6.10.47"): 21,
    ("lesson 1", "6.10.53"): 22,
    ("lesson 2", "7.13.51"): 24,
    ("lesson 2", "7.13.59"): 25,
    ("lesson 2", "7.14.06"): 26,
    ("lesson 2", "7.14.13"): 27,
    ("lesson 2", "7.14.18"): 28,
    ("lesson 2", "7.14.23"): 29,
    ("lesson 2", "7.14.29"): 30,
    ("lesson 2", "7.14.36"): 31,
    ("lesson 2", "7.14.40"): 32,
    ("lesson 2", "7.14.46"): 33,
    ("lesson 2", "7.14.51"): 34,
    ("lesson 2", "7.14.57"): 35,
    ("lesson 2", "7.15.01"): 36,
    ("lesson 2", "7.15.06"): 37,
    ("lesson 3", "7.18.12"): 38,
    ("lesson 3", "7.18.16"): 39,
    ("lesson 3", "7.18.22"): 40,
    ("lesson 3", "7.18.25"): 41,
    ("lesson 3", "7.18.34"): 42,
    ("lesson 3", "7.18.42"): 43,
    ("lesson 3", "7.18.47"): 44,
    ("lesson 3", "7.18.53"): 45,
    ("lesson 3", "7.18.57"): 46,
    ("lesson 3", "7.19.01"): 47,
    ("lesson 4", "4.22.38"): 48,
    ("lesson 4", "4.22.46"): 49,
    ("lesson 4", "4.22.51"): 50,
    ("lesson 4", "4.22.57"): 51,
    ("lesson 4", "4.23.00"): 52,
    ("lesson 4", "4.23.05"): 53,
    ("lesson 4", "4.23.10"): 54,
    ("lesson 4", "4.23.19"): 55,
    ("lesson 4", "4.23.25"): 56,
    ("lesson 4", "4.23.35"): 57,
    ("lesson 4", "4.23.44"): 58,
}


def main() -> None:
    staging = ROOT / ".rename_staging_pages"
    staging.mkdir(exist_ok=True)
    moves: list[tuple[Path, Path]] = []

    for (folder, needle), page in MAP.items():
        d = ROOT / folder
        if needle.endswith(".png"):
            matches = [d / needle] if (d / needle).is_file() else []
        else:
            matches = list(d.glob(f"Screenshot*{needle}*.png"))
        if len(matches) != 1:
            raise SystemExit(f"Expected 1 file for {folder}/{needle!r}, got {matches!r}")
        src = matches[0]
        dest = d / f"{page}.png"
        moves.append((src, dest))

    # Phase 1 -> staging
    tmp_paths: list[tuple[Path, Path]] = []
    for i, (src, dest) in enumerate(moves):
        tmp = staging / f"_{i:04d}.png"
        shutil.move(src, tmp)
        tmp_paths.append((tmp, dest))

    # Phase 2 -> final names
    for tmp, dest in tmp_paths:
        if dest.exists():
            dest.unlink()
        shutil.move(tmp, dest)

    staging.rmdir()
    print(f"Renamed {len(moves)} files under {ROOT}")


if __name__ == "__main__":
    main()
