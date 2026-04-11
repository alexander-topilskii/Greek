#!/usr/bin/env python3
"""Regenerate book/pages/lesson_*/content.md from raw/*.png in each folder."""
from __future__ import annotations

import re
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
BOOK_PAGES = REPO / "book" / "pages"


def page_nums(folder: Path) -> list[int]:
    raw = folder / "raw"
    out: list[int] = []
    if not raw.is_dir():
        return out
    for f in raw.glob("*.png"):
        m = re.match(r"^(\d+)\.png$", f.name)
        if m:
            out.append(int(m.group(1)))
    return sorted(out)


def rel_raw_png(n: int) -> str:
    return f"raw/{n}.png"


def lesson_md_exists(n: int) -> bool:
    return (REPO / "modules" / f"lesson_{n}" / "lesson.md").is_file()


def write_content(lesson_num: int, folder: Path, nums: list[int]) -> None:
    rel_readme = "../../../Readme.md"
    rel_pages = "../"
    rel_lesson = f"../../../modules/lesson_{lesson_num}/lesson.md"
    lesson_cell = f"[lesson.md]({rel_lesson})" if lesson_md_exists(lesson_num) else "—"

    lines = [
        f"# 📚 Страницы учебника — урок {lesson_num}",
        "",
        f"**[🏠 Readme]({rel_readme}) → [📘 book/pages]({rel_pages}) → 📄 `content.md`**",
        "",
        "| ⚡ Быстрые ссылки |                                                          |",
        "|------------------|----------------------------------------------------------|",
        f"| 📘 Урок          | {lesson_cell:<56} |",
        "| 📁 Исходники     | [raw/](raw/)                                             |",
        "| ✨ Оцифровка     | [digitized/](digitized/)                                 |",
        "| 📑 Оглавление    | [К навигации](#lesson-pages-nav)                         |",
        "| 🖼 Просмотр       | [К превью](#lesson-pages-preview)                        |",
        "",
        '<a id="lesson-pages-nav"></a>',
        "",
        "## 🔢 Навигация по страницам",
        "",
    ]

    if not nums:
        lines.extend(
            [
                "Пока нет файлов `raw/*.png` — добавьте сканы страниц учебника в папку `raw/`.",
                "",
            ]
        )
    else:
        row: list[str] = []
        for i, n in enumerate(nums):
            row.append(f"[{n}]({rel_raw_png(n)})")
            if len(row) >= 8 or i == len(nums) - 1:
                lines.append("- " + " · ".join(row))
                row = []
        lines.append("")

    lines.extend(
        [
            '<a id="lesson-pages-preview"></a>',
            "",
            "## 🖼 Просмотр страниц",
            "",
        ]
    )
    if nums:
        lines.extend(
            [
                "Ниже — те же файлы из `raw/` в порядке номеров страницы (удобно листать сверху вниз).",
                "",
            ]
        )
        for n in nums:
            lines.extend(
                [
                    f"### Стр. {n}",
                    "",
                    f"![Страница {n}]({rel_raw_png(n)})",
                    "",
                ]
            )
    else:
        lines.extend(
            [
                "Здесь появятся встроенные превью после добавления `*.png` в папку `raw/`.",
                "",
            ]
        )

    folder.mkdir(parents=True, exist_ok=True)
    (folder / "content.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    lesson_dirs = sorted(
        [p for p in BOOK_PAGES.iterdir() if p.is_dir() and re.match(r"^lesson_\d+$", p.name)],
        key=lambda p: int(p.name.split("_")[1]),
    )
    for d in lesson_dirs:
        n = int(d.name.split("_")[1])
        write_content(n, d, page_nums(d))
    print(f"Updated {len(lesson_dirs)} content.md under {BOOK_PAGES}")


if __name__ == "__main__":
    main()
