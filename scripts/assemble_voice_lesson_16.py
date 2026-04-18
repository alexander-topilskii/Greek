"""Assemble book/pages/lesson_16/lesson_voice_16/voice_lesson_16.md from lesson_16_digitized.md slices."""

from __future__ import annotations

from pathlib import Path


def main() -> None:
    repo = Path(__file__).resolve().parents[1]
    digit_path = repo / "book/pages/lesson_16/lesson_digitized/lesson_16_digitized.md"
    out_path = repo / "book/pages/lesson_16/lesson_voice_16/voice_lesson_16.md"
    out_path.parent.mkdir(parents=True, exist_ok=True)

    lines = digit_path.read_text(encoding="utf-8").splitlines()
    ANCHOR_LINE_BASE = 34
    _cur_anchor = next(i for i, ln in enumerate(lines) if '<a id="' in ln)
    _slice_shift = ANCHOR_LINE_BASE - _cur_anchor

    def sl(a: int, b: int) -> str:
        return "\n".join(lines[a - _slice_shift : b - _slice_shift]).rstrip()

    mic = chr(0x1F399)
    house = chr(0x1F3E0)
    book = chr(0x1F4DA)
    page = chr(0x1F4C4)
    zap = chr(0x26A1)

    # l16p212@34 … l16p231@1379, EOF len(lines)
    frame_b18 = sl(34, 136)
    seira_walk_214_215 = sl(136, 256)
    b19_walk_216_217 = sl(256, 387)
    bouzoukia_walk_218_219 = sl(387, 474)
    gia_typoi_exercises = sl(474, 684)
    exercises_14_15_16_17 = sl(684, 855)
    travel_b20_18 = sl(855, 1020)
    rest_19_through_31 = sl(1020, len(lines))

    pos_lene_coffee = sl(90, 101)
    pos_lene_cinema = sl(290, 298)
    pos_lene_trip = sl(901, 925)

    gia_mellon_na_typoi_a = sl(480, 598)
    gia_typoi_b_negation = sl(605, 627)

    out: list[str] = []

    def ln(s: str = "") -> None:
        out.append(s)

    ln(f"# {mic} Голосовой урок 16 (по оцифровке главы)")
    ln()
    ln("### Блок 1: Коммуникативные ситуации и ролевые игры")
    ln()

    ln(
        "#### Ситуация 1 — «Πάμε βόλτα;», B18 (καφές), "
        "упр. 1, шпаргалка «Πώς το λένε»"
    )
    ln()
    ln("```text")
    ln(frame_b18)
    ln("```")
    ln()
    ln(
        "*Роль А / Б:* Разыграйте диалог B18 (διάλειμμα / τάξη); "
        "сопоставьте фразы в упр. 1; повторите шпаргалку «Πώς το λένε» после диалога."
    )
    ln()
    ln("---")
    ln()

    ln(
        "#### Ситуация 2 — «\u0397 σειρά μου τώρα», упр. 2–3, "
        "«Πάμε βόλτα;» упр. 4–6"
    )
    ln()
    ln("```text")
    ln(seira_walk_214_215)
    ln("```")
    ln()
    ln(
        "*Роль А / Б:* Упорядочьте абзацы в 2; заполните пропуски в 3; "
        "выполните упр. 4–6 (в т. ч. верно / неверно)."
    )
    ln()
    ln("---")
    ln()

    ln(
        "#### Ситуация 3 — «\u0398\u03ad\u03bb\u03b5\u03c4\u03b5 \u03bd\u03b1 \u03b4\u03bf\u03cd\u03bc\u03b5 "
        "\u03ba\u03b1\u03bc\u03b9\u03ac \u03c4\u03b1\u03b9\u03bd\u03af\u03b1;», B19, "
        "«Πάμε βόλτα;» упр. 7–9"
    )
    ln()
    ln("```text")
    ln(b19_walk_216_217)
    ln("```")
    ln()
    ln(
        "*Роль А / Б:* Прослушайте / разыграйте B19; обсудите планы (кино, театр, μπουζούκια); "
        "сделайте упр. 7–9; повторите вторую шпаргалку «Πώς το λένε»."
    )
    ln()
    ln("---")
    ln()

    ln(
        "#### Ситуация 4 — «Πάμε στα μπουζούκια;», упр. 10"
    )
    ln()
    ln("```text")
    ln(bouzoukia_walk_218_219)
    ln("```")
    ln()
    ln(
        "*Роль А / Б:* Разыграйте сцену про μπουζούκια; выполните упр. 10."
    )
    ln()
    ln("---")
    ln()

    ln(
        "#### Ситуация 5 — «Για δες» τύπος \u0391, τύποι \u03921+\u03922, упр. 1.1–1.3"
    )
    ln()
    ln("```text")
    ln(gia_typoi_exercises)
    ln("```")
    ln()
    ln(
        "*Роль А / Б:* Прочитайте таблицы θα / να (τύπος \u0391 и \u03921+\u03922); "
        "заполните 1.1–1.3 (πρέπει, θέλω, μπορώ + να)."
    )
    ln()
    ln("---")
    ln()

    ln(
        "#### Ситуация 6 — упр. 14–15, 1.6–1.7"
    )
    ln()
    ln("```text")
    ln(exercises_14_15_16_17)
    ln("```")
    ln()
    ln(
        "*Роль А / Б:* Преобразуйте пары «хочу / должен» в 14; "
        "заполните пропуски в 15; выполните 1.6–1.7 (να + глагол)."
    )
    ln()
    ln("---")
    ln()

    ln(
        "#### Ситуация 7 — «\u0398\u03ad\u03bb\u03c9 \u03bd\u03b1 \u03ba\u03ac\u03bd\u03c9 "
        "\u03ad\u03bd\u03b1 \u03bc\u03b5\u03b3\u03ac\u03bb\u03bf \u03c4\u03b1\u03be\u03af\u03b4\u03b9», B20, упр. 1.8"
    )
    ln()
    ln("```text")
    ln(travel_b20_18)
    ln("```")
    ln()
    ln(
        "*Роль А / Б:* Прослушайте / обсудите диалог про туры; "
        "выполните упр. 1.8; выучите третью шпаргалку «Πώς το λένε» (κίτρινο / πράσινο / μπλε)."
    )
    ln()
    ln("---")
    ln()

    ln(
        "#### Ситуация 8 — упр. 1.9–2.9, 3.1 (роли, письмо, B21)"
    )
    ln()
    ln("```text")
    ln(rest_19_through_31)
    ln("```")
    ln()
    ln(
        "*Роль А / Б:* Заполните таблицы и пропуски 1.9–2.7; "
        "напишите письмо 2.8; выполните 2.9; прослушайте B21 и упр. 2.5–2.6; "
        "роль 3.1 (σερβιτόρος / πελάτης)."
    )

    ln()
    ln("### Блок 2: Шпаргалка («Πώς το λένε») — после B18, B19 и блока про ταξίδι")
    ln()
    ln("```text")
    ln(pos_lene_coffee)
    ln()
    ln(pos_lene_cinema)
    ln()
    ln(pos_lene_trip)
    ln("```")
    ln()

    ln("### Блок 3: Тематический словарь и образцы")
    ln()
    ln("#### Μέλλων и υποτακτική (τύπος Α): θα / να")
    ln()
    ln("```text")
    ln(gia_mellon_na_typoi_a)
    ln("```")
    ln()
    ln(
        "#### Τύποι \u03921 + \u03922: \u0386\u03c1\u03bd\u03b7\u03c3\u03b7 με «θα» και «να»"
    )
    ln()
    ln("```text")
    ln(gia_typoi_b_negation)
    ln("```")

    out_path.write_text("\n".join(out) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
