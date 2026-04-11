# 🧩 Markdown Formatting Rules (Project Standard)

[🏠 Readme](Readme.md) → 🧭 `agents.md`

| ⚡ Быстрые ссылки  |                                                                 |
|-------------------|-----------------------------------------------------------------|
| 🏠 Readme         | [Readme.md](Readme.md)                                          |
| 📘 Уроки          | [К таблице уроков](#5-lesson-table-readme)                      |
| 🧾 Суммарный      | [К спискам](#6-summary-section-суммарный)                       |
| 📷 Скриншоты стр. | [page-screenshot-renaming.md](docs/page-screenshot-renaming.md) |

Use these rules for all new `.md` pages in this repo.

## 1. 🎯 Headings and emojis

- Always start with a title heading: `# ...`
- Add a relevant emoji in the title when it makes sense.
- Section headers use `##` and can include emojis to improve scanability.
- Keep emojis consistent across similar sections (e.g. `📚 Материалы`, `🔁 Переходы`).

## 2. 🧭 Breadcrumbs (Хлебные крошки)

- Immediately after the title, add a bold breadcrumbs line.
- Format:
    - `[🏠 Readme](../../Readme.md) → ... → 📄 \`file.md\``
- Use the correct relative path for the current file.
- Use backticks for the current filename.

## 3. ⚡ Quick links table (⚡ Быстрые ссылки)

- After breadcrumbs, add a compact two-column table.
- Example structure:
    - `| ⚡ Быстрые ссылки    |                                                          |`
    - `|---------------------|----------------------------------------------------------|`
    - `| 📄 Список слов      | [all.md](all.md)                                         |`
- Keep the header row left-aligned and pad spacing for neat monospace alignment.
- Use consistent labels and emojis:
    - `📄 Список слов`
    - `🧠 Карточки`
    - `🧭 Навигация урока`
    - `🧾 Суммарный список`
    - `📘 Правила`

## 4. 🧭 Navigation sections

- Use sections like:
    - `## 📚 Материалы`
    - `## 🔁 Переходы`
- Links are bullet lists with emoji prefixes.
- Example bullet:
    - `- 🧠 [index.html](index.html)`

## 5. 📘 Lesson table (Readme)

- The main lesson table in `Readme.md` uses 4 columns:
    - `📘 Урок`, `📚 Материалы`, `🃏 Карточки`, `📘 Правила`
- Replace `all.md` link text with: `[📄 список слов](...)`
- If no rules, use `—`.
- Use local `index.html` for “карточки”, not external Quizlet.

## 6. 🧾 Summary section (Суммарный)

- Use bullets with emojis in `Readme.md` and summary navigation:
    - `📌 all_words.md`
    - `🧠 index.html`
    - `📘 rules`
    - `🧭 navigation.md`

## 7. 📊 Tables inside rules

- Keep tables aligned with header separator rows.
- If a table uses colored blocks or markers, include a short legend below it.

## 8. 🔗 Links and text

- Prefer clear link text (e.g., `карточки`, `📄 список слов`, `Местоимения`).
- Use relative links within the repo.
- Avoid empty lines between heading and table; add a blank line before a new section.

## 9. 📷 Скриншоты страниц учебника (`modules/pages/`)

- При переименовании PNG в `lesson N` в вид **`{номер}.png`** по номеру в колонтитуле страницы следуй полному чеклисту:
  надёжная идентификация номера (OCR только как помощник), проверка диапазона, **двухфазное** переименование без
  коллизий, поиск битых ссылок в репо.
- Подробности, типичные ошибки OCR и шаблон
  процесса: [docs/page-screenshot-renaming.md](docs/page-screenshot-renaming.md).
