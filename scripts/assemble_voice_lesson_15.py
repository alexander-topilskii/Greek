"""Assemble book/pages/lesson_15/lesson_voice_15/voice_lesson_15.md from lesson_15_digitized.md slices."""

from __future__ import annotations

from pathlib import Path


def main() -> None:
    repo = Path(__file__).resolve().parents[1]
    digit_path = repo / "book/pages/lesson_15/lesson_digitized/lesson_15_digitized.md"
    out_path = repo / "book/pages/lesson_15/lesson_voice_15/voice_lesson_15.md"
    out_path.parent.mkdir(parents=True, exist_ok=True)

    lines = digit_path.read_text(encoding="utf-8").splitlines()
    ANCHOR_LINE_BASE = 26
    _cur_anchor = next(i for i, ln in enumerate(lines) if '<a id="' in ln)
    _slice_shift = ANCHOR_LINE_BASE - _cur_anchor

    def sl(a: int, b: int) -> str:
        return "\n".join(lines[a - _slice_shift : b - _slice_shift]).rstrip()

    mic = chr(0x1F399)
    house = chr(0x1F3E0)
    book = chr(0x1F4DA)
    page = chr(0x1F4C4)
    zap = chr(0x26A1)

    # l15p200@26 … l15p211@714, EOF len(lines)
    review_verbs_p200 = sl(26, 147)
    nouns_prep_pron_p201 = sl(147, 225)
    seira_exercises_p202_203 = sl(225, 331)
    cats_b16_b17_p204_205 = sl(331, 437)
    messages_p206_207 = sl(437, 568)
    mykonos_p208 = sl(568, 620)
    grapse_p209 = sl(620, 674)
    logo_role_p210_211 = sl(674, len(lines))

    prep_pron_cheat = sl(178, 220)
    gia_typoi_regular = sl(32, 88)
    gia_anomala = sl(88, 147)
    gia_ousiastika = sl(153, 178)

    out: list[str] = []

    def ln(s: str = "") -> None:
        out.append(s)

    ln(f"# {mic} Голосовой урок 15 (по оцифровке главы)")
    ln()
    ln("### Блок 1: Коммуникативные ситуации и ролевые игры")
    ln()

    ln(
        "#### Ситуация 1 — «Πάμε πάλι!»: τύποι ρημάτων "
        "(ενεστώτας, αόριστος, μέλλων)"
    )
    ln()
    ln("```text")
    ln(review_verbs_p200)
    ln("```")
    ln()
    ln(
        "*Роль А / Б:* Прочитайте строки таблиц вслух; назовите формы "
        "ενεστώτα / αορίστου / μέλλοντα для выбранных глаголов."
    )
    ln()
    ln("---")
    ln()

    ln(
        "#### Ситуация 2 — ουσιαστικά, προθέσεις τόπου, αντωνυμίες"
    )
    ln()
    ln("```text")
    ln(nouns_prep_pron_p201)
    ln("```")
    ln()
    ln(
        "*Роль А / Б:* Проговорите примеры склонений существительных; "
        "составьте фразы с предлогами (δίπλα, κοντά, …); "
        "проговорите предложения с местоимёнными формами (μου, σου, …)."
    )
    ln()
    ln("---")
    ln()

    ln(
        "#### Ситуация 3 — «\u0397 σειρά μου τώρα», Ειρήνη, Κυριάκος и Ερβίν"
    )
    ln()
    ln("```text")
    ln(seira_exercises_p202_203)
    ln("```")
    ln()
    ln(
        "*Роль А / Б:* Упорядочьте абзацы биографии; заполните анкету и пропуски про Ειρήνη; "
        "разыграйте диалог при парковке (будущее время)."
    )
    ln()
    ln("---")
    ln()

    ln(
        "#### Ситуация 4 — «Πού είναι τα γατάκια;», упр. 5; B16, B17"
    )
    ln()
    ln("```text")
    ln(cats_b16_b17_p204_205)
    ln("```")
    ln()
    ln(
        "*Роль А / Б:* Опишите, где коты (предлоги места); дополните предложения "
        "с местоимёнными формами; прослушайте B16 и B17, выполните упражнения 6 и 7."
    )
    ln()
    ln("---")
    ln()

    ln("#### Ситуация 5 — «Απαντώ στα μηνύματα» (8 α–η)")
    ln()
    ln("```text")
    ln(messages_p206_207)
    ln("```")
    ln()
    ln(
        "*Роль А / Б:* Прочитайте сообщения α–η; устно сопоставьте их с ответами 1–14 "
        "(как в учебнике)."
    )
    ln()
    ln("---")
    ln()

    ln(
        "#### Ситуация 6 — «Διακοπές στη Μύκονο», σωστό ή λάθος"
    )
    ln()
    ln("```text")
    ln(mykonos_p208)
    ln("```")
    ln()
    ln(
        "*Роль А / Б:* Прочитайте текст о Миконосе; обсудите утверждения в таблице «σωστό / λάθος»."
    )
    ln()
    ln("---")
    ln()

    ln(
        "#### Ситуация 7 — Γράψε-σβήσε: таверна, текст для журнала"
    )
    ln()
    ln("```text")
    ln(grapse_p209)
    ln("```")
    ln()
    ln(
        "*Роль А / Б:* Напишите письмо о вечере в таверне; начните текст для журнала "
        "(удачный / неудачный день)."
    )
    ln()
    ln("---")
    ln()

    ln(
        "#### Ситуация 8 — «\u0388\u03c7\u03c9 \u03c4\u03bf\u03bd \u03bb\u03cc\u03b3\u03bf», "
        "роли 1.3 и 14 (медиум, психолог)"
    )
    ln()
    ln("```text")
    ln(logo_role_p210_211)
    ln("```")
    ln()
    ln(
        "*Роль А / Б:* Ответьте на микрофон в 1.2; разыграйте 1.3 (\u039b\u03ac\u03c7\u03b5\u03c3\u03b9\u03c2 / клиент); "
        "роль 14 (пациент / психолог)."
    )

    ln()
    ln("### Блок 2: Шпаргалка (προθέσεις τόπου + αντωνυμίες)")
    ln()
    ln("```text")
    ln(prep_pron_cheat)
    ln("```")
    ln()

    ln("### Блок 3: Тематический словарь и образцы")
    ln()
    ln("#### Για δες: τύποι \u0391, \u03921 + \u03922")
    ln()
    ln("```text")
    ln(gia_typoi_regular)
    ln("```")
    ln()
    ln("#### Ανώμαλα και συχνά ρήματα")
    ln()
    ln("```text")
    ln(gia_anomala)
    ln("```")
    ln()
    ln("#### Ουσιαστικά (ον., γεν., αιτ.)")
    ln()
    ln("```text")
    ln(gia_ousiastika)
    ln("```")

    out_path.write_text("\n".join(out) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
