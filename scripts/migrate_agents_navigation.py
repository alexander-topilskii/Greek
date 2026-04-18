#!/usr/bin/env python3
"""Patch agents.md: navigation rules; run from repo root: python3 scripts/migrate_agents_navigation.py"""
from __future__ import annotations

from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
HOUSE = chr(0x1F3E0)
BOOKS = chr(0x1F4DA)
GEM = chr(0x1F48E)
MIC = chr(0x1F399)


def main() -> None:
    path = REPO / "agents.md"
    t = path.read_text(encoding="utf-8")
    a = t.index(f"[{HOUSE} Readme](Readme.md)")
    b = t.index("\n## 1.")
    new_intro = (
        "Правила для всех `.md` в репозитории. **Крошки и таблица «быстрые ссылки» в шапке — только у корневого "
        "[Readme.md](Readme.md).** В остальных файлах после `# …` сразу содержание (при необходимости курсив-ввод), "
        "без навигации по репозиторию; читательские переходы — в HTML (`content_N.html`, при наличии `essence_N.html` и voice HTML).\n\n"
        "Куда смотреть: [Readme.md](Readme.md) · "
        "[lesson-extraction-from-textbook.md](docs/lesson-extraction-from-textbook.md) · "
        "[voice-lesson-from-digitized.md](docs/voice-lesson-from-digitized.md) · "
        "[page-screenshot-renaming.md](docs/page-screenshot-renaming.md)\n\n"
    )
    t = t[:a] + new_intro + t[b + 1 :]

    c = t.index("\n## 2.")
    d = t.index("\n## 5.")
    new_234 = f"""## 2. Без шапки-навигации в Markdown (кроме корневого Readme)

- Не добавляй строку хлебных крошек `**[{HOUSE} Readme](...) → …**`.
- Не добавляй двухколоночную таблицу «быстрые ссылки» на другие файлы репозитория сразу под заголовком.
- Не добавляй в `lesson_*_digitized.md` блок «## … Навигация по разделам» со списком якорей по главе.
- Исключение: **[Readme.md](Readme.md)** в корне — там сохраняются оглавление и таблица уроков.
- Таблицы **внутри** учебного текста (спряжения, лексика) не считаются навигацией и допустимы.

## 3. Вводный абзац

- Сразу после `#` можно один короткий курсив с контекстом (*источник страницы, тема*), без таблиц.

## 4. Разделы со ссылками (содержание, не «хром» сайта)

- Разделы вроде `## {BOOKS} Материалы` с предметными ссылками допустимы, если это часть материала, а не дублирование шапки сайта.

"""
    t = t[:c] + "\n" + new_234 + t[d:]

    old_b1 = (
        "- В `Readme.md` одна колонка: ссылка на **`content_{N}.html`** как точку входа по уроку для читателя "
        "(`lesson_0` … `lesson_20`). Файл **`content_{N}.md`** пересобирается тем же скриптом, что и HTML "
        "(`scripts/generate_book_lesson_content_md.py`), и служит источником/синхронным дублем для диффов и превью "
        "в репозитории; в пользовательской навигации используйте HTML."
    )
    new_b1 = (
        "- В `Readme.md` одна колонка: ссылка на **`content_{N}.html`** как точку входа по уроку для читателя "
        "(`lesson_0` … `lesson_20`). Файл **`content_{N}.md`** пересобирается тем же скриптом, что и HTML "
        "(`scripts/generate_book_lesson_content_md.py`), и служит сырьём для диффов; в пользовательской навигации используйте HTML."
    )
    old_b2 = (
        "- Ссылки на сканы (`raw/*.png`), оцифровки (`digitized/N.md`), при наличии — **`lesson_digitized/lesson_N_digitized.md`**, "
        "конспект и voice задаются **внутри** сгенерированного `content_N.html` / `content_N.md`, не дублируются отдельными колонками в Readme."
    )
    new_b2 = (
        "- Ссылки на сканы (`raw/*.png`), оцифровки (`digitized/N.md`), при наличии — **`lesson_digitized/lesson_N_digitized.md`**, "
        "конспект и voice задаются **внутри** `content_N.html` / минимального `content_N.md`, не дублируются отдельными колонками в Readme."
    )
    old_p = (
        "на конспект и файлы репозитория (см. [docs/lesson-extraction-from-textbook.md](docs/lesson-extraction-from-textbook.md) §3.1)."
    )
    new_p = (
        "на конспект и файлы репозитория (см. [docs/lesson-extraction-from-textbook.md](docs/lesson-extraction-from-textbook.md))."
    )
    old_s = (
        f"При наличии файла скрипт регенерации `content_N.md` / `content_N.html` добавит строки «{GEM} Суть урока» и «{MIC} Voice (HTML)» в Markdown "
        "и обновит сгенерированный **`essence_N.html`**"
    )
    new_s = "При наличии файла скрипт регенерации `content_N.md` / `content_N.html` обновляет **`essence_N.html`**"
    old_b4 = (
        "- Опционально **`lesson_voice_N/voice_lesson_N.md`** — раздаточный материал для разговорной отработки **по единой оцифровке** "
        "`lesson_digitized/lesson_N_digitized.md`: чеклист, структура папки, промпт и ссылка из сгенерированного оглавления "
        "(`content_N.html` / `content_N.md`) — [docs/voice-lesson-from-digitized.md](docs/voice-lesson-from-digitized.md)."
    )
    new_b4 = (
        "- Опционально **`lesson_voice_N/voice_lesson_N.md`** — раздаточный материал для разговорной отработки **по единой оцифровке** "
        "`lesson_digitized/lesson_N_digitized.md`: чеклист, структура папки, промпт — [docs/voice-lesson-from-digitized.md](docs/voice-lesson-from-digitized.md)."
    )

    for old, new, label in [
        (old_b1, new_b1, "b1"),
        (old_b2, new_b2, "b2"),
        (old_p, new_p, "p"),
        (old_s, new_s, "s"),
        (old_b4, new_b4, "b4"),
    ]:
        if old not in t:
            raise SystemExit(f"missing {label}")
        t = t.replace(old, new, 1)

    path.write_text(t, encoding="utf-8")
    print("patched", path.relative_to(REPO))


if __name__ == "__main__":
    main()
