# 📚 Документация

**Навигация:** [Readme](../Readme.md) → [AGENTS.md](../AGENTS.md) → `docs/README.md`

Краткое оглавление методичек.

**Слои урока:** в `book/pages/lesson_N/` — хаб **`content_N.html`** (и `content_N.md`), сканы, оцифровки, при наличии **`lesson_digitized/`** и опционально **`lexicon.md`**. Подробно: [lesson-extraction-from-textbook.md](lesson-extraction-from-textbook.md). Формат **lexicon.md** — [AGENTS.md](../AGENTS.md) (§5).

**Скрипты:** `scripts/generate_book_lesson_content_md.py` пересобирает `content_N.md` / `content_N.html` из `raw/*.png` и вставляет ссылки при наличии `lexicon.md`, `essence/essence_N.md`, `task/task_N.md` (HTML генерирует модуль `scripts/lesson_supplements.py`, см. [AGENTS.md §12](../AGENTS.md)).

## Методички

| Документ | Назначение |
|----------|------------|
| [lesson-extraction-from-textbook.md](lesson-extraction-from-textbook.md) | Обзор: подготовка (скан, оцифровка, `lesson_digitized`), хаб `content`, словарь `lexicon.md` |

## Каталог `docs/promt/`

[docs/promt/README.md](promt/README.md) — зарезервирован для будущих промптов, встраиваемых в HTML (сейчас пусто).

## Прочие материалы в `docs/promts/`

Вспомогательные подсказки и черновики без привязки к генератору — по мере появления.


## ⚙️ Генерация `content_*.html` и приложений (`essence_*`, `task_*`)

Из корня репозитория (нужен пакет `markdown`):

```bash
pip3 install -r ../scripts/requirements-generate.txt
python3 ../scripts/generate_book_lesson_content_md.py
```

Скрипт: [`scripts/generate_book_lesson_content_md.py`](scripts/generate_book_lesson_content_md.py).

**Из Cursor / VS Code:** палитра команд → **Tasks: Run Task** → **Generate book lesson HTML** (или задача с установкой зависимости: **Install generate deps + …** — см. [`.vscode/tasks.json`](.vscode/tasks.json)).

