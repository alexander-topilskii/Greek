"""Assemble book/pages/lesson_19/lesson_voice_19/voice_lesson_19.md from lesson_19_digitized.md slices."""

from __future__ import annotations

from pathlib import Path


def main() -> None:
    repo = Path(__file__).resolve().parents[1]
    digit_path = repo / "book/pages/lesson_19/lesson_digitized/lesson_19_digitized.md"
    out_path = repo / "book/pages/lesson_19/lesson_voice_19/voice_lesson_19.md"
    out_path.parent.mkdir(parents=True, exist_ok=True)

    lines = digit_path.read_text(encoding="utf-8").splitlines()

    def sl(a: int, b: int) -> str:
        return "\n".join(lines[a:b]).rstrip()

    mic = chr(0x1F399)
    house = chr(0x1F3E0)
    book = chr(0x1F4DA)
    page = chr(0x1F4C4)
    zap = chr(0x26A1)

    # l19p262@30 … l19p277@1069, EOF len(lines)
    sit1_intro_bank = sl(30, 153)
    sit2_bank_gia_roles = sl(153, 211)
    sit3_post_b28 = sl(211, 289)
    sit4_post_gia_ex = sl(289, 362)
    sit5_p267_268 = sl(362, 459)
    sit6_p269 = sl(459, 570)
    sit7_p270_271 = sl(570, 722)
    sit8_rest = sl(722, len(lines))

    pos_lene_bank = sl(119, 128)
    pos_lene_post = sl(247, 267)
    pos_lene_police = sl(434, 442)
    pos_lene_dimos = sl(632, 640)

    gia_bank = sl(161, 177)
    gia_post = sl(295, 325)
    gia_oti_pos = sl(542, 564)
    gia_feminine = sl(728, 788)

    out: list[str] = []

    def ln(s: str = "") -> None:
        out.append(s)

    ln(f"# {mic} Голосовой урок 19 (по оцифровке главы)")
    ln()
    ln(
        f"**[{house} Readme](../../../../Readme.md) → [{book} content_19.md](../content_19.md) "
        f"→ {page} `lesson_voice_19/voice_lesson_19.md`**"
    )
    ln()
    ln(f"| {zap} Быстрые ссылки |                                                                    |")
    ln("|------------------|--------------------------------------------------------------------|")
    ln(f"| {book} Урок          | [content_19.md](../content_19.md)                                    |")
    ln(f"| {page} Оцифровка     | [lesson_19_digitized.md](../lesson_digitized/lesson_19_digitized.md) |")
    ln()
    ln("### Блок 1: Коммуникативные ситуации и ролевые игры")
    ln()

    ln(
        "#### Ситуация 1 — «Περιμένετε στην ουρά», вводные фразы, коллаж, B27 (τράπεζα), «Πώς το λένε»"
    )
    ln()
    ln("```text")
    ln(sit1_intro_bank)
    ln("```")
    ln()
    ln(
        "*Роль А / Б:* Разыграйте диалог B27 (Υπάλληλος / Πάμπλο); "
        "проговорите фразы из двух колонок; повторите «Πώς το λένε» про τράπεζα."
    )
    ln()
    ln("---")
    ln()

    ln(
        "#### Ситуация 2 — «Για δες» (τράπεζα), «Η σειρά μου τώρα», ρόλοι (άνοιγμα λογαριασμού)"
    )
    ln()
    ln("```text")
    ln(sit2_bank_gia_roles)
    ln("```")
    ln()
    ln(
        "*Роль А / Б:* Прочитайте лексику τράπεζας; ответьте на микрофон; "
        "сыграйте клиент / υπάλληλος по ролям Α / Β."
    )
    ln()
    ln("---")
    ln()

    ln(
        "#### Ситуация 3 — B28 στο ταχυδρομείο, «Πώς το λένε», упр. 4 (Σωστό/Λάθος)"
    )
    ln()
    ln("```text")
    ln(sit3_post_b28)
    ln("```")
    ln()
    ln(
        "*Роль А / Б:* Разыграйτε Μαρίνα / υπάλληλος; повторите жёлтый/синий/зелёный блоки «Πώς το λένε»; "
        "оцените утверждения в 4."
    )
    ln()
    ln("---")
    ln()

    ln(
        "#### Ситуация 4 — «Για δες» (ΕΛ.Τ.Α.), «Η σειρά μου τώρα», упр. 5–6"
    )
    ln()
    ln("```text")
    ln(sit4_post_gia_ex)
    ln("```")
    ln()
    ln(
        "*Роль А / Б:* Проговорите услуги ταχυδρομείου по спискам; ответьте в 5; составьте диалог ΔΕΗ в 6."
    )
    ln()
    ln("---")
    ln()

    ln(
        "#### Ситуация 5 — упр. 7, B29, «Έχασα τα χαρτιά μου», «Πώς το λένε», упр. 8"
    )
    ln()
    ln("```text")
    ln(sit5_p267_268)
    ln("```")
    ln()
    ln(
        "*Роль А / Б:* Выполните цепочку в 7; разыграйте αστυνομία; "
        "повторите «Πώς το λένε» про δήλωση и διαβατήριο; заполните текст в 8."
    )
    ln()
    ln("---")
    ln()

    ln(
        "#### Ситуация 6 — «Για δες» (στην αστυνομία), упр. 9–11, «ότι / πως»"
    )
    ln()
    ln("```text")
    ln(sit6_p269)
    ln("```")
    ln()
    ln(
        "*Роль А / Б:* Озвучьте процедуры в αστυνομία; ответьте на вопросы в 9; "
        "сыграйте кражу сумки в 10; свяжите предложения в 11; прочитайте таблицу ρημάτων с ότι/πως."
    )
    ln()
    ln("---")
    ln()

    ln(
        "#### Ситуация 7 — B30 στον δήμο, «Πώς το λένε», упр. 1.2–1.3, «Για δες» (άδεια διαμονής)"
    )
    ln()
    ln("```text")
    ln(sit7_p270_271)
    ln("```")
    ln()
    ln(
        "*Роль А / Б:* Разыграйте Γκαμάλ / υπάλληλος; повторите речевые клише; "
        "ответьте на вопросы в 1.2; объясните схему документов в «Για δες»."
    )
    ln()
    ln("---")
    ln()

    ln(
        "#### Ситуация 8 — «Για δες» (-η / -εις), упр. 14–19, ΚΕΠ, γράμμα, «Διαλέγω το σωστό»"
    )
    ln()
    ln("```text")
    ln(sit8_rest)
    ln("```")
    ln()
    ln(
        "*Роль А / Б:* Прочитайте таблицы склонения и список слов; выполните упражнения на -ση/-ξη/-ψη; "
        "ознакомьтесь с ΚΕΠ; прослушайте B31; подготовьте γράμμα и задание 19."
    )

    ln()
    ln(
        "### Блок 2: Шпаргалка («Πώς το λένε») — τράπεζα, ταχυδρομείο, αστυνομία, δήμος"
    )
    ln()
    ln("```text")
    ln(pos_lene_bank)
    ln()
    ln(pos_lene_post)
    ln()
    ln(pos_lene_police)
    ln()
    ln(pos_lene_dimos)
    ln("```")
    ln()

    ln("### Блок 3: Тематический словарь и образцы")
    ln()
    ln("#### Για δες — τράπεζα (λογαριασμός, κατάθεση, συνάλλαγμα)")
    ln()
    ln("```text")
    ln(gia_bank)
    ln("```")
    ln()
    ln("#### Για δες — στο ταχυδρομείο (ΕΛ.Τ.Α.)")
    ln()
    ln("```text")
    ln(gia_post)
    ln("```")
    ln()
    ln("#### Ρήματα με «ότι» ή «πως»")
    ln()
    ln("```text")
    ln(gia_oti_pos)
    ln("```")
    ln()
    ln("#### Θηλυκά σε -η / πληθυντικός σε -εις (-ση, -ξη, -ψη)")
    ln()
    ln("```text")
    ln(gia_feminine)
    ln("```")

    out_path.write_text("\n".join(out) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
