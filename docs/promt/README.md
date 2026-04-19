# Промпты для встраивания в HTML

**Навигация:** [Readme](../../Readme.md) → [docs/README.md](../README.md) → `docs/promt/README.md`

В **`docs/promt/`** лежат **только** те промпты, текст которых **подставляется в сгенерированные страницы** скриптом **`scripts/generate_essence_html.py`** (кнопка «Скопировать промпт + материал» в браузере). После изменения файлов здесь нужно перегенерировать HTML (`scripts/generate_book_lesson_content_md.py`) и закоммитить вывод; при включённом **GitHub Actions** для Pages это делает workflow **GitHub Pages**.

**Не класть сюда:** методички «для людей» без встраивания, промпты только для чата ИИ без участия HTML, вспомогательные промпты генерации markdown (например [voice_lesson_generation.md](../promts/voice_lesson_generation.md)) — им место в **[docs/promts/](../promts/)** или в других методичках.

**Сейчас в каталоге**

| Файл | Куда встраивается |
|------|-------------------|
| [voice_essence_notes_promt.md](voice_essence_notes_promt.md) | `book/pages/lesson_N/essence_N.html` |
| [voice_roleplay_system_promt.md](voice_roleplay_system_promt.md) | `book/pages/lesson_N/lesson_voice_N/voice_lesson_N.html` |

Методичка для людей (как пользоваться сессией, без дублирования текста промпта): [promts/ai_voice_promt.md](../promts/ai_voice_promt.md). Обзор пайплайна — [voice-generation.md](../voice-generation.md).
