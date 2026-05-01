#!/usr/bin/env python3
"""Build root index.html from Readme.md (styled landing for GitHub Pages)."""
from __future__ import annotations

import html
import re
import sys
from pathlib import Path

try:
    import markdown
except ImportError as e:
    raise SystemExit(
        "Need the `markdown` package. Install: pip install -r scripts/requirements-generate.txt"
    ) from e

SCRIPTS_DIR = Path(__file__).resolve().parent
REPO = SCRIPTS_DIR.parent


def _read_h1_title(md_text: str) -> str:
    """First # line -> document title (for <title> / header)."""
    for line in md_text.strip().splitlines():
        m = re.match(r"^#\s+(.+)$", line.strip())
        if m:
            return m.group(1).strip()
    return "Greek"


def _linkify_bare_urls(fragment: str) -> str:
    """Turn bare http(s) URLs in text into links without touching existing tags."""
    url_re = re.compile(r"https?://[^\s<>\"']+")

    def text_parts(s: str) -> list[str]:
        return re.split(r"(<[^>]+>)", s)

    out: list[str] = []
    for chunk in text_parts(fragment):
        if chunk.startswith("<"):
            out.append(chunk)
            continue
        pos = 0
        buf: list[str] = []
        for m in url_re.finditer(chunk):
            buf.append(chunk[pos : m.start()])
            raw = m.group(0)
            url = raw.rstrip(").,;]")
            tail = raw[len(url) :]
            buf.append(
                f'<a href="{html.escape(url)}" rel="noopener noreferrer">'
                f"{html.escape(url)}</a>{html.escape(tail) if tail else ''}"
            )
            pos = m.end()
        buf.append(chunk[pos:])
        out.append("".join(buf))
    return "".join(out)


def _strip_leading_title_and_breadcrumbs(md_text: str) -> str:
    """Remove first H1 and breadcrumbs line so the chrome does not duplicate them."""
    lines = md_text.splitlines()
    out: list[str] = []
    i = 0
    if lines and re.match(r"^#\s+", lines[0].strip()):
        i = 1
        while i < len(lines) and not lines[i].strip():
            i += 1
    if i < len(lines) and re.match(
        r"^\*\*Хлебные крошки:\*\*", lines[i].strip()
    ):
        i += 1
        while i < len(lines) and not lines[i].strip():
            i += 1
    return "\n".join(lines[i:]).lstrip("\n")


def _ensure_lessons_heading_id(html_fragment: str) -> str:
    """Match in-repo anchor used in Readme quick links: (#-уроки)."""
    return re.sub(
        r"<h2>\s*📘\s*Уроки\s*</h2>",
        '<h2 id="-уроки">📘 Уроки</h2>',
        html_fragment,
        count=1,
    )


def write_index_html(repo_root: Path | None = None) -> Path:
    root = repo_root or REPO
    readme = root / "Readme.md"
    if not readme.is_file():
        raise FileNotFoundError(readme)

    raw = readme.read_text(encoding="utf-8")
    title_plain = _read_h1_title(raw)
    body_md = _strip_leading_title_and_breadcrumbs(raw)

    md = markdown.Markdown(
        extensions=["tables", "fenced_code", "nl2br"],
        output_format="html",
    )
    body_html = md.convert(body_md)
    body_html = _ensure_lessons_heading_id(body_html)
    body_html = _linkify_bare_urls(body_html)

    safe_title = html.escape(title_plain)
    gh_url = "https://github.com/alexander-topilskii/Greek/blob/main/Readme.md"

    doc = f"""<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{safe_title}</title>
  <meta name="description" content="Материалы для изучения греческого языка — оглавление уроков." />
  <link rel="stylesheet" href="assets/readme-index.css" />
</head>
<body>
  <header class="site-header">
    <h1>{safe_title}</h1>
    <p class="tagline">Оглавление репозитория: уроки, ссылки и веб-версия учебных страниц.</p>
    <div class="meta">
      <a href="{html.escape(gh_url)}">Исходный Readme на GitHub</a>
      <span aria-hidden="true">·</span>
      <span>Тот же контент, что в <code>Readme.md</code></span>
    </div>
  </header>
  <div class="page-wrap">
    <article class="readme-body" aria-label="Содержимое Readme">
{body_html}
    </article>
  </div>
  <footer class="site-footer">
    Сгенерировано из <code>Readme.md</code> · правьте Markdown, затем <code>python scripts/generate_index_html.py</code>
  </footer>
</body>
</html>
"""

    out = root / "index.html"
    out.write_text(doc, encoding="utf-8")
    return out


def main() -> None:
    path = write_index_html()
    print(f"Wrote {path.relative_to(REPO)}")


if __name__ == "__main__":
    main()
