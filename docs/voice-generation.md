# 🎙 Voice: HTML и голосовая отработка

*Как в репозитории собираются страницы для голосовой практики и чем пользоваться в сессии с ИИ.*

**Навигация:** [README.md](README.md) · [Обзор урока в репозитории](lesson-extraction-from-textbook.md) · [Правила конспекта](essence-generation.md)

Конспект **`essence_N.md`** готовится по [essence-generation.md](essence-generation.md). Отдельный пайплайн **`voice_lesson_N.md`** из оцифровки главы — в [voice-lesson-from-digitized.md](voice-lesson-from-digitized.md).

---

## 1. Статические HTML-страницы (генерация)

Скрипт: **`scripts/generate_essence_html.py`** (также вызывается при регенерации `content_N.md` через `generate_book_lesson_content_md.py`).

| Страница | Источники | Редактировать вручную |
|----------|-----------|------------------------|
| **`essence_N.html`** | блок промпта из [promts/ai_voice_promt.md](promts/ai_voice_promt.md) + `essence_N/essence_N.md` | нет |
| **`lesson_voice_N/voice_lesson_N.html`** | фиксированный ролевой промпт в скрипте + `voice_lesson_N.md` | нет |

В браузере: кнопка копирования собирает **текст промпта** и **markdown** материала урока для вставки в чат.

---

## 2. Промпт голосовой сессии с конспектом

- Файл: **[promts/ai_voice_promt.md](promts/ai_voice_promt.md)** — один и тот же блок для любого урока.
- В сессии с ИИ: скопировать промпт и приложить **`essence_N.md`** того же урока (или содержимое из `essence_N.html`).
- Промпт рассчитан на структуру конспекта из [essence-generation.md](essence-generation.md) (грамматика → фразы → эталоны → словарь; диалоги после микрофраз).

---

## 3. Голосовой урок по единой оцифровке

Раздаточный **`voice_lesson_N.md`** и интеграция в `content_N.md`: **[voice-lesson-from-digitized.md](voice-lesson-from-digitized.md)**. Промпт генерации: **[promts/voice_lesson_generation.md](promts/voice_lesson_generation.md)**.

Его можно приложить к голосовой сессии **вместе** с `essence_N.md` или **вместо** него, если конспекта ещё нет.

---

## 4. Строки в `content_N.md` / `content_N.html`

При наличии **`essence_N.md`** скрипт контента добавляет ссылки **«💎 Суть урока»** и **«🎙 Voice (HTML)»** на конспект и на `essence_N.html`. Подробности пересборки — в [essence-generation.md](essence-generation.md) §9.

---

*Дополняет [agents.md](../agents.md).*
