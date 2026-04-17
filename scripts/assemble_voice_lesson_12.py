"""Assemble book/pages/lesson_12/lesson_voice_12/voice_lesson_12.md from lesson_12_digitized.md slices."""

from __future__ import annotations

from pathlib import Path


def main() -> None:
    repo = Path(__file__).resolve().parents[1]
    digit_path = repo / "book/pages/lesson_12/lesson_digitized/lesson_12_digitized.md"
    out_path = repo / "book/pages/lesson_12/lesson_voice_12/voice_lesson_12.md"
    out_path.parent.mkdir(parents=True, exist_ok=True)

    lines = digit_path.read_text(encoding="utf-8").splitlines()

    def sl(a: int, b: int) -> str:
        return "\n".join(lines[a:b]).rstrip()

    mic = chr(0x1F399)
    house = chr(0x1F3E0)
    book = chr(0x1F4DA)
    page = chr(0x1F4C4)
    zap = chr(0x26A1)
    gem = chr(0x1F48E)

    # l12p150@31 … l12p165@903, EOF 935
    intro_b5 = sl(31, 130)
    aorist_exercises_2_4 = sl(131, 320)
    imoun_piga_things_vaggelis = sl(320, 456)
    cafe_b7_aorist_b1b2 = sl(456, 574)
    exercises_16_18 = sl(574, 713)
    eida_irregular_acc = sl(713, 784)
    b8_role_b9_paros = sl(784, 876)
    story_write_fix = sl(876, 935)

    pos_lene_b5 = sl(89, 106)
    pos_lene_cafe = sl(493, 500)

    gia_aorist_tora = sl(146, 209)
    gia_paron_parelthon = sl(301, 314)
    gia_imoun_piga = sl(337, 353)
    gia_b_aorist = sl(532, 569)
    gia_kano_troo = sl(660, 675)
    gia_eida_acc = sl(718, 728)

    out: list[str] = []

    def ln(s: str = "") -> None:
        out.append(s)

    ln(f"# {mic} \u0413\u043e\u043b\u043e\u0441\u043e\u0432\u043e\u0439 \u0443\u0440\u043e\u043a 12 (\u043f\u043e \u043e\u0446\u0438\u0444\u0440\u043e\u0432\u043a\u0435 \u0433\u043b\u0430\u0432\u044b)")
    ln()
    ln(
        f"**[{house} Readme](../../../../Readme.md) \u2192 [{book} content_12.md](../content_12.md) "
        f"\u2192 {page} `lesson_voice_12/voice_lesson_12.md`**"
    )
    ln()
    ln(f"| {zap} \u0411\u044b\u0441\u0442\u0440\u044b\u0435 \u0441\u0441\u044b\u043b\u043a\u0438 |                                                                    |")
    ln("|------------------|--------------------------------------------------------------------|")
    ln(f"| {book} \u0423\u0440\u043e\u043a          | [content_12.md](../content_12.md)                                    |")
    ln(f"| {page} \u041e\u0446\u0438\u0444\u0440\u043e\u0432\u043a\u0430     | [lesson_12_digitized.md](../lesson_digitized/lesson_12_digitized.md) |")
    ln(f"| {gem} \u0421\u0443\u0442\u044c \u0443\u0440\u043e\u043a\u0430    | [essence_12/essence_12.md](../essence_12/essence_12.md)                                    |")
    ln(
        f"| {mic} Voice (HTML)  | [voice_lesson_12.html](voice_lesson_12.html) · "
        f"[essence_12.html](../essence_12.html)                                |"
    )
    ln()
    ln("### \u0411\u043b\u043e\u043a 1: \u041a\u043e\u043c\u043c\u0443\u043d\u0438\u043a\u0430\u0442\u0438\u0432\u043d\u044b\u0435 \u0441\u0438\u0442\u0443\u0430\u0446\u0438\u0438 \u0438 \u0440\u043e\u043b\u0435\u0432\u044b\u0435 \u0438\u0433\u0440\u044b")
    ln()

    ln(
        "#### \u0421\u0438\u0442\u0443\u0430\u0446\u0438\u044f 1 \u2014 \u00ab\u0388\u03bd\u03b1 \u03c4\u03b1\u03be\u03af\u03b4\u03b9\u00bb: \u0440\u0430\u043c\u043a\u0430, B5, "
        "\u0448\u043f\u0430\u0440\u0433\u0430\u043b\u043a\u0430, \u0432\u0435\u0440\u043d\u043e / \u043d\u0435\u0432\u0435\u0440\u043d\u043e"
    )
    ln()
    ln("```text")
    ln(intro_b5)
    ln("```")
    ln()
    ln(
        "*\u0420\u043e\u043b\u044c \u0410 / \u0411:* \u039c\u03b5\u03bb\u03ad\u03ba \u0438 \u0391\u03c1\u03bb\u03ad\u03c4\u03b1 \u2014 "
        "\u0434\u0438\u0430\u043b\u043e\u0433 \u043f\u043e \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u0443; "
        "\u0437\u0430\u0442\u0435\u043c \u043e\u0431\u0441\u0443\u0434\u0438\u0442\u0435 \u0443\u0442\u0432\u0435\u0440\u0436\u0434\u0435\u043d\u0438\u044f \u0438\u0437 \u0442\u0430\u0431\u043b\u0438\u0446\u044b 1."
    )
    ln()
    ln("---")
    ln()

    ln(
        "#### \u0421\u0438\u0442\u0443\u0430\u0446\u0438\u044f 2 \u2014 \u0391\u03cc\u03c1\u03b9\u03c3\u03c4\u03bf\u03c2: "
        "\u0444\u043e\u0440\u043c\u044b, \u0443\u043f\u0440\u0430\u0436\u043d\u0435\u043d\u0438\u044f 2\u20134, "
        "\u043f\u0440\u043e\u0448\u0435\u0434\u0448\u0435\u0435 / \u043d\u0430\u0441\u0442\u043e\u044f\u0449\u0435\u0435"
    )
    ln()
    ln("```text")
    ln(aorist_exercises_2_4)
    ln("```")
    ln()
    ln(
        "*\u0420\u043e\u043b\u044c \u0410 / \u0411:* \u041e\u0442\u0432\u0435\u0442\u044b \u043d\u0430 \u0432\u043e\u043f\u0440\u043e\u0441\u044b "
        "\u00ab\u03a0\u03bf\u03cd \u03ae\u03c3\u03bf\u03c5\u03bd;\u00bb \u0432 \u0440\u0430\u0437\u043d\u044b\u0435 \u0432\u0440\u0435\u043c\u0435\u043d\u0430; "
        "\u0437\u0430\u043f\u043e\u043b\u043d\u044f\u0439\u0442\u0435 \u043f\u0440\u043e\u043f\u0443\u0441\u043a\u0438 \u0430\u043e\u0440\u0438\u0441\u0442\u043e\u043c \u043f\u043e \u043e\u0431\u0440\u0430\u0437\u0446\u0430\u043c."
    )
    ln()
    ln("---")
    ln()

    ln(
        "#### \u0421\u0438\u0442\u0443\u0430\u0446\u0438\u044f 3 \u2014 \u00ab\u03a4\u03b1 \u03c0\u03c1\u03ac\u03b3\u03bc\u03b1\u03c4\u03b1 \u03b1\u03bb\u03bb\u03ac\u03b6\u03bf\u03c5\u03bd\u00bb: "
        "\u0434\u0430\u0442\u044b, \u03ae\u03bc\u03bf\u03c5\u03bd / \u03c0\u03ae\u03b3\u03b1, "
        "\u0392\u03b1\u03b3\u03b3\u03ad\u03bb\u03b7\u03c2, B6, \u043f\u0438\u0441\u044c\u043c\u043e e-mail"
    )
    ln()
    ln("```text")
    ln(imoun_piga_things_vaggelis)
    ln("```")
    ln()
    ln(
        "*\u0420\u043e\u043b\u044c \u0410 / \u0411:* \u0420\u0430\u0441\u0441\u043a\u0430\u0436\u0438\u0442\u0435 \u0432\u0447\u0435\u0440\u0430 / \u0441\u0435\u0433\u043e\u0434\u043d\u044f "
        "\u043f\u043e \u0442\u0430\u0431\u043b\u0438\u0446\u0435 \u043f\u0440\u043e\u0448\u043b\u043e\u0433\u043e; "
        "\u0440\u0430\u0437\u044b\u0433\u0440\u0430\u0439\u0442\u0435 \u0446\u0435\u043f\u043e\u0447\u043a\u0443 \u0392\u03b1\u03b3\u03b3\u03ad\u03bb\u03b7; "
        "\u0443\u0441\u0442\u043d\u043e \u043e\u0442\u0432\u0435\u0442\u044b B6 \u0438 \u043f\u043b\u0430\u043d \u043f\u0438\u0441\u044c\u043c\u0430 12."
    )
    ln()
    ln("---")
    ln()

    ln(
        "#### \u0421\u0438\u0442\u0443\u0430\u0446\u0438\u044f 4 \u2014 B7 \u0432 \u043a\u0430\u0444\u0435\u043d\u0435\u0439\u043e, "
        "\u0442\u0438\u043f B1\u2013B2 \u0430\u043e\u0440\u0438\u0441\u0442\u0430 (-\u03b7\u03c3\u03b1 / -\u03b1\u03c3\u03b1 / -\u03b5\u03c3\u03b1)"
    )
    ln()
    ln("```text")
    ln(cafe_b7_aorist_b1b2)
    ln("```")
    ln()
    ln(
        "*\u0420\u043e\u043b\u044c \u0410 / \u0411:* \u03a0\u03b1\u03bd\u03b1\u03b3\u03b9\u03ce\u03c4\u03b7\u03c2, \u039c\u03b5\u03bb\u03ad\u03ba, "
        "\u0395\u03c1\u03b2\u03af\u03bd, \u0391\u03c1\u03bb\u03ad\u03c4\u03b1 \u2014 \u043e \u043f\u043e\u0435\u0437\u0434\u043a\u0435 \u0434\u043e\u043c\u043e\u0439; "
        "\u0437\u0430\u0442\u0435\u043c \u0442\u0440\u0435\u043d\u0438\u0440\u0443\u0439\u0442\u0435 \u0430\u043e\u0440\u0438\u0441\u0442 "
        "\u043d\u0430 -\u03b7\u03c3\u03b1 / -\u03b1\u03c3\u03b1 / -\u03b5\u03c3\u03b1 \u043f\u043e \u0442\u0430\u0431\u043b\u0438\u0446\u0435 \u0438 \u043f\u0440\u0438\u043c\u0435\u0440\u0430\u043c."
    )
    ln()
    ln("---")
    ln()

    ln(
        "#### \u0421\u0438\u0442\u0443\u0430\u0446\u0438\u044f 5 \u2014 \u0423\u043f\u0440\u0430\u0436\u043d\u0435\u043d\u0438\u044f 1.6\u20131.8, "
        "\u043d\u0435\u043f\u0440\u0430\u0432\u0438\u043b\u044c\u043d\u044b\u0435 \u0433\u043b\u0430\u0433\u043e\u043b\u044b, "
        "\u03ba\u03ac\u03bd\u03c9 / \u03c4\u03c1\u03ce\u03c9 / \u03b2\u03bb\u03ad\u03c0\u03c9"
    )
    ln()
    ln("```text")
    ln(exercises_16_18)
    ln("```")
    ln()
    ln(
        "*\u0420\u043e\u043b\u044c \u0410 / \u0411:* \u0421\u043e\u0441\u0442\u0430\u0432\u044c\u0442\u0435 \u0432\u043e\u043f\u0440\u043e\u0441\u044b \u0438 \u043e\u0442\u0432\u0435\u0442\u044b "
        "\u0434\u043b\u044f \u0441\u043e\u043f\u043e\u0441\u0442\u0430\u0432\u043b\u0435\u043d\u0438\u044f 1.7; "
        "\u043f\u0440\u043e\u0433\u043e\u0432\u043e\u0440\u0438\u0442\u0435 \u0444\u043e\u0440\u043c\u044b \u00ab\u03ad\u03ba\u03b1\u03bd\u03b1, \u03ad\u03c6\u03b1\u03b3\u03b1, \u03b5\u03af\u03b4\u03b1\u00bb \u0432 \u0434\u0438\u0430\u043b\u043e\u0433\u0435."
    )
    ln()
    ln("---")
    ln()

    ln(
        "#### \u0421\u0438\u0442\u0443\u0430\u0446\u0438\u044f 6 \u2014 \u03b5\u03af\u03b4\u03b1 + "
        "\u043c\u0435\u0441\u0442\u043e\u0438\u043c\u0435\u043d\u0438\u044f \u0432 \u0432\u0438\u043d."
    )
    ln()
    ln("```text")
    ln(eida_irregular_acc)
    ln("```")
    ln()
    ln(
        "*\u0420\u043e\u043b\u044c \u0410 / \u0411:* \u0417\u0430\u043c\u0435\u043d\u044f\u0439\u0442\u0435 \u0438\u043c\u0435\u043d\u0430 "
        "\u0432 \u043e\u0442\u0440\u044b\u0432\u043a\u0430\u0445 2.1\u20132.2; "
        "\u043f\u0440\u043e\u0432\u0435\u0440\u044c\u0442\u0435 \u0442\u0430\u0431\u043b\u0438\u0446\u0443 \u0441 \u039c\u03b5 / \u03a4\u03bf\u03bd / \u2026"
    )
    ln()
    ln("---")
    ln()

    ln(
        "#### \u0421\u0438\u0442\u0443\u0430\u0446\u0438\u044f 7 \u2014 B8, \u0440\u043e\u043b\u044c, "
        "\u0430\u0443\u0434\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 B9 (\u03a0\u03ac\u03c1\u03bf\u03c2)"
    )
    ln()
    ln("```text")
    ln(b8_role_b9_paros)
    ln("```")
    ln()
    ln(
        "*\u0420\u043e\u043b\u044c \u0410 / \u0411:* \u00ab\u03a0\u03ce\u03c2 \u03c4\u03b1 \u03c0\u03ad\u03c1\u03b1\u03c3\u03b5\u03c2;\u00bb; "
        "\u0437\u0430\u0442\u0435\u043c \u0443\u0441\u0442\u043d\u043e \u043f\u043e \u0441\u043b\u0443\u0445\u0443 B9 "
        "\u043e\u043f\u0438\u0448\u0438\u0442\u0435 \u043c\u0430\u0440\u0448\u0440\u0443\u0442 \u043f\u043e \u041f\u0430\u0440\u043e\u0441\u0443."
    )
    ln()
    ln("---")
    ln()

    ln(
        "#### \u0421\u0438\u0442\u0443\u0430\u0446\u0438\u044f 8 \u2014 \u0422\u0435\u043a\u0441\u0442 \u043f\u0440\u043e \u0420\u043e\u0434\u043e\u0441, "
        "\u00ab\u0393\u03c1\u03ac\u03c8\u03b5-\u03c3\u03b2\u03ae\u03c3\u03b5\u00bb, \u0438\u0441\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u043e\u0448\u0438\u0431\u043e\u043a 2.9"
    )
    ln()
    ln("```text")
    ln(story_write_fix)
    ln("```")
    ln()
    ln(
        "*\u0417\u0430\u0434\u0430\u043d\u0438\u0435:* \u043f\u0440\u043e\u0447\u0438\u0442\u0430\u0439\u0442\u0435 \u0438\u0441\u0442\u043e\u0440\u0438\u044e "
        "\u0438 \u043d\u0430\u0439\u0434\u0438\u0442\u0435 \u0432\u0441\u0442\u0430\u0432\u043a\u0438 \u0438\u0437 \u0442\u0430\u0431\u043b\u0438\u0446\u044b; "
        "\u043f\u043b\u0430\u043d \u0442\u0435\u043a\u0441\u0442\u0430 2.8; "
        "\u0438\u0441\u043f\u0440\u0430\u0432\u044c\u0442\u0435 \u0433\u043b\u0430\u0433\u043e\u043b\u044b \u0432 \u043f\u0438\u0441\u044c\u043c\u0435 \u0412\u03ad\u03c1\u03b1."
    )

    ln()
    ln("### \u0411\u043b\u043e\u043a 2: \u0428\u043f\u0430\u0440\u0433\u0430\u043b\u043a\u0430 (\u03a0\u03ce\u03c2 \u03c4\u03bf \u03bb\u03ad\u03bd\u03b5;)")
    ln()
    ln("*\u0414\u0432\u0430 \u0444\u0440\u0430\u0433\u043c\u0435\u043d\u0442\u0430: \u043f\u043e\u0441\u043b\u0435 B5 \u0438 \u043f\u043e\u0441\u043b\u0435 B7.*")
    ln()
    ln("```text")
    ln(pos_lene_b5)
    ln()
    ln(pos_lene_cafe)
    ln("```")
    ln()

    ln("### \u0411\u043b\u043e\u043a 3: \u0422\u0435\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u0441\u043b\u043e\u0432\u0430\u0440\u044c \u0438 \u043e\u0431\u0440\u0430\u0437\u0446\u044b")
    ln()
    ln("#### \u0391\u03cc\u03c1\u03b9\u03c3\u03c4\u03bf\u03c2: \u03c4\u03ce\u03c1\u03b1 / \u03c7\u03c4\u03b5\u03c2, \u043a\u043e\u0440\u043d\u0438 \u0438 \u0443\u0434\u0430\u0440\u0435\u043d\u0438\u0435")
    ln()
    ln("```text")
    ln(gia_aorist_tora)
    ln("```")
    ln()
    ln("#### \u041f\u0440\u043e\u0448\u043b\u043e\u0435 \u0438 \u043d\u0430\u0441\u0442\u043e\u044f\u0449\u0435\u0435 \u0432\u0440\u0435\u043c\u044f")
    ln()
    ln("```text")
    ln(gia_paron_parelthon)
    ln("```")
    ln()
    ln("#### \u03ae\u03bc\u03bf\u03c5\u03bd / \u03c0\u03ae\u03b3\u03b1")
    ln()
    ln("```text")
    ln(gia_imoun_piga)
    ln("```")
    ln()
    ln("#### \u0422\u0438\u043f B1\u2013B2: -\u03b7\u03c3\u03b1, -\u03b1\u03c3\u03b1, -\u03b5\u03c3\u03b1")
    ln()
    ln("```text")
    ln(gia_b_aorist)
    ln("```")
    ln()
    ln("#### \u03ba\u03ac\u03bd\u03c9, \u03c4\u03c1\u03ce\u03c9, \u03c0\u03af\u03bd\u03c9, \u03b2\u03bb\u03ad\u03c0\u03c9")
    ln()
    ln("```text")
    ln(gia_kano_troo)
    ln("```")
    ln()
    ln("#### \u03b5\u03af\u03b4\u03b1 + \u0430\u0438\u0442. \u043c\u0435\u0441\u0442\u043e\u0438\u043c\u0435\u043d\u0438\u044f")
    ln()
    ln("```text")
    ln(gia_eida_acc)
    ln("```")

    out_path.write_text("\n".join(out) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
