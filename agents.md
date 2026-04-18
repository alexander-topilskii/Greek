# 🧩 Markdown Formatting Rules (Project Standard)

[🏠 Readme](Readme.md) → 🧭 `agents.md`

| ⚡ Быстрые ссылки  |                                                                 |
|-------------------|-----------------------------------------------------------------|
| 🏠 Readme         | [Readme.md](Readme.md)                                          |
| 📘 Уроки          | [К таблице уроков](#5-lesson-table-readme)                      |
| 🧾 Суммарный      | [К спискам](#6-summary-section-суммарный)                       |
| 🎙 Voice + essence | [essence_voice_index.html](book/pages/essence_voice_index.html) |
| 📷 Скриншоты стр. | [page-screenshot-renaming.md](docs/page-screenshot-renaming.md) |
| 📖 Урок из учебника | [lesson-extraction-from-textbook.md](docs/lesson-extraction-from-textbook.md) |
| 🎙 Голосовой урок (оцифровка) | [voice-lesson-from-digitized.md](docs/voice-lesson-from-digitized.md) |

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

- В `Readme.md` одна колонка: ссылка на **`content_{N}.html`** как точку входа по уроку для читателя (`lesson_0` … `lesson_20`). Файл **`content_{N}.md`** пересобирается тем же скриптом, что и HTML (`scripts/generate_book_lesson_content_md.py`), и служит источником/синхронным дублем для диффов и превью в репозитории; в пользовательской навигации используйте HTML.
- Ссылки на сканы (`raw/*.png`), оцифровки (`digitized/N.md`), при наличии — **`lesson_digitized/lesson_N_digitized.md`**, конспект и voice задаются **внутри** сгенерированного `content_N.html` / `content_N.md`, не дублируются отдельными колонками в Readme.
- Опционально в `book/pages/lesson_N/` можно добавить **`essence_N.md`** — **практическая замена** печатного материала для повторения: правила, фразы, словарь. **В тексте конспекта нельзя** упоминать или подразумевать учебник, книгу, пособие — читатель опирается только на конспект и файлы репозитория (см. [docs/lesson-extraction-from-textbook.md](docs/lesson-extraction-from-textbook.md) §3.1). Рекомендуемый порядок: **грамматика → готовые фразы/диалоги → [опционально] эталоны → словарь в конце**; **в конце раздела со словарём (📇)** — **итоговая таблица** всех **уникальных** слов и форм из материала урока в учебнике, **включая слова из названий и условий заданий**, с переводом (греч. | рус.). Вместо сносок «это не входит в активный словарь» давай **пояснение + таблицу или примеры для тренировки**. При наличии файла скрипт регенерации `content_N.md` / `content_N.html` добавит строки «💎 Суть урока» и «🎙 Voice (HTML)» в Markdown и обновит сгенерированный **`essence_N.html`** (промпт из [docs/ai_voice_promt.md](docs/ai_voice_promt.md) + конспект; индекс: [essence_voice_index.html](book/pages/essence_voice_index.html)). Подробный чеклист: [docs/lesson-extraction-from-textbook.md](docs/lesson-extraction-from-textbook.md).
- Опционально **`lesson_voice_N/voice_lesson_N.md`** — раздаточный материал для разговорной отработки **по единой оцифровке** `lesson_digitized/lesson_N_digitized.md`: чеклист, структура папки, промпт и ссылка из сгенерированного оглавления (`content_N.html` / `content_N.md`) — [docs/voice-lesson-from-digitized.md](docs/voice-lesson-from-digitized.md).
- Ссылки на слова/карточки в других модулях оформляй отдельно, не в этой таблице.

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

## 10. UTF-8, греческий текст и генерация файлов

Все `.md` в репозитории — **UTF-8**. «Поломки кодировки» чаще всего из-за **цепочки копирования и escape-последовательностей**, а не из-за самой кодировки на диске.

- **Редактор и сохранение:** при создании или правке вручную сохраняй файл как UTF-8; не смешивай в одном файле разные нормализации одной буквы без нужды (NFC обычно достаточно).
- **Python и строки с не-ASCII:**
  - В литералах `\u` допустимы **ровно четыре шестнадцатеричные цифры** (`\u03b1` → α). Не подставляй **десятичный** код символа в виде `\u945` — это даст **другой символ** или ошибку.
  - Для произвольного кода удобно: `chr(0x03b1)` или `chr(945)` — явно и без двусмысленности.
  - Эмодзи: `\U0001f399` (восемь hex-цифр после `\U`) или символ в исходнике файла `.py`, сохранённого в UTF-8.
- **Оболочка и heredoc:** большие фрагменты с греческим, эмодзи и русским не прогоняй через `python3 <<'EOF'` без проверки: канал может исказить байты. Надёжнее: **отдельный `.py` в репозитории** с `path.write_text(..., encoding="utf-8")` или правка `.md` прямо в IDE.
- **Гомоглифы:** латинская **B** (U+0042) и греческая заглавная бета (U+0392) выглядят одинаково; поиск/замена и автогенерация должны использовать **тот алфавит, что в учебнике**, иначе строки «не находятся» и в тексте появляются лишние символы.
- **Проверка после генерации:** открой файл в IDE; при сомнении — поиск по **известному слову из оцифровки** (например из `lesson_N_digitized.md`). Появление **U+FFFD** (официальное имя в Unicode — replacement character) в новом тексте — признак потери байтов на пути записи.
- **ИИ и инструменты записи:** при массовой вставке греческого через посредника держи **эталон** (фрагмент `lesson_*_digitized.md`) и сверяй спорные формы (апостроф в `Από 'δώ`, ударения, артикли).
