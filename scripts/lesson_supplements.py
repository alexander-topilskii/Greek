"""Определения и генерация дополнительных HTML-страниц урока (конспект, практика).

Используется из `generate_book_lesson_content_md.py`. Для любого номера урока N при
наличии исходного Markdown в `lesson_N/<subdir>/<stem>_N.md` записывает
`<subdir>/<stem>_N.html` с общей версткой, крошками и ссылкой на хаб content_N.html.

Зависимость: пакет `markdown` (см. `scripts/requirements-generate.txt`).
"""
from __future__ import annotations

import html
import textwrap
from dataclasses import dataclass
from pathlib import Path

try:
    import markdown as _markdown
except ImportError:
    _markdown = None  # type: ignore[assignment, misc]


def content_html_filename(lesson_num: int) -> str:
    return f"content_{lesson_num}.html"


@dataclass(frozen=True)
class LessonSupplement:
    """Подстраница урока: конспект, практика и т.д."""

    subdir: str
    stem: str
    default_h1: str
    article_class: str
    render_id: str
    table_heading: str
    links_row_primary: str
    md_intro_label: str

    def md_basename(self, lesson_num: int) -> str:
        return f"{self.stem}_{lesson_num}.md"

    def html_basename(self, lesson_num: int) -> str:
        return f"{self.stem}_{lesson_num}.html"

    def relpath_to_html_from_lesson(self, lesson_num: int) -> str:
        return f"{self.subdir}/{self.html_basename(lesson_num)}"

    def path_md(self, lesson_folder: Path, lesson_num: int) -> Path:
        return lesson_folder / self.subdir / self.md_basename(lesson_num)

    def md_exists(self, lesson_folder: Path, lesson_num: int) -> bool:
        return self.path_md(lesson_folder, lesson_num).is_file()


SUPPLEMENT_ORDER: tuple[LessonSupplement, ...] = (
    LessonSupplement(
        subdir="essence",
        stem="essence",
        default_h1="Конспект",
        article_class="essence-section",
        render_id="essence-render",
        table_heading="📋 Конспект",
        links_row_primary="📋 Конспект",
        md_intro_label="Конспект",
    ),
    LessonSupplement(
        subdir="task",
        stem="task",
        default_h1="Практика и задания",
        article_class="task-section",
        render_id="task-render",
        table_heading="📝 Практика",
        links_row_primary="📝 Практика",
        md_intro_label="Практика (задания)",
    ),
)


def strip_first_atx_title(md_raw: str, default_title: str) -> tuple[str, str]:
    """Отделяет первый заголовок ATX `# …` для вывода в `<h1>`, остальное — в поток markdown."""
    lines = md_raw.splitlines()
    i = 0
    while i < len(lines) and not lines[i].strip():
        i += 1
    if i < len(lines) and lines[i].startswith("#"):
        title = lines[i].lstrip("#").strip()
        body = "\n".join(lines[i + 1 :]).lstrip("\n")
        return title or default_title, body
    return default_title, md_raw.lstrip()


def write_supplement_html(
    lesson_num: int,
    lesson_folder: Path,
    spec: LessonSupplement,
    *,
    generator_script: str = "generate_book_lesson_content_md.py",
) -> bool:
    """Пишет HTML рядом с исходным .md в spec.subdir. Возвращает True, если файл записан."""
    path_md = spec.path_md(lesson_folder, lesson_num)
    if not path_md.is_file():
        return False
    if _markdown is None:
        rp = spec.relpath_to_html_from_lesson(lesson_num)
        print(
            f"Warning: package `markdown` not installed — skip {rp!r}; install: pip install markdown"
        )
        return False

    raw = path_md.read_text(encoding="utf-8")
    title_vis, body_md = strip_first_atx_title(raw, spec.default_h1)
    body_html = _markdown.markdown(
        body_md,
        extensions=[
            "tables",
            "fenced_code",
        ],
    ).strip()

    rel_readme = "https://alexander-topilskii.github.io/Greek/"
    rel_pages = "../../"
    content_hub = content_html_filename(lesson_num)
    content_hub_href = "../" + content_hub
    md_fname = spec.md_basename(lesson_num)
    html_fname = spec.html_basename(lesson_num)
    target_dir = lesson_folder / spec.subdir
    target_dir.mkdir(parents=True, exist_ok=True)

    nav_html = f"""    <nav class="breadcrumbs" aria-label="Навигация">
      <a href="{html.escape(rel_readme)}">🏠 Readme</a>
      → <a href="{html.escape(rel_pages)}">book/pages</a>
      → <a href="{html.escape(content_hub_href)}">{html.escape(content_hub)}</a>
      → <span>📄 {html.escape(html_fname)}</span>
    </nav>
    <nav class="links-row" aria-label="Связанные страницы">
      <a href="{html.escape(content_hub_href)}">📚 Страницы урока</a>
      <a href="{html.escape(md_fname)}">📄 Markdown-источник</a>
    </nav>
"""
    doc = f"""<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{html.escape(title_vis)} — урок {lesson_num}</title>
  <link rel="stylesheet" href="../../assets/lesson-content.css" />
</head>
<body>
  <div class="page-wrap">
{nav_html}    <h1>{html.escape(title_vis)}</h1>
    <p class="note">Источник рядом с этой страницей: <code>{html.escape(md_fname)}</code>. Пересборка скриптом <code>{html.escape(generator_script)}</code>.</p>

    <article class="{html.escape(spec.article_class)}">
      <div id="{html.escape(spec.render_id)}">
{textwrap.indent(body_html, "        ")}
      </div>
    </article>
  </div>
</body>
</html>
"""

    (target_dir / html_fname).write_text(doc, encoding="utf-8")
    return True
