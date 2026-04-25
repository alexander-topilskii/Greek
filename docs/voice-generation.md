# 🎙 Voice: HTML и голосовая отработка

*Как в репозитории собираются страницы для голосовой практики и чем пользоваться в сессии с ИИ.*

**Навигация:** [README.md](README.md) · [Обзор урока в репозитории](lesson-extraction-from-textbook.md) · [Правила конспекта](essence-generation.md)

Конспект **`book/pages/lesson_N/essence_N/essence_N.md`** готовится по [essence-generation.md](essence-generation.md). Отдельный пайплайн **`voice_lesson_N.md`** из оцифровки главы — в [voice-lesson-from-digitized.md](voice-lesson-from-digitized.md).

**Автономность** по смыслу плана относится к **исходным** markdown-файлам урока для читателя (`essence_…/essence_….md`, `lesson_voice_…/voice_lesson_….md`): в них нет перекрёстных ссылок и ссылок на сырьё. Сгенерированный **`essence_N.html`** технически объединяет блок промпта и текст конспекта на одной странице — это **не** нарушение правила «двух островов», потому что в сам **`essence_N.md`** ссылку на голосовой урок или на HTML не вставляют.

---

## 1. Статические HTML-страницы (генерация)

Скрипт: **`scripts/generate_essence_html.py`** (также вызывается при регенерации `content_N.md` / `content_N.html` через **`scripts/generate_book_lesson_content_md.py`**).

| Страница | Источники | Редактировать вручную |
|----------|-----------|------------------------|
| **`essence_N.html`** | блок промпта из [promt/voice_essence_notes_promt.md](promt/voice_essence_notes_promt.md) + `essence_N/essence_N.md` (+ при наличии **`essence_N/lexicon.md`**, склейка при генерации) | нет |
| **`lesson_voice_N/voice_lesson_N.html`** | блок промпта из [promt/voice_roleplay_system_promt.md](promt/voice_roleplay_system_promt.md) + `voice_lesson_N.md` (+ при наличии **`lesson_voice_N/lexicon.md`**) | нет |

Фрагменты после основного файла перечислены в **`scripts/generate_essence_html.py`** (`OPTIONAL_MD_FRAGMENTS`); сейчас это только `lexicon.md`. Между частями вставляется разделитель `---`.

В браузере: кнопка копирования собирает **текст промпта** и **весь склеенный markdown** материала урока для вставки в чат.

Пересборка опубликованных HTML при правках промптов или уроков: локально `python3 scripts/generate_book_lesson_content_md.py` и коммит; на GitHub — workflow **GitHub Pages** (после включения источника *GitHub Actions* в настройках Pages репозитория).

---

## 2. Промпты, которые копирует HTML

- **Конспект:** **[promt/voice_essence_notes_promt.md](promt/voice_essence_notes_promt.md)** — один и тот же блок для любого `essence_N.html`.
- **Ролевой урок:** **[promt/voice_roleplay_system_promt.md](promt/voice_roleplay_system_promt.md)** — для любого `voice_lesson_N.html`. Каталог **`docs/promt/`** — только промпты, встраиваемые в HTML; см. [promt/README.md](promt/README.md).

## 3. Промпт голосовой сессии с конспектом (ручная сессия)

- Текст промпта: **[promt/voice_essence_notes_promt.md](promt/voice_essence_notes_promt.md)**. Как пользоваться сессией: **[promts/ai_voice_promt.md](promts/ai_voice_promt.md)**.
- В сессии с ИИ: скопировать промпт и **прикрепить файл** **`book/pages/lesson_N/essence_N/essence_N.md`** того же урока (или вставить содержимое из `essence_N.html`). Это **инструкция для сессии**, а не требование вставлять ссылку на конспект внутрь **`voice_lesson_N.md`**.
- Промпт рассчитан на структуру конспекта из [essence-generation.md](essence-generation.md) (грамматика → фразы → словарь; диалоги после микрофраз; без ключей к заданиям пособия).

---

## 4. Голосовой урок по единой оцифровке

Раздаточный **`voice_lesson_N.md`** и интеграция в `content_N.md`: **[voice-lesson-from-digitized.md](voice-lesson-from-digitized.md)**. Промпт генерации: **[promts/voice_lesson_generation.md](promts/voice_lesson_generation.md)**.

В одной голосовой сессии **вложениями** можно сочетать конспект и `voice_lesson_N.md` — см. [voice-lesson-from-digitized.md](voice-lesson-from-digitized.md); в markdown-файлах урока при этом **нет** обязательных ссылок друг на друга.

---

## 5. Строки в `content_N.md` / `content_N.html`

При наличии **`essence_N/essence_N.md`** скрипт контента добавляет ссылки **«Суть урока»** и **«Voice (HTML)»** на конспект и на `essence_N.html`. Подробности пересборки — в [essence-generation.md](essence-generation.md), раздел про публикацию и пересборку.

---

*Дополняет [agents.md](../agents.md).*
