#!/usr/bin/env python3
"""Generate lesson HTML pages for GitHub Pages (copy button).

Sources:
- essence page: docs/ai_voice_promt.md (prompt block) + lesson_N/essence_N/essence_N.md
- voice lesson page: fixed roleplay prompt + lesson_N/lesson_voice_N/voice_lesson_N.md
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
ROLEPLAY_PROMPT = """Λειτούργησε ως αυστηρός δάσκαλος ελληνικών και συνεργάτης μου για πρακτική εξάσκηση.

Я новичок в греческом языке, поэтому мета-общение со мной веди на русском. У тебя две основные задачи: разыгрывать со мной диалоги по ролям и строго контролировать мою речь.

ПРАВИЛА ИСПРАВЛЕНИЯ ОШИБОК (КРИТИЧЕСКИ ВАЖНО):
1. Будь максимально краток. Никакой вежливости, похвалы и лишних слов.
2. Если в моей реплике нет ошибок — ничего не говори вне роли (просто ответь «ОК» или сразу продолжай диалог своей репликой).
3. Если ты видишь ошибку (в грамматике, лексике, порядке слов) — прерви роль и скажи ТОЛЬКО исправленный вариант. Никаких вступлений вроде «Правильно будет так...» или объяснений.
4. Переводи фразы на русский язык ТОЛЬКО если я скажу слово «Перевод» или «Translate».

ПРАВИЛА РОЛЕВОЙ ИГРЫ:
1. Я пришлю тебе сценарии (Ситуации). Я всегда играю Роль А, ты всегда играешь Роль Б.
2. Жди моей первой реплики, не начинай диалог сам (если по сценарию Роль А говорит первой).
3. Так как я новичок, говори короткими репликами, удобными для восприятия на слух, и используй строго лексику из чек-листа к ситуации. Не усложняй грамматику.

Мы будем переходить от одной ситуации к другой по моей команде (например, "Ситуация 1").

