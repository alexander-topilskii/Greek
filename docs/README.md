# 📚 Документация

**Навигация:** [Readme](../Readme.md) → [agents.md](../agents.md) → `docs/README.md`

Краткое оглавление методичек и промптов.

**Политика автономности:** учебные файлы **`book/pages/lesson_N/essence_N/essence_N.md`** и **`book/pages/lesson_N/lesson_voice_N/voice_lesson_N.md`** самодостаточны для читателя (без ссылок на сырьё и без перекрёста друг с другом); навигация по всем слоям урока — через **`content_N.md`**. Подробности: [essence-generation.md](essence-generation.md), [voice-lesson-from-digitized.md](voice-lesson-from-digitized.md), обзор слоёв — [lesson-extraction-from-textbook.md](lesson-extraction-from-textbook.md).

**Скрипты:** упоминания `lesson_digitized` / `digitized` в `scripts/*.py` относятся к **входам** пайплайнов и к генерации **`content_N`** как хаба; это не задача вставлять такие ссылки в тело автономных `essence_*.md` / `voice_lesson_*.md`.

## Методички

| Документ | Назначение |
|----------|------------|
| [lesson-extraction-from-textbook.md](lesson-extraction-from-textbook.md) | Обзор: подготовка (скан, оцифровка, `lesson_digitized`), хаб `content`, автономные `essence` и `voice_lesson`, Voice HTML |
| [essence-generation.md](essence-generation.md)                           | Правила конспекта `essence_N/essence_N.md`: автономность, структура, эталоны, чеклист |
| [voice-generation.md](voice-generation.md)                               | `essence_N.html`, `voice_lesson_*.html`, промпты, связь с `content_N.md` |
| [voice-lesson-from-digitized.md](voice-lesson-from-digitized.md)         | Вход генерации `lesson_N_digitized.md` vs автономный `voice_lesson_N.md`, папки, интеграция в `content_N.md` |

## Промпты (`docs/promts/`)

| Файл                                                                   | Назначение                                                                                               |
|------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| [promts/ai_voice_promt.md](promts/ai_voice_promt.md)                   | Голосовая сессия с приложенным `essence_N/essence_N.md`; тот же блок подставляется в `essence_N.html`   |
| [promts/voice_lesson_generation.md](promts/voice_lesson_generation.md) | Генерация раздаточного `voice_lesson_N.md` по тексту `lesson_N_digitized.md`                             |
