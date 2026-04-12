#!/usr/bin/env python3
"""Generate book/pages/lesson_N/essence_N.html — Voice prompt + essence for GitHub Pages (copy button).

Source of truth: docs/ai_voice_promt.md (prompt block) + essence_N.md
Run from repo root: python3 scripts/generate_essence_html.py
Also invoked from generate_book_lesson_content_md.py
"""
from __future__ import annotations

import re
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
BOOK_PAGES = REPO / "book" / "pages"
VOICE_PROMPT_MD = REPO / "docs" / "ai_voice_promt.md"
INDEX_HTML = BOOK_PAGES / "essence_voice_index.html"


def extract_voice_prompt_block(md: str) -> str:
    """Return text inside the first ```text ... ``` fence."""
    m = re.search(r"```text\n(.*?)```", md, re.DOTALL)
    if not m:
        raise ValueError("docs/ai_voice_promt.md: не найден блок ```text ... ```")
    return m.group(1).strip()


def load_voice_prompt() -> str:
    return extract_voice_prompt_block(VOICE_PROMPT_MD.read_text(encoding="utf-8"))


def html_escape(s: str) -> str:
    return (
        s.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def build_page_html(lesson_num: int, essence_md: str, voice_prompt: str) -> str:
    """Single static HTML; links relative to book/pages/lesson_N/essence_N.html"""
    title = f"Урок {lesson_num} — Voice + конспект (essence)"
    import json

    prompt_j = json.dumps(voice_prompt, ensure_ascii=False)
    essence_j = json.dumps(essence_md, ensure_ascii=False)
    return f"""<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html_escape(title)}</title>
  <style>
    :root {{ font-family: system-ui, sans-serif; line-height: 1.45; }}
    body {{ max-width: 52rem; margin: 0 auto; padding: 1rem 1.25rem 3rem; color: #1a1a1a; }}
    header.nav {{ border-bottom: 1px solid #ddd; padding-bottom: 0.75rem; margin-bottom: 1.25rem; }}
    header.nav a {{ margin-right: 0.75rem; }}
    button#copy-all {{
      cursor: pointer; padding: 0.45rem 0.9rem; font-size: 0.95rem;
      background: #0969da; color: #fff; border: none; border-radius: 6px;
    }}
    button#copy-all:hover {{ background: #0550ae; }}
    .ok {{ color: #1a7f37; font-size: 0.9rem; margin-left: 0.5rem; }}
    h2 {{ margin-top: 1.75rem; font-size: 1.15rem; }}
    #essence-render {{ overflow-x: auto; }}
    #essence-render table {{ border-collapse: collapse; width: 100%; }}
    #essence-render th, #essence-render td {{ border: 1px solid #ccc; padding: 0.35rem 0.5rem; }}
    #prompt-block {{
      white-space: pre-wrap; background: #f6f8fa; padding: 1rem; border-radius: 8px;
      border: 1px solid #d0d7de; font-size: 0.9rem;
    }}
    .hint {{ font-size: 0.85rem; color: #57606a; margin-top: 0.35rem; }}
  </style>
</head>
<body>
  <header class="nav">
    <strong>🎙 Voice + essence</strong> · урок {lesson_num}
    <span style="display:block;margin-top:0.5rem;">
      <a href="../../../Readme.md">Readme</a>
      <a href="../../../agents.md">agents</a>
      <a href="../../../docs/ai_voice_promt.md">Промпт (md)</a>
      <a href="content_{lesson_num}.md">content_{lesson_num}.md</a>
      <a href="essence_{lesson_num}.md">essence_{lesson_num}.md</a>
      <a href="../essence_voice_index.html">Все уроки (индекс)</a>
    </span>
    <p style="margin: 0.75rem 0 0;">
      <button type="button" id="copy-all">Скопировать промпт + конспект</button>
      <span id="copy-feedback" class="ok" aria-live="polite"></span>
    </p>
    <p class="hint">В буфер попадает греческий блок промпта из docs и полный markdown конспекта (как в essence_N.md).</p>
  </header>

  <section>
    <h2>Промпт (из docs/ai_voice_promt.md)</h2>
    <div id="prompt-block"></div>
  </section>
  <section>
    <h2>Конспект (essence_{lesson_num}.md)</h2>
    <div id="essence-render"></div>
  </section>

  <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js" crossorigin="anonymous"></script>
  <script>
    const VOICE_PROMPT = {prompt_j};
    const ESSENCE_MD = {essence_j};

    document.getElementById("prompt-block").textContent = VOICE_PROMPT;
    if (typeof marked !== "undefined") {{
      document.getElementById("essence-render").innerHTML = marked.parse(ESSENCE_MD);
    }} else {{
      document.getElementById("essence-render").innerHTML = "<pre>" + ESSENCE_MD.replace(/</g, "&lt;") + "</pre>";
    }}

    document.getElementById("copy-all").addEventListener("click", async () => {{
      const text = VOICE_PROMPT + "\\n\\n---\\n\\n" + ESSENCE_MD;
      try {{
        await navigator.clipboard.writeText(text);
        const el = document.getElementById("copy-feedback");
        el.textContent = "Скопировано.";
        setTimeout(() => {{ el.textContent = ""; }}, 2500);
      }} catch (e) {{
        alert("Не удалось скопировать: " + e);
      }}
    }});
  </script>
</body>
</html>
"""


def write_index_html(entries: list[tuple[int, str]]) -> None:
    """entries: (lesson_num, relative_path_from_book_pages)"""
    rows = []
    for n, rel in sorted(entries, key=lambda x: x[0]):
        rows.append(
            f'    <tr><td>{n}</td><td><a href="{html_escape(rel)}">essence_{n}.html</a> '
            f'· <a href="{html_escape(rel.replace(".html", ".md"))}">essence_{n}.md</a></td></tr>'
        )
    body = "\n".join(rows) if rows else "    <tr><td colspan=\"2\">Нет сгенерированных страниц.</td></tr>"
    html = f"""<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Индекс — Voice + essence</title>
  <style>
    body {{ font-family: system-ui, sans-serif; max-width: 42rem; margin: 2rem auto; padding: 0 1rem; }}
    table {{ border-collapse: collapse; width: 100%; }}
    th, td {{ border: 1px solid #ccc; padding: 0.4rem 0.6rem; text-align: left; }}
    th {{ background: #f6f8fa; }}
  </style>
</head>
<body>
  <p><a href="../../Readme.md">Readme</a> · <a href="../../docs/ai_voice_promt.md">Промпт Voice (md)</a></p>
  <h1>🎙 Страницы Voice + конспект (HTML)</h1>
  <p>Генерируются скриптом <code>scripts/generate_essence_html.py</code>. Источник правды — <code>essence_N.md</code>.</p>
  <table>
    <thead><tr><th>Урок</th><th>Страница</th></tr></thead>
    <tbody>
{body}
    </tbody>
  </table>
</body>
</html>
"""
    INDEX_HTML.parent.mkdir(parents=True, exist_ok=True)
    INDEX_HTML.write_text(html, encoding="utf-8")


def generate_all() -> list[tuple[int, str]]:
    """Generate essence_N.html for each lesson with essence_N.md. Remove orphan html."""
    voice = load_voice_prompt()
    entries: list[tuple[int, str]] = []
    lesson_dirs = sorted(
        [p for p in BOOK_PAGES.iterdir() if p.is_dir() and re.match(r"^lesson_\d+$", p.name)],
        key=lambda p: int(p.name.split("_")[1]),
    )
    for folder in lesson_dirs:
        n = int(folder.name.split("_")[1])
        emd = folder / f"essence_{n}.md"
        ehtml = folder / f"essence_{n}.html"
        if emd.is_file():
            md_text = emd.read_text(encoding="utf-8")
            ehtml.write_text(build_page_html(n, md_text, voice), encoding="utf-8")
            # path from book/pages to lesson_N/essence_N.html
            entries.append((n, f"lesson_{n}/essence_{n}.html"))
        else:
            if ehtml.is_file():
                ehtml.unlink()
    write_index_html(entries)
    return entries


def main() -> None:
    entries = generate_all()
    print(f"Generated {len(entries)} essence_*.html + {INDEX_HTML.relative_to(REPO)}")


if __name__ == "__main__":
    main()
