"""Assemble book/pages/lesson_20/lesson_voice_20/voice_lesson_20.md from lesson_20_digitized.md slices."""

from __future__ import annotations

from pathlib import Path


def main() -> None:
    repo = Path(__file__).resolve().parents[1]
    digit_path = repo / "book/pages/lesson_20/lesson_digitized/lesson_20_digitized.md"
    out_path = repo / "book/pages/lesson_20/lesson_voice_20/voice_lesson_20.md"
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

    # l20p278@26 … l20p287@705, без παράρτημα (λύσεις) — до idx 750
    sit1_p278_279 = sl(26, 204)
    sit2_p280 = sl(204, 274)
    sit3_p281 = sl(274, 340)
    sit4_p282 = sl(340, 403)
    sit5_p283_hotels = sl(403, 513)
    sit6_p284_jobs = sl(513, 585)
    sit7_p285_286 = sl(585, 705)
    sit8_p287 = sl(705, 750)

    pos_imper_hotels = sl(414, 452)

    gia_typoi_a_irreg = sl(40, 107)
    gia_typoi_b_fem = sl(122, 199)
    gia_echo_logos = sl(643, 681)

    out: list[str] = []

    def ln(s: str = "") -> None:
        out.append(s)

    ln(f"# {mic} Голосовой урок 20 (по оцифровке главы)")
    ln()
    ln("### Блок 1: Коммуникативные ситуации и ролевые игры")
    ln()

    ln(
        "#### Ситуация 1 — «Πάμε πάλι!», сводные таблицы: "
        "ενεστώτας, υποτακτική, προστακτική (стр. 278–279)"
    )
    ln()
    ln("```text")
    ln(sit1_p278_279)
    ln("```")
    ln()
    ln(
        "*Роль А / Б:* Проговорите формы по цветным блокам; "
        "обратите внимание на пометку про «διαβάζω / να αγοράσω» в учебнике."
    )
    ln()
    ln("---")
    ln()

    ln("#### Ситуация 2 — «Πάμε πάλι!», упражнения 1–2 (стр. 280)")
    ln()
    ln("```text")
    ln(sit2_p280)
    ln("```")
    ln()
    ln(
        "*Роль А / Б:* Озвучьте задания; обсудите ответы вслух "
        "(προστακτική, υποτακτική после «να»)."
    )
    ln()
    ln("---")
    ln()

    ln("#### Ситуация 3 — «Πάμε πάλι!», упражнения 3–4 (стр. 281)")
    ln()
    ln("```text")
    ln(sit3_p281)
    ln("```")
    ln()
    ln(
        "*Роль А / Б:* Прочитайте текст с пропусками и фразы из рамки; "
        "проговорите варианты глаголов."
    )
    ln()
    ln("---")
    ln()

    ln(
        "#### Ситуация 4 — «Είμαι όλος αυτιά», B32–B33, упражнения 5–6 (стр. 282)"
    )
    ln()
    ln("```text")
    ln(sit4_p282)
    ln("```")
    ln()
    ln(
        "*Роль А / Б:* Прослушайте (или прочитайте инструкции к) B32 и B33; "
        "озвучьте списки документов и порядок действий (Λουντμίλας)."
    )
    ln()
    ln("---")
    ln()

    ln(
        "#### Ситуация 5 — «Πάμε πάλι!», упр. 7: ξενοδοχεία, таблица характеристик (стр. 283)"
    )
    ln()
    ln("```text")
    ln(sit5_p283_hotels)
    ln("```")
    ln()
    ln(
        "*Роль А / Б:* Прочитайте рекламы отелей; отметьте и проговорите "
        "двенадцать характеристик (кроме примера)."
    )
    ln()
    ln("---")
    ln()

    ln(
        "#### Ситуация 6 — «Πάμε πάλι!», упр. 8: вакансии и письмо (стр. 284)"
    )
    ln()
    ln("```text")
    ln(sit6_p284_jobs)
    ln("```")
    ln()
    ln(
        "*Роль А / Б:* Озвучьте объявления о работе; обсудите, куда бы вы "
        "написали; начните черновик письма вслух."
    )
    ln()
    ln("---")
    ln()

    ln(
        "#### Ситуация 7 — Γράψε-σβήσε 9–10, «Έχω τον λόγο» 1.1, роли 1.2 (стр. 285–286)"
    )
    ln()
    ln("```text")
    ln(sit7_p285_286)
    ln("```")
    ln()
    ln(
        "*Роль А / Б:* Проговорите формы в письме; ответьте на вопросы микрофона; "
        "сыграйте соискатель / HR по ролям 1.2."
    )
    ln()
    ln("---")
    ln()

    ln(
        "#### Ситуация 8 — «Παίζω έναν ρόλο», упр. 13, логотипы δημοσίων υπηρεσιών (стр. 287)"
    )
    ln()
    ln("```text")
    ln(sit8_p287)
    ln("```")
    ln()
    ln(
        "*Роль А / Б:* Прочитайте роли про очередь в δημόσια υπηρεσία; разыграйте диалог "
        "друзей; проговорите подписи к логотипам (ΚΕΠ, ΙΚΑ, ΕΛΤΑ и др.)."
    )

    ln()
    ln(
        "### Блок 2: Шпаргалка — προστακτική в рекламных текстах ξενοδοχείων (фрагмент упр. 7)"
    )
    ln()
    ln("```text")
    ln(pos_imper_hotels)
    ln("```")
    ln()

    ln("### Блок 3: Таблицы и лексика для повторения")
    ln()
    ln("#### Τύπος Α, ανώμαλα ρήματα — ενεστώτας, υποτακτική, προστακτική")
    ln()
    ln("```text")
    ln(gia_typoi_a_irreg)
    ln("```")
    ln()
    ln("#### Τύπος Β, τόνος, θηλυκά -η / λεξιλόγιο κατά κατάληξη")
    ln()
    ln("```text")
    ln(gia_typoi_b_fem)
    ln("```")
    ln()
    ln("#### «Έχω τον λόγο» — вопросы для ответа по микрофону (только 1.1)")
    ln()
    ln("```text")
    ln(gia_echo_logos)
    ln("```")

    out_path.write_text("\n".join(out) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
