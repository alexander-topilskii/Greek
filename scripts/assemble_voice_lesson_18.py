"""Assemble book/pages/lesson_18/lesson_voice_18/voice_lesson_18.md from lesson_18_digitized.md slices."""

from __future__ import annotations

from pathlib import Path


def main() -> None:
    repo = Path(__file__).resolve().parents[1]
    digit_path = repo / "book/pages/lesson_18/lesson_digitized/lesson_18_digitized.md"
    out_path = repo / "book/pages/lesson_18/lesson_voice_18/voice_lesson_18.md"
    out_path.parent.mkdir(parents=True, exist_ok=True)

    lines = digit_path.read_text(encoding="utf-8").splitlines()
    ANCHOR_LINE_BASE = 30
    _cur_anchor = next(i for i, ln in enumerate(lines) if '<a id="' in ln)
    _slice_shift = ANCHOR_LINE_BASE - _cur_anchor

    def sl(a: int, b: int) -> str:
        return "\n".join(lines[a - _slice_shift : b - _slice_shift]).rstrip()

    mic = chr(0x1F399)
    house = chr(0x1F3E0)
    book = chr(0x1F4DA)
    page = chr(0x1F4C4)
    zap = chr(0x26A1)

    # l18p246@30 … l18p261@1013, EOF len(lines)
    sit1_intro_b25_pos = sl(30, 156)
    sit2_ex1_4 = sl(156, 215)
    sit3_body_ex5_symptom = sl(215, 309)
    sit4_ex6_vocab_comic = sl(309, 392)
    sit5_ex7_8_polys = sl(392, 472)
    sit6_ex9_comparison = sl(472, 532)
    sit7_ex10_12_letter_tf = sl(532, 665)
    sit8_rest = sl(665, len(lines))

    pos_lene = sl(127, 151)

    gia_polys = sl(438, 467)
    gia_comparison = sl(506, 526)
    gia_an = sl(693, 704)

    out: list[str] = []

    def ln(s: str = "") -> None:
        out.append(s)

    ln(f"# {mic} Голосовой урок 18 (по оцифровке главы)")
    ln()
    ln("### Блок 1: Коммуникативные ситуации и ролевые игры")
    ln()

    ln(
        "#### Ситуация 1 — «Στον γιατρό», вводные фразы, B25 «Χάλια είμαι!», «Πώς το λένε»"
    )
    ln()
    ln("```text")
    ln(sit1_intro_b25_pos)
    ln("```")
    ln()
    ln(
        "*Роль А / Б:* Разыграйте диалог B25 (Παθολόγος / Μελέκ); "
        "проговорите вводные фразы; повторите «Πώς το λένε»."
    )
    ln()
    ln("---")
    ln()

    ln(
        "#### Ситуация 2 — упр. 1–4: συμπλήρωση, «Η σειρά μου τώρα», ρόλοι"
    )
    ln()
    ln("```text")
    ln(sit2_ex1_4)
    ln("```")
    ln()
    ln(
        "*Роль А / Б:* Заполните текст в 1; ответьте на микрофон в 2; расскажите о «трудном» пациенте в 3; "
        "сыграйте страх перед врачом в 4 (ρόλος Α / Β)."
    )
    ln()
    ln("---")
    ln()

    ln(
        "#### Ситуация 3 — «Για δες» (μέρη του σώματος), упр. 5, σύμπτωμα → ειδικότητα"
    )
    ln()
    ln("```text")
    ln(sit3_body_ex5_symptom)
    ln("```")
    ln()
    ln(
        "*Роль А / Б:* Назовите части тела по схеме; выполните 5; свяжите симптомы со специальностями."
    )
    ln()
    ln("---")
    ln()

    ln("#### Ситуация 4 — упр. 6, «Για δες» (σύμπτωμα, θεραπεία), κόμικ")
    ln()
    ln("```text")
    ln(sit4_ex6_vocab_comic)
    ln("```")
    ln()
    ln(
        "*Роль А / Б:* Дополните предложения в 6; прочитайте лексику по колонкам; озвучьте κόμικ."
    )
    ln()
    ln("---")
    ln()

    ln("#### Ситуация 5 — упр. 7–8, «Για δες»: επίθετο πολύς")
    ln()
    ln("```text")
    ln(sit5_ex7_8_polys)
    ln("```")
    ln()
    ln(
        "*Роль А / Б:* Составьте мини-диалоги по образцу в 7; разыграйте сцену в φαρμακείο в 8; "
        "прочитайте таблицу πολύς и примеры."
    )
    ln()
    ln("---")
    ln()

    ln("#### Ситуация 6 — упр. 9, «Για δες»: σύγκριση (πιο … από, πολύ …)")
    ln()
    ln("```text")
    ln(sit6_ex9_comparison)
    ln("```")
    ln()
    ln(
        "*Роль А / Б:* Подберите формы «πολύς» в 9; проговорите таблицы сравнения вслух."
    )
    ln()
    ln("---")
    ln()

    ln(
        "#### Ситуация 7 — упр. 10–12, «Η σειρά μου πάλι», ρόλοι, γράμμα Δημήτρη, Σωστό/Λάθος"
    )
    ln()
    ln("```text")
    ln(sit7_ex10_12_letter_tf)
    ln("```")
    ln()
    ln(
        "*Роль А / Б:* Выполните сравнения в 10; сыграйте звонок παιδιάτρου в 11; заполните таблицу по письму в 12; "
        "оцените утверждения Σωστό/Λάθος."
    )
    ln()
    ln("---")
    ln()

    ln(
        "#### Ситуация 8 — упр. 1.3–2.2: ιστορία, «Αν», συμβουλές γιατρών, B26, ομοιοπαθητική, γράμμα, λάθη"
    )
    ln()
    ln("```text")
    ln(sit8_rest)
    ln("```")
    ln()
    ln(
        "*Роль А / Б:* Продолжите историю в 1.3; потренируйте пары μέλλων/προστακτική с «Αν»; "
        "заполните советы врачей; выполните 18–21 и 2.2; подготовьте ответ на γράμμα κυρίου Ηλιόπουλου."
    )

    ln()
    ln("### Блок 2: Шпаргалка («Πώς το λένε»)")
    ln()
    ln("```text")
    ln(pos_lene)
    ln("```")
    ln()

    ln("### Блок 3: Тематический словарь и образцы")
    ln()
    ln("#### Επίθετο πολύς")
    ln()
    ln("```text")
    ln(gia_polys)
    ln("```")
    ln()
    ln("#### Σύγκριση: επιρρήματα και ανώμαλοι συγκριτικοί")
    ln()
    ln("```text")
    ln(gia_comparison)
    ln("```")
    ln()
    ln("#### Προτάσεις με Αν (μέλλων και προστακτική)")
    ln()
    ln("```text")
    ln(gia_an)
    ln("```")

    out_path.write_text("\n".join(out) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
