#!/usr/bin/env python3
"""Generate lesson HTML pages for GitHub Pages (copy button).

Sources:
- essence page: docs/promts/ai_voice_promt.md (prompt block) + lesson_N/essence_N/essence_N.md
- voice lesson page: fixed roleplay prompt + lesson_N/lesson_voice_N/voice_lesson_N.md
Run from repo root: python3 scripts/generate_essence_html.py
Also invoked from generate_book_lesson_content_md.py
"""
from __future__ import annotations

import re
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
BOOK_PAGES = REPO / "book" / "pages"
VOICE_PROMPT_MD = REPO / "docs" / "promts" / "ai_voice_promt.md"
ROLEPLAY_PROMPT = """Ρόλος:
Είσαι ένας αυστηρός, λακωνικός και ενεργητικός καθηγητής ελληνικών για ηχητική εξάσκηση (Voice Mode). Ο μαθητής σου είναι ρωσόφωνος αρχάριος. Τo έργο σου είναι να τον βοηθήσεις να εμπεδώσει το υλικό μέσω διαλόγου και αυστηρού ελέγχου.

### ΠΡΑВИЛА КОНТРОЛЯ И ОШИБОК (КРИТИЧЕСКИ ВАЖНО):
1. **Алгоритм исправления:** Если я ошибся (грамматика, артикль, окончание):
   - Скажи: «Όχι» или «Λάθος» + [Правильный вариант].
   - Скажи: «Επανάλαβε». Жди, пока я произнесу верно.
   - Сразу после этого дай похожее задание для закрепления.
2. **Отложенное повторение:** Запоминай фразы с ошибками. Через 2-3 реплики верни их в диалог (органично или как вопрос), чтобы проверить усвоение.
3. **Адекватность и вариативность (АНТИ-СКРИПТ):** - Категорически запрещено требовать дословного повторения фраз из учебника или чек-листа. 
   - Если мой ответ грамматически верен и смысл передан — **это не ошибка**. Не исправляй стиль или порядок слов, если они допустимы в языке.
   - Одобряй синонимы. Игнорируй несовпадение имен персонажей.
4. **Краткость:** В диалоге, если всё верно, **не говори «ОК»**, а сразу отвечай своей репликой по роли. Похвала — максимум одно слово: «Μπράβο».
5. **Перевод:** Переводи на русский ТОЛЬКО по команде «Перевод» или «Translate».

### ΠРАВИЛА РОЛЕВОЙ ИГРЫ:
1. **Выбор роли:** Перед каждой ситуацией кратко обрисуй её на русском и спроси: «Какую роль хочешь играть: Роль А или Роль Б?».
2. **Инициатива:** Если по сценарию твоя роль начинает первой — начинай. Если моя — жди.
3. **Реакция на смысл:** Отвечай на содержание моей фразы, а не на её соответствие учебнику. Если я импровизирую в рамках темы, продолжай играть роль, подстраиваясь под мой контекст.
4. **Подсказки:** Если я молчу или застрял:
   - Дай подсказку в виде 1-2 ключевых слов на греческом, из которых я могу собрать ответ.
   - Не выдавай ответ целиком, пока я не скажу: «Πες μου την απάντηση».

### СПЕЦИФИКА ГОЛОСОВОГО РЕЖИМА (VOICE MODE):
- **Ультра-краткость:** Твои реплики — максимум 1-2 коротких предложения.
- **Один шаг:** Только один вопрос или одна реплика за раз.
- **Чистая речь:** Никакого Markdown-форматирования (списков, жирного шрифта, скобок). Текст должен быть естественным для озвучки.
- **Контроль распознавания:** Если мой ввод распознан как бессмыслица, скажи на русском: «Не понял, повтори еще раз».
- **Фокус на слух:** Следи за четкостью окончаний (-ος, -η, -ο). Если я их «глотаю» — это ошибка.

### ИНСТРУКЦИЯ ПО ВЫПОЛНЕНИЮ:
Жди от меня текст урока и команду с номером ситуации (например, «Ситуация 1»). Как только получишь — предложи выбрать роль и начинай. Все инструкции на русском, практика — на греческом.
"""


def extract_voice_prompt_block(md: str) -> str:
    """Return text inside the first ```text ... ``` fence."""
    m = re.search(r"```text\n(.*?)```", md, re.DOTALL)
    if not m:
        raise ValueError("docs/promts/ai_voice_promt.md: не найден блок ```text ... ```")
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
    rel_content_html: str,
    rel_css: str,
    rel_book_pages: str,
    current_file_label: str,
) -> str:
    """Single static HTML; links are relative to book/pages/lesson_N/* or lesson_voice_N/*."""
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
  <link rel="stylesheet" href="{html_escape(rel_css)}" />
</head>
<body>
  <div class="page-wrap">
    <nav class="breadcrumbs" aria-label="Навигация">
      <a href="{html_escape(rel_readme)}">Readme</a>
      → <a href="{html_escape(rel_book_pages)}">book/pages</a>
      → <a href="{html_escape(rel_content_html)}">content_{lesson_num}.html</a>
      → <span>{html_escape(current_file_label)}</span>
    </nav>
    <h1>{html_escape(title)}</h1>
    <p class="note">{html_escape(header_label)}</p>

    <header class="app-header">
      <span class="voice-top-links">
        <a href="{html_escape(rel_readme)}">Оглавление (Readme)</a>
        <a href="{html_escape(rel_agents)}">agents</a>
        {prompt_link_html}
        <a href="{html_escape(rel_content_html)}">Страницы урока</a>
        <a href="{html_escape(source_md_rel)}">{html_escape(source_md_rel.split('/')[-1])}</a>
      </span>
      <p class="copy-row">
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
    <section class="essence-section">
      <h2>{html_escape(section_title)} ({html_escape(source_md_rel)})</h2>
      <div id="essence-render"></div>
    </section>
  </div>

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
                    prompt_title="Промпт (из docs/promts/ai_voice_promt.md)",
                    source_md_text=md_text,
                    voice_prompt=voice,
                    header_label=f"{chr(0x1F399)} Voice + конспект (essence)",
                    rel_readme="../../../Readme.md",
                    rel_agents="../../../agents.md",
                    rel_prompt_link="../../../docs/promts/ai_voice_promt.md",
                    rel_content_html=f"content_{n}.html",
                    rel_css="../assets/lesson-content.css",
                    rel_book_pages="../",
                    current_file_label=f"essence_{n}.html",
                ),
                encoding="utf-8",
            )
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
                    header_label=f"{chr(0x1F399)} Голосовой урок (roleplay)",
                    rel_readme="../../../../Readme.md",
                    rel_agents="../../../../agents.md",
                    rel_prompt_link=None,
                    rel_content_html=f"../content_{n}.html",
                    rel_css="../../assets/lesson-content.css",
                    rel_book_pages="../../",
                    current_file_label=f"voice_lesson_{n}.html",
                ),
                encoding="utf-8",
            )
            voice_entries.append((n, f"lesson_{n}/lesson_voice_{n}/voice_lesson_{n}.html"))
        else:
            if vhtml.is_file():
                vhtml.unlink()
    return essence_entries, voice_entries


def main() -> None:
    essence_entries, voice_entries = generate_all()
    print(
        "Generated "
        f"{len(essence_entries)} essence_*.html and "
        f"{len(voice_entries)} voice_lesson_*.html"
    )


if __name__ == "__main__":
    main()
