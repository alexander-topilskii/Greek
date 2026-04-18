"""Assemble book/pages/lesson_17/lesson_voice_17/voice_lesson_17.md from lesson_17_digitized.md slices."""

from __future__ import annotations

from pathlib import Path


def main() -> None:
    repo = Path(__file__).resolve().parents[1]
    digit_path = repo / "book/pages/lesson_17/lesson_digitized/lesson_17_digitized.md"
    out_path = repo / "book/pages/lesson_17/lesson_voice_17/voice_lesson_17.md"
    out_path.parent.mkdir(parents=True, exist_ok=True)

    lines = digit_path.read_text(encoding="utf-8").splitlines()
    ANCHOR_LINE_BASE = 28
    _cur_anchor = next(i for i, ln in enumerate(lines) if '<a id="' in ln)
    _slice_shift = ANCHOR_LINE_BASE - _cur_anchor

    def sl(a: int, b: int) -> str:
        return "\n".join(lines[a - _slice_shift : b - _slice_shift]).rstrip()

    mic = chr(0x1F399)
    house = chr(0x1F3E0)
    book = chr(0x1F4DA)
    page = chr(0x1F4C4)
    zap = chr(0x26A1)

    # l17p232@28 … l17p245@1036, EOF len(lines)
    intro_b22_ex1 = sl(28, 127)
    seira_ex2_3 = sl(127, 260)
    enestotas_mellon_prostaktiki = sl(260, 354)
    imper_b_ex4_7 = sl(354, 495)
    ex7_8_salary = sl(495, 629)
    ex9_vocab_text = sl(629, 788)
    exercises_12_15a = sl(788, 935)
    exercises_15b_end = sl(935, len(lines))

    pos_lene_b22 = sl(98, 108)
    pos_lene_salary = sl(612, 623)

    gia_prostaktiki_typoi_a = sl(270, 348)
    gia_prostaktiki_typoi_b = sl(364, 384)

    out: list[str] = []

    def ln(s: str = "") -> None:
        out.append(s)

    ln(f"# {mic} Голосовой урок 17 (по оцифровке главы)")
    ln()
    ln("### Блок 1: Коммуникативные ситуации и ролевые игры")
    ln()

    ln(
        "#### Ситуация 1 — «Πάμε για δουλειά», B22, упр. 1, «Πώς το λένε»"
    )
    ln()
    ln("```text")
    ln(intro_b22_ex1)
    ln("```")
    ln()
    ln(
        "*Роль А / Б:* Разыграйте диалог B22 (\u03a6\u03bf\u03af\u03b2\u03bf\u03c2 / υπάλληλος); "
        "оцените упр. 1 (σωστό / λάθος); повторите фразы «Πώς το λένε»."
    )
    ln()
    ln("---")
    ln()

    ln(
        "#### Ситуация 2 — «\u0397 σειρά μου τώρα», упр. 2–3"
    )
    ln()
    ln("```text")
    ln(seira_ex2_3)
    ln("```")
    ln()
    ln(
        "*Роль А / Б:* Ответьте на микрофон в 2; заполните форму и текст резюме в 3."
    )
    ln()
    ln("---")
    ln()

    ln(
        "#### Ситуация 3 — ενεστώτας, μέλλοντας, προστακτική (τύπος Α, цветные таблицы)"
    )
    ln()
    ln("```text")
    ln(enestotas_mellon_prostaktiki)
    ln("```")
    ln()
    ln(
        "*Роль А / Б:* Прочитайте таблицы вслух; назовите προστακτική (εσύ / εσείς) для выбранных глаголов."
    )
    ln()
    ln("---")
    ln()

    ln(
        "#### Ситуация 4 — τύποι \u03921+\u03922, προστακτική, упр. 4 и блок 5–7"
    )
    ln()
    ln("```text")
    ln(imper_b_ex4_7)
    ln("```")
    ln()
    ln(
        "*Роль А / Б:* Выучите формы B1/B2; свяжите να + υποτακτική с προστακτική (πράσινο κουτί); "
        "выполните упр. 4 и задания 5–7."
    )
    ln()
    ln("---")
    ln()

    ln(
        "#### Ситуация 5 — упр. 7 (продолжение), "
        "«Καί ρώτα για τον μισθό…»"
    )
    ln()
    ln("```text")
    ln(ex7_8_salary)
    ln("```")
    ln()
    ln(
        "*Роль А / Б:* Доделайте цепочки в 7; выполните 8; разыграйте советы перед собеседованием; "
        "повторите вторую «Πώς το λένε»."
    )
    ln()
    ln("---")
    ln()

    ln(
        "#### Ситуация 6 — упр. 9–10, «Για δες» (лексика), κείμενο"
    )
    ln()
    ln("```text")
    ln(ex9_vocab_text)
    ln("```")
    ln()
    ln(
        "*Роль А / Б:* Заполните пропуски в 9; ответьте на вопросы микрофона в 10; "
        "проговорите лексику по колонкам; перескажите κείμενο про работу и зарплату."
    )
    ln()
    ln("---")
    ln()

    ln(
        "#### Ситуация 7 — Γράψε-σβήσε, «Για δες» (грамматика), упр. 1.2–1.4"
    )
    ln()
    ln("```text")
    ln(exercises_12_15a)
    ln("```")
    ln()
    ln(
        "*Роль А / Б:* Напишите письмо-заявление; повторите грамматическую вставку «Για δες»; "
        "выполните 1.2–1.4."
    )
    ln()
    ln("---")
    ln()

    ln(
        "#### Ситуация 8 — упр. 1.4 (продолжение), 5, тайминг предложений, 1.6–1.9"
    )
    ln()
    ln("```text")
    ln(exercises_15b_end)
    ln("```")
    ln()
    ln(
        "*Роль А / Б:* Допишите 1.4 и письмо в 5; сопоставьте предложения в 1.6; "
        "заполните пропуски и ответьте на вопросы в 1.7–1.9."
    )

    ln()
    ln("### Блок 2: Шпаргалка («Πώς το λένε») — после B22 и после блока про μισθό")
    ln()
    ln("```text")
    ln(pos_lene_b22)
    ln()
    ln(pos_lene_salary)
    ln("```")
    ln()

    ln("### Блок 3: Тематический словарь и образцы")
    ln()
    ln("#### Προστακτική — τύπος Α (μπλε · πορτοκαλί · πράσινος · μωβ)")
    ln()
    ln("```text")
    ln(gia_prostaktiki_typoi_a)
    ln("```")
    ln()
    ln("#### Τύποι \u03921+\u03922: να → προστακτική, μήν")
    ln()
    ln("```text")
    ln(gia_prostaktiki_typoi_b)
    ln("```")

    out_path.write_text("\n".join(out) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
