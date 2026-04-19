# 📚 Документация

**Навигация:** [Readme](../Readme.md) → [agents.md](../agents.md) → `docs/README.md`

Краткое оглавление методичек и промптов.

**Политика автономности:** учебные файлы **`book/pages/lesson_N/essence_N/essence_N.md`** (при вынесении словаря — ещё **`lexicon.md`** в той же папке) и **`book/pages/lesson_N/lesson_voice_N/voice_lesson_N.md`** самодостаточны для читателя относительно сырья (без ссылок на сырьё и без перекрёста конспекта с голосовым уроком); навигация по всем слоям урока — через **`content_N.md`**. Подробности: [essence-generation.md](essence-generation.md), [voice-lesson-from-digitized.md](voice-lesson-from-digitized.md), обзор слоёв — [lesson-extraction-from-textbook.md](lesson-extraction-from-textbook.md).

**Скрипты:** упоминания `lesson_digitized` / `digitized` в `scripts/*.py` относятся к **входам** пайплайнов и к генерации **`content_N`** как хаба; это не задача вставлять такие ссылки в тело автономных `essence_*.md`, при необходимости **`lexicon.md`**, и `voice_lesson_*.md`.

## Методички

| Документ | Назначение |
|----------|------------|
| [lesson-extraction-from-textbook.md](lesson-extraction-from-textbook.md) | Обзор: подготовка (скан, оцифровка, `lesson_digitized`), хаб `content`, автономные `essence` и `voice_lesson`, Voice HTML |
| [essence-generation.md](essence-generation.md)                           | Правила конспекта `essence_N/essence_N.md` (опционально `lexicon.md`): автономность комплекта, структура, эталоны, чеклист |
| [voice-generation.md](voice-generation.md)                               | `essence_N.html`, `voice_lesson_*.html`, промпты, связь с `content_N.md` |
| [voice-lesson-from-digitized.md](voice-lesson-from-digitized.md)         | Вход генерации `lesson_N_digitized.md` vs автономный `voice_lesson_N.md`, папки, интеграция в `content_N.md` |

## Промпты для встраивания в HTML (`docs/promt/`)

Только тексты, которые **подставляет** `scripts/generate_essence_html.py` в сгенерированные страницы. Правило каталога: [promt/README.md](promt/README.md).

| Файл | Куда попадает |
|------|----------------|
| [promt/voice_essence_notes_promt.md](promt/voice_essence_notes_promt.md) | `essence_N.html` |
| [promt/voice_roleplay_system_promt.md](promt/voice_roleplay_system_promt.md) | `lesson_voice_N/voice_lesson_N.html` |

## Прочие промпты и методички (`docs/promts/`)

| Файл                                                                   | Назначение                                                                                               |
|------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| [promts/ai_voice_promt.md](promts/ai_voice_promt.md)                   | Методичка: голосовая сессия с `essence_N/essence_N.md`; ссылка на канонический текст в `docs/promt/voice_essence_notes_promt.md`   |
| [promts/voice_lesson_generation.md](promts/voice_lesson_generation.md) | Генерация раздаточного `voice_lesson_N.md` по тексту `lesson_N_digitized.md`                             |
