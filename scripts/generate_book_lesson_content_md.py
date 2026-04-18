#!/usr/bin/env python3
"""Regenerate book/pages/lesson_*/content_{N}.md from raw/*.png in each folder.

Also writes content_{N}.html (user-facing hub: links, full-chapter MD, scan carousel, page list)
and runs generate_essence_html.generate_all() so essence_N.html and essence_voice_index.html
stay in sync before quick links are written."""
from __future__ import annotations

import html
import json
import re
from pathlib import Path

from generate_essence_html import generate_all

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


def essence_md_exists(folder: Path, lesson_num: int) -> bool:
    return (folder / f"essence_{lesson_num}" / f"essence_{lesson_num}.md").is_file()


def voice_lesson_md_exists(folder: Path, lesson_num: int) -> bool:
    return (folder / f"lesson_voice_{lesson_num}" / f"voice_lesson_{lesson_num}.md").is_file()


def content_filename(lesson_num: int) -> str:
    return f"content_{lesson_num}.md"


def content_html_filename(lesson_num: int) -> str:
    return f"content_{lesson_num}.html"


def lesson_digitized_md_exists(folder: Path, lesson_num: int) -> bool:
    return (folder / "lesson_digitized" / f"lesson_{lesson_num}_digitized.md").is_file()


def voice_lesson_html_exists(folder: Path, lesson_num: int) -> bool:
    return (folder / f"lesson_voice_{lesson_num}" / f"voice_lesson_{lesson_num}.html").is_file()


def essence_html_exists(folder: Path, lesson_num: int) -> bool:
    return (folder / f"essence_{lesson_num}.html").is_file()


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
    essence_name = f"essence_{lesson_num}.md"
    essence_rel = f"essence_{lesson_num}/essence_{lesson_num}.md"
    essence_cell = f"[{essence_name}]({essence_rel})" if essence_md_exists(folder, lesson_num) else None
    voice_lesson_rel = f"lesson_voice_{lesson_num}/voice_lesson_{lesson_num}.md"
    voice_lesson_html_rel = f"lesson_voice_{lesson_num}/voice_lesson_{lesson_num}.html"
    voice_lesson_exists = voice_lesson_md_exists(folder, lesson_num)
    voice_essence_html_rel = f"essence_{lesson_num}.html"
    out_name = content_filename(lesson_num)
    html_name = content_html_filename(lesson_num)

    lines = [
        f"# 📚 Страницы учебника — урок {lesson_num}",
        "",
        f"**[🏠 Readme]({rel_readme}) → [📘 book/pages]({rel_pages}) → 📄 `{out_name}`**",
        "",
        f"*Пользовательская точка входа: [`{html_name}`]({html_name}). Здесь (генерация) — ссылки на скан (`raw/*.png`) и оцифровку (`digitized/N.md`), если есть"
        + ("; при необходимости — конспект в `essence_*/essence_*.md`" if essence_cell else "")
        + ".*",
        "",
        "| ⚡ Быстрые ссылки |                                                          |",
        "|------------------|----------------------------------------------------------|",
        f"| 📘 Урок (modules) | {lesson_cell:<56} |",
    ]
    if essence_cell:
        lines.append(f"| 💎 Суть урока     | {essence_cell:<56} |")
    if essence_cell or voice_lesson_exists:
        voice_parts: list[str] = []
        if voice_lesson_exists:
            voice_parts.append(f"[voice_lesson_{lesson_num}.html]({voice_lesson_html_rel})")
            voice_parts.append(f"[voice_lesson_{lesson_num}.md]({voice_lesson_rel})")
        if essence_cell:
            voice_parts.append(f"[essence_{lesson_num}.html]({voice_essence_html_rel})")
        voice_parts.append("[индекс Voice](../essence_voice_index.html)")
        voice_cell = " · ".join(voice_parts)
        lines.append(f"| 🎙 Voice (HTML)   | {voice_cell:<56} |")
    lines.extend(
        [
        "| 📑 Оглавление    | [К навигации по страницам](#lesson-pages-nav)            |",
        "| 🖼 Превью        | [К превью страниц](#lesson-pages-preview)                |",
        "",
        ]
    )
    lines.extend(
        [
            '<a id="lesson-pages-nav"></a>',
            "",
            "## 🔢 Навигация по страницам",
            "",
        ]
    )

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


