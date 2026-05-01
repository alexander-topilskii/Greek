#!/usr/bin/env python3
"""Create missing book/pages/lesson_N/digitized/K.md using Tesseract OCR on raw/K.png.

Skips K.md if it already exists (preserves hand-curated pages).
Requires: tesseract, traineddata ell+eng (brew install tesseract tesseract-lang).
"""
from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
BOOK_PAGES = REPO / "book" / "pages"


def ocr_png(png: Path) -> str:
    r = subprocess.run(
        ["tesseract", str(png), "stdout", "-l", "ell+eng"],
        capture_output=True,
        text=True,
        timeout=180,
        check=False,
    )
    if r.returncode != 0:
        return f"(OCR failed: {r.stderr.strip() or 'unknown'})\n"
    return r.stdout or ""


def write_digitized(lesson_num: int, page: int, png: Path, text: str) -> None:
    folder = BOOK_PAGES / f"lesson_{lesson_num}"
    dig = folder / "digitized"
    dig.mkdir(parents=True, exist_ok=True)
    out = dig / f"{page}.md"
    content_name = f"content_{lesson_num}.md"
    body = text.strip()
    if not body:
        body = "_(κενό αποτέλεσμα OCR — δείτε το σκανάρισμα.)_"

    md = f"""# 📄 Σελίδα {page}

**[🏠 Readme](https://alexander-topilskii.github.io/Greek/) → [📘 lesson_{lesson_num}](../) → [✨ digitized](.) → 📄 `{page}.md`**

| ⚡ Быстрые ссылки    |                             |
|---------------------|-----------------------------|
| 📑 Оглавление урока | [{content_name}](../{content_name}) |
| 📁 Исходник (скан)  | [{page}.png](../raw/{page}.png)     |

*Источник: σελίδα {page}, «Ελληνικά Α΄». Μηχανική μεταγραφή (Tesseract, ell+eng) από `raw/{page}.png` — ελέγξτε έναντι του σκαναρίσματος.*

---

## Κείμενο (OCR)

{body}
"""
    out.write_text(md, encoding="utf-8")


def main() -> None:
    only_lesson: int | None = None
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        only_lesson = int(sys.argv[1])

    lesson_dirs = sorted(
        [p for p in BOOK_PAGES.iterdir() if p.is_dir() and re.match(r"^lesson_\d+$", p.name)],
        key=lambda p: int(p.name.split("_")[1]),
    )
    created = 0
    skipped = 0
    for d in lesson_dirs:
        n = int(d.name.split("_")[1])
        if only_lesson is not None and n != only_lesson:
            continue
        raw = d / "raw"
        if not raw.is_dir():
            continue
        for png in sorted(raw.glob("*.png"), key=lambda p: int(p.stem)):
            m = re.match(r"^(\d+)\.png$", png.name)
            if not m:
                continue
            page = int(m.group(1))
            out_md = d / "digitized" / f"{page}.md"
            if out_md.is_file():
                skipped += 1
                continue
            txt = ocr_png(png)
            write_digitized(n, page, png, txt)
            created += 1
            print(f"+ lesson_{n} page {page}")

    print(f"Done: created {created}, skipped existing {skipped}")


if __name__ == "__main__":
    main()