Вот сценарии для нашей практики:
"""


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


def build_page_html(
    *,
    lesson_num: int,
    page_kind: str,
    title_suffix: str,
    section_title: str,
    source_md_rel: str,
    prompt_title: str,
    source_md_text: str,
    voice_prompt: str,
    header_label: str,
    rel_readme: str,
    rel_agents: str,
    rel_prompt_link: str | None,
    rel_content_md: str,
    rel_index: str,
) -> str:
    """Single static HTML; links are relative to book/pages/lesson_N/*."""
    title = f"Урок {lesson_num} — {title_suffix}"
    import json

    prompt_j = json.dumps(voice_prompt, ensure_ascii=False)
    source_j = json.dumps(source_md_text, ensure_ascii=False)
    prompt_link_html = (
        f'<a href="{html_escape(rel_prompt_link)}">Промпт (md)</a>' if rel_prompt_link else "Промпт (в этой странице)"
    )
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
    .prompt-details {{
      margin-top: 0.5rem; border: 1px solid #d0d7de; border-radius: 8px; background: #fafbfc;
    }}
    .prompt-details summary {{
      cursor: pointer; padding: 0.65rem 1rem; font-size: 1.05rem; font-weight: 600;
      list-style: none;
    }}
    .prompt-details summary::-webkit-details-marker {{ display: none; }}
    .prompt-details summary::before {{
      content: "▸ "; display: inline-block; width: 1.1em; color: #57606a;
    }}
    .prompt-details[open] summary::before {{ content: "▾ "; }}
    .prompt-details[open] summary {{ border-bottom: 1px solid #e1e4e8; }}
    #prompt-block {{
      white-space: pre-wrap; background: #f6f8fa; padding: 1rem; margin: 0;
      font-size: 0.9rem; border-radius: 0 0 7px 7px;
    }}
    .hint {{ font-size: 0.85rem; color: #57606a; margin-top: 0.35rem; }}
  </style>
</head>
<body>
  <header class="nav">
    <strong>{html_escape(header_label)}</strong> · урок {lesson_num}
    <span style="display:block;margin-top:0.5rem;">
      <a href="{html_escape(rel_readme)}">Readme</a>
      <a href="{html_escape(rel_agents)}">agents</a>
      {prompt_link_html}
      <a href="{html_escape(rel_content_md)}">content_{lesson_num}.md</a>
      <a href="{html_escape(source_md_rel)}">{html_escape(source_md_rel.split('/')[-1])}</a>
      <a href="{html_escape(rel_index)}">Все уроки (индекс)</a>
    </span>
    <p style="margin: 0.75rem 0 0;">
      <button type="button" id="copy-all">Скопировать промпт + материал</button>
      <span id="copy-feedback" class="ok" aria-live="polite"></span>
    </p>
      <p class="hint">В буфер попадает текст промпта и полный markdown файла из раздела урока.</p>
  </header>

  <section>
    <details class="prompt-details">
      <summary>{html_escape(prompt_title)}</summary>
      <div id="prompt-block"></div>
    </details>
  </section>
  <section>
    <h2>{html_escape(section_title)} ({html_escape(source_md_rel)})</h2>
    <div id="essence-render"></div>
  </section>

  <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js" crossorigin="anonymous"></script>
  <script>
    const VOICE_PROMPT = {prompt_j};
    const SOURCE_MD = {source_j};

    document.getElementById("prompt-block").textContent = VOICE_PROMPT;
    if (typeof marked !== "undefined") {{
      document.getElementById("essence-render").innerHTML = marked.parse(SOURCE_MD);
    }} else {{
      document.getElementById("essence-render").innerHTML = "<pre>" + SOURCE_MD.replace(/</g, "&lt;") + "</pre>";
    }}

    document.getElementById("copy-all").addEventListener("click", async () => {{
      const text = VOICE_PROMPT + "\\n\\n---\\n\\n" + SOURCE_MD;
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


def write_index_html(
    essence_entries: list[tuple[int, str]],
    voice_entries: list[tuple[int, str]],
) -> None:
    """Entries are (lesson_num, relative_path_from_book_pages)."""
    essence_map = {n: rel for n, rel in essence_entries}
    voice_map = {n: rel for n, rel in voice_entries}
    rows = []
    lesson_nums = sorted(set(essence_map) | set(voice_map))
    for n in lesson_nums:
        essence_rel = essence_map.get(n)
        voice_rel = voice_map.get(n)
        essence_cell = (
            f'<a href="{html_escape(essence_rel)}">essence_{n}.html</a> · '
            f'<a href="lesson_{n}/essence_{n}/essence_{n}.md">essence_{n}.md</a>'
            if essence_rel
            else "—"
        )
        voice_cell = (
            f'<a href="{html_escape(voice_rel)}">voice_lesson_{n}.html</a> · '
            f'<a href="lesson_{n}/lesson_voice_{n}/voice_lesson_{n}.md">voice_lesson_{n}.md</a>'
            if voice_rel
            else "—"
        )
        rows.append(
            f"    <tr><td>{n}</td><td>{essence_cell}</td><td>{voice_cell}</td></tr>"
        )
    body = (
        "\n".join(rows)
        if rows
        else "    <tr><td colspan=\"3\">Нет сгенерированных страниц.</td></tr>"
    )
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
  <h1>🎙 Страницы Voice (HTML)</h1>
  <p>Генерируются скриптом <code>scripts/generate_essence_html.py</code> из <code>essence_N.md</code> и <code>voice_lesson_N.md</code>.</p>
  <table>
    <thead><tr><th>Урок</th><th>Essence HTML</th><th>Voice lesson HTML</th></tr></thead>
    <tbody>
{body}
    </tbody>
  </table>
</body>
</html>
"""
    INDEX_HTML.parent.mkdir(parents=True, exist_ok=True)
    INDEX_HTML.write_text(html, encoding="utf-8")


def generate_all() -> tuple[list[tuple[int, str]], list[tuple[int, str]]]:
    """Generate lesson HTML pages. Remove orphan html files."""
    voice = load_voice_prompt()
    essence_entries: list[tuple[int, str]] = []
    voice_entries: list[tuple[int, str]] = []
    lesson_dirs = sorted(
        [p for p in BOOK_PAGES.iterdir() if p.is_dir() and re.match(r"^lesson_\d+$", p.name)],
        key=lambda p: int(p.name.split("_")[1]),
    )
    for folder in lesson_dirs:
        n = int(folder.name.split("_")[1])
        emd = folder / f"essence_{n}" / f"essence_{n}.md"
        ehtml = folder / f"essence_{n}.html"
        if emd.is_file():
            md_text = emd.read_text(encoding="utf-8")
            ehtml.write_text(
                build_page_html(
                    lesson_num=n,
                    page_kind="essence",
                    title_suffix="Voice + конспект (essence)",
                    section_title=f"Конспект (essence_{n})",
                    source_md_rel=f"essence_{n}/essence_{n}.md",
                    prompt_title="Промпт (из docs/ai_voice_promt.md)",
                    source_md_text=md_text,
                    voice_prompt=voice,
                    header_label="🎙 Voice + essence",
                    rel_readme="../../../Readme.md",
                    rel_agents="../../../agents.md",
                    rel_prompt_link="../../../docs/ai_voice_promt.md",
                    rel_content_md=f"content_{n}.md",
                    rel_index="../essence_voice_index.html",
                ),
                encoding="utf-8",
            )
            # path from book/pages to lesson_N/essence_N.html
            essence_entries.append((n, f"lesson_{n}/essence_{n}.html"))
        else:
            if ehtml.is_file():
                ehtml.unlink()
        vmd = folder / f"lesson_voice_{n}" / f"voice_lesson_{n}.md"
        vhtml = folder / f"lesson_voice_{n}" / f"voice_lesson_{n}.html"
        if vmd.is_file():
            vhtml.parent.mkdir(parents=True, exist_ok=True)
            voice_md_text = vmd.read_text(encoding="utf-8")
            vhtml.write_text(
                build_page_html(
                    lesson_num=n,
                    page_kind="voice lesson",
                    title_suffix="Voice lesson (roleplay)",
                    section_title=f"Голосовой урок (voice_lesson_{n})",
                    source_md_rel=f"voice_lesson_{n}.md",
                    prompt_title="Промпт для ролевой практики (фиксированный)",
                    source_md_text=voice_md_text,
                    voice_prompt=ROLEPLAY_PROMPT,
                    header_label="🎙 Voice lesson",
                    rel_readme="../../../../Readme.md",
                    rel_agents="../../../../agents.md",
                    rel_prompt_link=None,
                    rel_content_md=f"../content_{n}.md",
                    rel_index="../../essence_voice_index.html",
                ),
                encoding="utf-8",
            )
            voice_entries.append((n, f"lesson_{n}/lesson_voice_{n}/voice_lesson_{n}.html"))
        else:
            if vhtml.is_file():
                vhtml.unlink()
    write_index_html(essence_entries, voice_entries)
    return essence_entries, voice_entries


def main() -> None:
    essence_entries, voice_entries = generate_all()
    print(
        "Generated "
        f"{len(essence_entries)} essence_*.html and "
        f"{len(voice_entries)} voice_lesson_*.html + {INDEX_HTML.relative_to(REPO)}"
    )


if __name__ == "__main__":
    main()