def write_content_html(lesson_num: int, folder: Path, nums: list[int]) -> None:
    """User-facing HTML hub: essence + voice + optional full-chapter MD, carousel, page list."""
    rel_readme = "../../../Readme.md"
    rel_pages = "../"
    rel_lesson = f"../../../modules/lesson_{lesson_num}/lesson.md"
    out_html = content_html_filename(lesson_num)
    essence_rel = f"essence_{lesson_num}.html"
    voice_html_rel = f"lesson_voice_{lesson_num}/voice_lesson_{lesson_num}.html"
    full_chapter_rel = f"lesson_digitized/lesson_{lesson_num}_digitized.md"

    lesson_cell = (
        f'<a href="{html.escape(rel_lesson)}">lesson.md</a>'
        if lesson_md_exists(lesson_num)
        else "—"
    )
    essence_cell = (
        f'<a href="{html.escape(essence_rel)}">{html.escape(essence_rel)}</a>'
        if essence_html_exists(folder, lesson_num)
        else "—"
    )
    voice_cell = (
        f'<a href="{html.escape(voice_html_rel)}">{html.escape(voice_html_rel)}</a>'
        if voice_lesson_html_exists(folder, lesson_num)
        else "—"
    )
    primary_links: list[str] = []
    if essence_html_exists(folder, lesson_num):
        primary_links.append(f'<a href="{html.escape(essence_rel)}">💎 Конспект</a>')
    if voice_lesson_html_exists(folder, lesson_num):
        primary_links.append(f'<a href="{html.escape(voice_html_rel)}">🎙 Практика</a>')
    primary_html = (
        f'    <nav class="links-row" aria-label="Быстрые переходы">\n      {" · ".join(primary_links)}\n    </nav>\n'
        if primary_links
        else ""
    )
    index_voice = "../essence_voice_index.html"

    pages_payload: list[dict[str, int | str | None]] = []
    for n in nums:
        item: dict[str, int | str | None] = {"n": n, "png": rel_raw_png(n)}
        item["md"] = f"digitized/{n}.md" if digitized_md_exists(folder, n) else None
        pages_payload.append(item)

    json_ld = json.dumps(pages_payload, ensure_ascii=False)

    full_chapter_block = ""
    if lesson_digitized_md_exists(folder, lesson_num):
        full_chapter_block = f"""    <section class="block full-chapter" aria-labelledby="full-chapter-h">
      <h2 id="full-chapter-h">📄 Вся глава (оцифровка)</h2>
      <p>Единый файл с текстом урока: <a href="{html.escape(full_chapter_rel)}">lesson_{lesson_num}_digitized.md</a></p>
    </section>
"""

    if nums:
        n0 = nums[0]
        if digitized_md_exists(folder, n0):
            md0_h = html.escape(f"digitized/{n0}.md")
            md0_part = f'<span id="scan-md-wrap"> · <a id="scan-link-md" href="{md0_h}">{n0}.md</a></span>'
        else:
            md0_part = (
                '<span id="scan-md-wrap" hidden> · <a id="scan-link-md" href="#"></a></span>'
            )
        carousel_block = f"""    <section class="block scan-carousel" aria-labelledby="scan-h">
      <h2 id="scan-h">🖼 Просмотр сканов</h2>
      <p class="note">Листайте страницы кнопками; ниже — полный список с ссылками на оцифровку по страницам.</p>
      <div class="scan-carousel__toolbar">
        <button type="button" id="scan-carousel-prev" aria-label="Предыдущая страница">← Назад</button>
        <span id="scan-carousel-counter" aria-live="polite"></span>
        <button type="button" id="scan-carousel-next" aria-label="Следующая страница">Вперёд →</button>
      </div>
      <figure class="scan-carousel__figure">
        <img id="scan-carousel-img" src="{html.escape(rel_raw_png(n0))}" alt="" width="800" height="1200" loading="eager" />
        <figcaption id="scan-carousel-caption" class="scan-carousel__caption"></figcaption>
      </figure>
      <p class="scan-carousel__open">
        Открыть файл: <a id="scan-link-png" href="{html.escape(rel_raw_png(n0))}">{n0}.png</a>{md0_part}
      </p>
      <script type="application/json" id="scan-pages-data">{json_ld}</script>
    </section>
"""
    else:
        carousel_block = """    <section class="block" aria-labelledby="scan-h">
      <h2 id="scan-h">🖼 Просмотр сканов</h2>
      <p class="empty-msg">Пока нет файлов <code>raw/*.png</code> — добавьте сканы в папку <code>raw/</code>.</p>
    </section>
"""

    page_list_items: list[str] = []
    for n in nums:
        png_h = html.escape(rel_raw_png(n))
        line = f'        <li><strong>{n}</strong> — <a href="{png_h}">{n}.png</a>'
        if digitized_md_exists(folder, n):
            dm = html.escape(f"digitized/{n}.md")
            line += f' · <a href="{dm}">{n}.md</a>'
        line += "</li>"
        page_list_items.append(line)
    if page_list_items:
        page_list_body = "\n".join(page_list_items)
        page_list_section = f"""    <section class="block" aria-labelledby="pages-h">
      <h2 id="pages-h">🔢 Страницы по номерам</h2>
      <ul class="page-list">
{page_list_body}
      </ul>
    </section>
"""
    else:
        page_list_section = ""

    doc = f"""<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{html.escape(f"Урок {lesson_num} — страницы учебника")}</title>
  <link rel="stylesheet" href="../assets/lesson-content.css" />
</head>
<body>
  <div class="page-wrap">
    <nav class="breadcrumbs" aria-label="Навигация">
      <a href="{html.escape(rel_readme)}">🏠 Readme</a>
      → <a href="{html.escape(rel_pages)}">book/pages</a>
      → <span>📄 {html.escape(out_html)}</span>
    </nav>
    <h1>📚 Страницы учебника — урок {lesson_num}</h1>
    <p class="note">Оглавление урока: материалы, просмотр сканов и оцифровка по страницам. Генерация из <code>{html.escape(content_filename(lesson_num))}</code>.</p>

{primary_html}    <table class="quick-table" role="presentation">
      <tbody>
        <tr><th>📘 Урок (modules)</th><td>{lesson_cell}</td></tr>
        <tr><th>💎 Конспект (HTML)</th><td>{essence_cell}</td></tr>
        <tr><th>🎙 Практика (HTML)</th><td>{voice_cell}</td></tr>
        <tr><th>🎙 Индекс Voice</th><td><a href="{html.escape(index_voice)}">essence_voice_index.html</a></td></tr>
      </tbody>
    </table>

{full_chapter_block}{carousel_block}{page_list_section}
  </div>
  <script src="../assets/scan-carousel.js" defer></script>
</body>
</html>
"""

    folder.mkdir(parents=True, exist_ok=True)
    (folder / out_html).write_text(doc, encoding="utf-8")


def main() -> None:
    generate_all()
    lesson_dirs = sorted(
        [p for p in BOOK_PAGES.iterdir() if p.is_dir() and re.match(r"^lesson_\d+$", p.name)],
        key=lambda p: int(p.name.split("_")[1]),
    )
    for d in lesson_dirs:
        n = int(d.name.split("_")[1])
        pnums = page_nums(d)
        write_content(n, d, pnums)
        write_content_html(n, d, pnums)
    print(f"Updated {len(lesson_dirs)} content_*.md and content_*.html under {BOOK_PAGES}")


if __name__ == "__main__":
    main()
