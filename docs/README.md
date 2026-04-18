# 📚 Документация

**Навигация:** [Readme](../Readme.md) → [agents.md](../agents.md) → `docs/README.md`

Краткое оглавление методичек и промптов.

## Методички

| Документ                                                                 | Назначение                                                                                            |
|--------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| [lesson-extraction-from-textbook.md](lesson-extraction-from-textbook.md) | Слои урока (скан, оцифровка, `content`, `essence`, Voice HTML), правила конспекта, чеклисты           |
| [voice-lesson-from-digitized.md](voice-lesson-from-digitized.md)         | Пайплайн `voice_lesson_N.md` из `lesson_N_digitized.md`, структура папок, интеграция в `content_N.md` |

## Промпты (`docs/promts/`)

| Файл                                                                   | Назначение                                                                                               |
|------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| [promts/ai_voice_promt.md](promts/ai_voice_promt.md)                   | Голосовая сессия (Voice Mode) с приложенным `essence_N.md`; тот же блок подставляется в `essence_N.html` |
| [promts/voice_lesson_generation.md](promts/voice_lesson_generation.md) | Генерация раздаточного `voice_lesson_N.md` по тексту `lesson_N_digitized.md`                             |
