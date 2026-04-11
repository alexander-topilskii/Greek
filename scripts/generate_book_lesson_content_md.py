#!/usr/bin/env python3
"""Regenerate book/pages/lesson_*/content_{N}.md from raw/*.png in each folder."""
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


def digitized_md_exists(folder: Path, n: int) -> bool:
    p = folder / "digitized" / f"{n}.md"
    return p.is_file()


def lesson_md_exists(n: int) -> bool:
    return (REPO / "modules" / f"lesson_{n}" / "lesson.md").is_file()


def content_filename(lesson_num: int) -> str:
    return f"content_{lesson_num}.md"


def page_links_line(folder: Path, n: int) -> str:
    """Скан PNG + опционально оцифровка digitized/N.md."""
    parts = [f"[{n}.png]({rel_raw_png(n)})"]
    if digitized_md_exists(folder, n):
        parts.append(f"[{n}.md](digitized/{n}.md)")
    return " · ".join(parts)


def write_content(lesson_num: int, folder: Path, nums: list[int]) -> None:
    rel_readme = "../../../Readme.md"
    rel_pages = "../"
    rel_lesson = f"../../../modules/lesson_{lesson_num}/lesson.md"
    lesson_cell = f"[lesson.md]({rel_lesson})" if lesson_md_exists(lesson_num) else "—"
    out_name = content_filename(lesson_num)

    lines = [
        f"# 📚 Страницы учебника — урок {lesson_num}",
        "",
        f"**[🏠 Readme]({rel_readme}) → [📘 book/pages]({rel_pages}) → 📄 `{out_name}`**",
        "",
        "*Точка входа: здесь ссылки на файл скана (`raw/*.png`) и на оцифровку (`digitized/N.md`), если она есть.*",
        "",
        "| ⚡ Быстрые ссылки |                                                          |",
        "|------------------|----------------------------------------------------------|",
        f"| 📘 Урок (modules) | {lesson_cell:<56} |",
        "| 📑 Оглавление    | [К навигации по страницам](#lesson-pages-nav)            |",
        "| 🖼 Превью        | [К превью страниц](#lesson-pages-preview)                |",
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
        for n in nums:
            lines.append(f"- **{n}** — {page_links_line(folder, n)}")
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
                "Ниже — превью в порядке номеров страницы; перед картинкой — те же ссылки, что в навигации.",
                "",
            ]
        )
        for n in nums:
            sub = page_links_line(folder, n)
            lines.extend(
                [
                    f"### Стр. {n}",
                    "",
                    sub,
                    "",
                    f"![Страница {n}]({rel_raw_png(n)})",
                    "",
                ]
            )
    else:
        lines.extend(
            [
                "Здесь появятся превью после добавления `*.png` в папку `raw/`.",
                "",
            ]
        )

    folder.mkdir(parents=True, exist_ok=True)
    out_path = folder / out_name
    out_path.write_text("\n".join(lines), encoding="utf-8")
    legacy = folder / "content.md"
    if legacy.is_file() and legacy.resolve() != out_path.resolve():
        legacy.unlink()


def main() -> None:
    lesson_dirs = sorted(
        [p for p in BOOK_PAGES.iterdir() if p.is_dir() and re.match(r"^lesson_\d+$", p.name)],
        key=lambda p: int(p.name.split("_")[1]),
    )
    for d in lesson_dirs:
        n = int(d.name.split("_")[1])
        write_content(n, d, page_nums(d))
    print(f"Updated {len(lesson_dirs)} content_*.md under {BOOK_PAGES}")


if __name__ == "__main__":
    main()
