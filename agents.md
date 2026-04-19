# 🧩 Markdown Formatting Rules (Project Standard)

Правила для всех `.md` в репозитории. **Крошки и таблица «быстрые ссылки» в шапке — только у корневого [Readme.md](Readme.md).** В остальных файлах после `# …` сразу содержание (при необходимости курсив-ввод), без навигации по репозиторию; **исключение:** учебные **`book/pages/lesson_N/essence_N/essence_N.md`** и **`book/pages/lesson_N/lesson_voice_N/voice_lesson_N.md`** — минимальная шапка по [docs/essence-generation.md](docs/essence-generation.md) и [docs/voice-lesson-from-digitized.md](docs/voice-lesson-from-digitized.md) (крошки до `content_N.md`, узкая таблица быстрых ссылок). Читательские переходы ко всем слоям урока — в HTML (`content_N.html`, при наличии `essence_N.html` и `lesson_voice_N/voice_lesson_N.html`).

Куда смотреть: [Readme.md](Readme.md) · [docs/README.md](docs/README.md) · [lesson-extraction-from-textbook.md](docs/lesson-extraction-from-textbook.md) · [essence-generation.md](docs/essence-generation.md) · [voice-generation.md](docs/voice-generation.md) · [voice-lesson-from-digitized.md](docs/voice-lesson-from-digitized.md)

## 1. 🎯 Headings and emojis

- Always start with a title heading: `# ...`
- Add a relevant emoji in the title when it makes sense.
- Section headers use `##` and can include emojis to improve scanability.
- Keep emojis consistent across similar sections (e.g. `📚 Материалы`, `🔁 Переходы`).

## 2. Без шапки-навигации в Markdown (кроме корневого Readme и автономных уроковых файлов)

- Не добавляй строку хлебных крошек `**[🏠 Readme](...) → …**`.
- Не добавляй двухколоночную таблицу «быстрые ссылки» на другие файлы репозитория сразу под заголовком.
- Не добавляй в `lesson_*_digitized.md` блок «## … Навигация по разделам» со списком якорей по главе.
- Исключение: **[Readme.md](Readme.md)** в корне — там сохраняются оглавление и таблица уроков.
- Исключение: **`book/pages/lesson_N/essence_N/essence_N.md`** и **`book/pages/lesson_N/lesson_voice_N/voice_lesson_N.md`** — разрешены **только** хлебные крошки до [Readme.md](Readme.md) → `book/pages` → **`content_N.md`** → текущий файл и **узкая** таблица «Быстрые ссылки» без сырья и без перекрёста между конспектом и голосовым уроком (подробно: [docs/essence-generation.md](docs/essence-generation.md), [docs/voice-lesson-from-digitized.md](docs/voice-lesson-from-digitized.md)).
- Таблицы **внутри** учебного текста (спряжения, лексика) не считаются навигацией и допустимы.

## 3. Вводный абзац

- Сразу после `#` можно один короткий курсив с контекстом (*источник страницы, тема*), без таблиц.

## 4. Разделы со ссылками (содержание, не «хром» сайта)

- Разделы вроде `## 📚 Материалы` с предметными ссылками допустимы, если это часть материала, а не дублирование шапки сайта.


## 5. 📘 Lesson table (Readme)

- В `Readme.md` одна колонка: ссылка на **`content_{N}.html`** как точку входа по уроку для читателя (`lesson_0` … `lesson_20`). Файл **`content_{N}.md`** пересобирается тем же скриптом, что и HTML (`scripts/generate_book_lesson_content_md.py`), и служит сырьём для диффов; в пользовательской навигации используйте HTML.
- Ссылки на сканы (`raw/*.png`), оцифровки (`digitized/N.md`), при наличии — **`lesson_digitized/lesson_N_digitized.md`**, конспект и voice задаются **внутри** `content_N.html` / минимального `content_N.md`, не дублируются отдельными колонками в Readme.
- Опционально в `book/pages/lesson_N/essence_N/` добавь **`essence_N.md`** — **практическая замена** печатного материала для повторения: правила, фразы, словарь. Файл **автономен** для читателя: **нет** markdown-ссылок на сырьё (`raw/`, `digitized/`, `lesson_digitized/`), на голосовой урок, на HTML voice; минимальная навигация — только крошки и при необходимости **`content_N.md`** / соседние конспекты (без перекрёста с `voice_lesson`). **В тексте конспекта нельзя** подменять смысл отсылками к пособию как к обязательному источнику (слово «книга» в примерах допустимо). Обзор слоёв: [docs/lesson-extraction-from-textbook.md](docs/lesson-extraction-from-textbook.md); **детально:** [docs/essence-generation.md](docs/essence-generation.md). Рекомендуемый порядок: **грамматика → готовые фразы/диалоги → [опционально] эталоны → словарь в конце**; **в конце раздела со словарём (📇)** — **итоговая таблица** всех **уникальных** слов и форм из материала урока в учебнике, **включая слова из названий и условий заданий**, с переводом (греч. | рус.). Вместо сносок «это не входит в активный словарь» давай **пояснение + таблицу или примеры для тренировки**. При наличии файла скрипт регенерации `content_N.md` / `content_N.html` обновляет **`essence_N.html`** (промпт из [docs/promt/voice_essence_notes_promt.md](docs/promt/voice_essence_notes_promt.md) + конспект; как пользоваться сессией — [docs/promts/ai_voice_promt.md](docs/promts/ai_voice_promt.md); ссылки на эти HTML — внутри `content_N.html`). Сгенерированный HTML технически объединяет промпт и конспект — это не требует ссылки на voice из `essence_N.md`. Ролевой промпт для **`voice_lesson_N.html`** хранится в [docs/promt/voice_roleplay_system_promt.md](docs/promt/voice_roleplay_system_promt.md); в **[docs/promt/](docs/promt/README.md)** — только промпты, текст которых **встраивает** `scripts/generate_essence_html.py` в HTML. **Voice HTML и голосовые сессии:** [docs/voice-generation.md](docs/voice-generation.md).
- Опционально **`lesson_voice_N/voice_lesson_N.md`** — раздаточный материал для разговорной отработки; **генерация** из `lesson_digitized/lesson_N_digitized.md`, **итоговый файл** автономен для читателя — [docs/voice-lesson-from-digitized.md](docs/voice-lesson-from-digitized.md).
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

## 9. 📷 Скриншоты страниц учебника (`book/pages/lesson_N/raw/`)

- При переименовании PNG в **`book/pages/lesson_N/raw/`** в вид **`{номер}.png`** по номеру в колонтитуле страницы следуй полному чеклисту:
  надёжная идентификация номера (OCR только как помощник), проверка диапазона, **двухфазное** переименование без
  коллизий, поиск битых ссылок в репо.
- Пример двухфазного переноса с таблицей соответствий: [scripts/apply_page_renames.py](scripts/apply_page_renames.py).

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
