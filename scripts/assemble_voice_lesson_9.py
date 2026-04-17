"""Assemble book/pages/lesson_9/lesson_voice_9/voice_lesson_9.md from lesson_9_digitized.md slices."""

from __future__ import annotations

from pathlib import Path


def main() -> None:
    repo = Path(__file__).resolve().parents[1]
    digit_path = repo / "book/pages/lesson_9/lesson_digitized/lesson_9_digitized.md"
    out_path = repo / "book/pages/lesson_9/lesson_voice_9/voice_lesson_9.md"
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

    intro_frame_a54 = sl(31, 128)
    pronouns_adj_gia = sl(129, 199)
    opposites_autos_ekeinos_ex = sl(200, 308)
    clothes_a55 = sl(309, 399)
    colors_erkhomai = sl(400, 462)
    dresses_a56 = sl(463, 526)
    clothes_colors_grid = sl(527, 644)
    yparxei_aresei_roles = sl(645, 809)
    listening_write_erase = sl(810, 905)

    pos_lene_a54 = sl(95, 106)
    pos_lene_a55 = sl(373, 379)
    pos_lene_a56 = sl(499, 522)

    gia_pronouns = sl(147, 157)
    gia_adj_osi_o = sl(173, 195)
    gia_adj_osa_o = sl(217, 224)
    gia_autos_ekeinos = sl(236, 242)
    gia_colors_basic = sl(404, 414)
    gia_clothes_list = sl(531, 541)
    gia_colors_gender = sl(545, 565)
    gia_yparxei = sl(649, 669)
    gia_aresei = sl(673, 685)

    out: list[str] = []

    def ln(s: str = "") -> None:
        out.append(s)

    ln(f"# {mic} Голосовой урок 9 (по оцифровке главы)")
    ln()
    ln(
        f"**[{house} Readme](../../../../Readme.md) → [{book} content_9.md](../content_9.md) "
        f"→ {page} `lesson_voice_9/voice_lesson_9.md`**"
    )
    ln()
    ln(f"| {zap} Быстрые ссылки |                                                                    |")
    ln("|------------------|--------------------------------------------------------------------|")
    ln(f"| {book} Урок          | [content_9.md](../content_9.md)                                    |")
    ln(f"| {page} Оцифровка     | [lesson_9_digitized.md](../lesson_digitized/lesson_9_digitized.md) |")
    ln(f"| {gem} Суть урока    | [essence_9/essence_9.md](../essence_9/essence_9.md)                                    |")
    ln(
        f"| {mic} Voice (HTML)  | [voice_lesson_9.html](voice_lesson_9.html) · "
        f"[essence_9.html](../essence_9.html)                                |"
    )
    ln()
    ln("### Блок 1: Коммуникативные ситуации и ролевые игры")
    ln()

    ln("#### Ситуация 1 — Рамка урока и магазин электроники (A54)")
    ln()
    ln("*Контекст:* серая рамка с фразами, диалог про телефон, таблица «как сказать», верно/неверно.")
    ln()
    ln("```text")
    ln(intro_frame_a54)
    ln("```")
    ln()
    ln("*Роль А:* Пабло — выбираете телефон, спрашиваете цену и способ оплаты по репликам из цитаты.")
    ln()
    ln("*Роль Б:* Продавец и Никос — отвечайте по тексту, подсказывайте «карточный» вариант.")
    ln()
    ln("*Чек-фразы:* маркированный список и таблица после диалога.")
    ln()
    ln("---")
    ln()

    ln("#### Ситуация 2 — Дательные местоимения и прилагательное -ος -η -ο (\u03b1\u03ba\u03c1\u03b9\u03b2\u03cc\u03c2)")
    ln()
    ln(
        "*Контекст:* блок "
        "\u00ab\u0397 \u03c3\u03b5\u03b9\u03c1\u03ac \u03bc\u03bf\u03c5 \u03c4\u03ce\u03c1\u03b1\u00bb, "
        "\u043f\u0440\u0438\u043c\u0435\u0440\u044b \u03bc\u03bf\u03c5/\u03c3\u03bf\u03c5/\u2026, "
        "\u0443\u043f\u0440\u0430\u0436\u043d\u0435\u043d\u0438\u0435 \u043d\u0430 \u0432\u0441\u0442\u0430\u0432\u043a\u0443, "
        "\u043f\u0430\u0440\u0430\u0434\u0438\u0433\u043c\u0430 \u03b1\u03ba\u03c1\u03b9\u03b2\u03cc\u03c2."
    )
    ln()
    ln("```text")
    ln(pronouns_adj_gia)
    ln("```")
    ln()
    ln("*Роль А:* Расскажите, кому что покупаете или пишете — по цепочкам из «\u0393\u03b9\u03b1 \u03b4\u03ad\u03c2».")
    ln()
    ln("*Роль Б:* Задавайте уточнения («кому», «что»), используя формы из упражнения.")
    ln()
    ln("*Чек-фразы:* четыре строки прилагательного в трёх родах и двух числах в цитате.")
    ln()
    ln("---")
    ln()

    ln(
        "#### Ситуация 3 — \u0410\u043d\u0442\u043e\u043d\u0438\u043c\u044b, -ος -α -ο (\u03ba\u03b1\u03b9\u03bd\u03bf\u03cd\u03c1\u03b9\u03bf\u03c2), "
        "\u03b1\u03c5\u03c4\u03cc\u03c2 / \u03b5\u03ba\u03b5\u03af\u03bd\u03bf\u03c2, \u0443\u043f\u0440\u0430\u0436\u043d\u0435\u043d\u0438\u044f 4\u20135"
    )
    ln()
    ln(
        "*\u041a\u043e\u043d\u0442\u0435\u043a\u0441\u0442:* \u0441\u043f\u0438\u0441\u043a\u0438 \u043f\u0440\u043e\u0442\u0438\u0432\u043e\u043f\u043e\u043b\u043e\u0436\u043d\u043e\u0441\u0442\u0435\u0439, "
        "\u0442\u0430\u0431\u043b\u0438\u0446\u0430 \u03ba\u03b1\u03b9\u03bd\u03bf\u03cd\u03c1\u03b9\u03bf\u03c2, "
        "\u0434\u0435\u043c\u043e\u043d\u0441\u0442\u0440\u0430\u0442\u0438\u0432\u043d\u044b\u0435 \u043c\u0435\u0441\u0442\u043e\u0438\u043c\u0435\u043d\u0438\u044f, "
        "\u0437\u0430\u0434\u0430\u043d\u0438\u044f \u043d\u0430 \u0444\u043e\u0440\u043c\u044b."
    )
    ln()
    ln("```text")
    ln(opposites_autos_ekeinos_ex)
    ln("```")
    ln()
    ln(
        "*\u0420\u043e\u043b\u044c \u0410:* \u041e\u043f\u0438\u0448\u0438\u0442\u0435 \u0432\u0435\u0449\u044c \u0443 \u0432\u0438\u0442\u0440\u0438\u043d\u044b "
        "(\u00ab\u044d\u0442\u043e\u0442 \u0434\u043e\u0440\u043e\u0433\u043e\u0439 / \u0442\u043e\u0442 \u0434\u0435\u0448\u0451\u0432\u044b\u0439\u00bb) "
        "\u2014 \u0438\u0437 \u0431\u043b\u043e\u043a\u0430 \u03b1\u03c5\u03c4\u03cc\u03c2 \u00b7 \u03b5\u03ba\u03b5\u03af\u03bd\u03bf\u03c2."
    )
    ln()
    ln(
        "*\u0420\u043e\u043b\u044c \u0411:* \u041f\u043e\u043f\u0440\u0430\u0432\u044c\u0442\u0435 \u0440\u043e\u0434/\u0447\u0438\u0441\u043b\u043e "
        "\u0432 \u043a\u043e\u0440\u043e\u0442\u043a\u0438\u0445 \u0444\u0440\u0430\u0437\u0430\u0445 \u043f\u043e \u043e\u0431\u0440\u0430\u0437\u0446\u0430\u043c "
        "\u043f\u0443\u043d\u043a\u0442\u043e\u0432 4\u20135."
    )
    ln()
    ln("*Чек-фразы:* пары антонимов и окончания -ος -α -ο в цитате.")
    ln()
    ln("---")
    ln()

    ln("#### Ситуация 4 — Магазин одежды (A55)")
    ln()
    ln("*Контекст:* диалог про джинсы и рубашку, шпаргалка продавец/клиент, верно/неверно.")
    ln()
    ln("```text")
    ln(clothes_a55)
    ln("```")
    ln()
    ln("*Роль А:* Фивос — размер, цена, примерка, цвет рубашки по репликам.")
    ln()
    ln("*Роль Б:* Продавец — предлагайте модели и цвета из текста.")
    ln()
    ln("*Чек-фразы:* две колонки «\u03a0\u03ce\u03c2 \u03c4\u03bf \u03bb\u03ad\u03bd\u03b5» после диалога.")
    ln()
    ln("---")
    ln()

    ln(
        "#### \u0421\u0438\u0442\u0443\u0430\u0446\u0438\u044f 5 \u2014 \u0426\u0432\u0435\u0442\u0430 \u0438 \u0433\u043b\u0430\u0433\u043e\u043b "
        "\u03ad\u03c1\u03c7\u03bf\u03bc\u03b1\u03b9 (\u0441\u0440\u0435\u0434\u043d\u0438\u0439 \u0437\u0430\u043b\u043e\u0433)"
    )
    ln()
    ln(
        "*\u041a\u043e\u043d\u0442\u0435\u043a\u0441\u0442:* \u0442\u0430\u0431\u043b\u0438\u0446\u0430 \u0446\u0432\u0435\u0442\u043e\u0432 \u0441 "
        "\u00ab\u03b1\u03c1\u03ad\u03c3\u03b5\u03b9\u00bb, \u0441\u043f\u0440\u044f\u0436\u0435\u043d\u0438\u0435 \u03ad\u03c1\u03c7\u03bf\u03bc\u03b1\u03b9 "
        "\u0438 \u0440\u043e\u0434\u0441\u0442\u0432\u0435\u043d\u043d\u044b\u0445 \u0444\u043e\u0440\u043c, \u0443\u043f\u0440\u0430\u0436\u043d\u0435\u043d\u0438\u0435 7."
    )
    ln()
    ln("```text")
    ln(colors_erkhomai)
    ln("```")
    ln()
    ln(
        "*\u0420\u043e\u043b\u044c \u0410:* \u041d\u0430\u0437\u043e\u0432\u0438\u0442\u0435 \u043b\u044e\u0431\u0438\u043c\u044b\u0439 \u0446\u0432\u0435\u0442 "
        "\u0438 \u0432\u0435\u0449\u044c \u2014 \u043f\u043e \u043c\u043e\u0434\u0435\u043b\u0438 "
        "\u00ab\u039c\u03bf\u03c5 \u03b1\u03c1\u03ad\u03c3\u03b5\u03b9 \u03c4\u03bf \u2026\u00bb."
    )
    ln()
    ln(
        "*\u0420\u043e\u043b\u044c \u0411:* \u0421\u043f\u0440\u043e\u0441\u0438\u0442\u0435 "
        "\u00ab\u0433\u0434\u0435 \u0442\u044b / \u0433\u0434\u0435 \u0432\u0440\u0430\u0447 / \u043d\u0443\u0436\u043d\u043e \u043b\u0438 \u0447\u0442\u043e-\u0442\u043e\u00bb "
        "\u2014 \u0444\u043e\u0440\u043c\u044b \u03b2\u03c1\u03af\u03c3\u03ba\u03bf\u03bc\u03b1\u03b9, "
        "\u03c7\u03c1\u03b5\u03b9\u03ac\u03b6\u03bf\u03bc\u03b1\u03b9, \u03ad\u03c1\u03c7\u03bf\u03bc\u03b1\u03b9."
    )
    ln()
    ln("*Чек-фразы:* таблица лиц и примеры предложений в цитате.")
    ln()
    ln("---")
    ln()

    ln("#### Ситуация 6 — Платье и комплименты (A56)")
    ln()
    ln(
        "*\u041a\u043e\u043d\u0442\u0435\u043a\u0441\u0442:* \u0434\u0438\u0430\u043b\u043e\u0433 \u0443 \u0432\u0438\u0442\u0440\u0438\u043d\u044b "
        "\u0438 \u0432 \u043f\u0440\u0438\u043c\u0435\u0440\u043e\u0447\u043d\u043e\u0439, "
        "\u0444\u0440\u0430\u0437\u044b \u00ab\u03c3\u03bf\u03c5 \u03c0\u03ac\u03b5\u03b9\u00bb, "
        "\u00ab\u03b7 \u03c3\u03b5\u03b9\u03c1\u03ac \u03c3\u03bf\u03c5 \u03c4\u03ce\u03c1\u03b1\u00bb."
    )
    ln()
    ln("```text")
    ln(dresses_a56)
    ln("```")
    ln()
    ln("*Роль А:* Мелек или Марина — выбираете платье, обмениваетесь мнениями.")
    ln()
    ln("*Роль Б:* Продавщица — номер, примерочная, комплименты по тексту.")
    ln()
    ln("*Чек-фразы:* блок «\u03a0\u03ce\u03c2 \u03c4\u03bf \u03bb\u03ad\u03bd\u03b5» в той же цитате.")
    ln()
    ln("---")
    ln()

    ln(
        "#### \u0421\u0438\u0442\u0443\u0430\u0446\u0438\u044f 7 \u2014 \u041b\u0435\u043a\u0441\u0438\u043a\u0430 \u043e\u0434\u0435\u0436\u0434\u044b "
        "\u0438 \u0441\u043e\u0433\u043b\u0430\u0441\u043e\u0432\u0430\u043d\u0438\u0435 \u0446\u0432\u0435\u0442\u0430 \u0441 \u0440\u043e\u0434\u043e\u043c"
    )
    ln()
    ln(
        "*\u041a\u043e\u043d\u0442\u0435\u043a\u0441\u0442:* \u0441\u0435\u0442\u043a\u0430 \u0441\u043b\u043e\u0432 \u043f\u043e \u0440\u044f\u0434\u0430\u043c, "
        "\u0442\u0440\u0438 \u0441\u0442\u0440\u043e\u043a\u0438 \u0446\u0432\u0435\u0442\u0430 \u0434\u043b\u044f \u043c\u0443\u0436./\u0436\u0435\u043d./\u0441\u0440\u0435\u0434. \u0440\u043e\u0434\u0430."
    )
    ln()
    ln("```text")
    ln(clothes_colors_grid)
    ln("```")
    ln()
    ln(
        "*\u0420\u043e\u043b\u044c \u0410:* \u041f\u043e\u043a\u0443\u043f\u0430\u0442\u0435\u043b\u044c "
        "\u2014 \u043d\u0430\u0437\u043e\u0432\u0438\u0442\u0435 \u0432\u0435\u0449\u044c \u0438 \u0446\u0432\u0435\u0442 "
        "(\u03c0.\u03c7. \u03bc\u03b1\u03cd\u03c1\u03bf \u03c6\u03cc\u03c1\u03b5\u03bc\u03b1, \u03ac\u03c3\u03c0\u03c1\u03b7 \u03bc\u03c0\u03bb\u03bf\u03cd\u03b6\u03b1)."
    )
    ln()
    ln(
        "*\u0420\u043e\u043b\u044c \u0411:* \u041f\u0440\u043e\u0434\u0430\u0432\u0435\u0446 "
        "\u2014 \u043f\u0435\u0440\u0435\u0441\u043f\u0440\u043e\u0441\u0438\u0442\u0435 \u0446\u0432\u0435\u0442 \u0438 \u0440\u0430\u0437\u043c\u0435\u0440, "
        "\u0438\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u044f \u043b\u0435\u043a\u0441\u0438\u043a\u0443 \u0441\u0435\u0442\u043a\u0438."
    )
    ln()
    ln(
        "*\u0427\u0435\u043a-\u0444\u0440\u0430\u0437\u044b:* \u0441\u043f\u0438\u0441\u043a\u0438 "
        "\u00ab\u03a3\u03b5\u03b9\u03c1\u03ac 1\u20134\u00bb \u0438 \u0431\u043b\u043e\u043a "
        "\u00ab\u03a7\u03c1\u03ce\u03bc\u03b1\u03c4\u03b1 \u03ba\u03b1\u03b9 \u03b3\u03ad\u03bd\u03b7\u00bb."
    )
    ln()
    ln("---")
    ln()

    ln(
        "#### \u0421\u0438\u0442\u0443\u0430\u0446\u0438\u044f 8 \u2014 "
        "\u03a5\u03c0\u03ac\u03c1\u03c7\u03b5\u03b9, \u03b1\u03c1\u03ad\u03c3\u03b5\u03b9, \u0440\u043e\u043b\u0438, "
        "\u0442\u0435\u043a\u0441\u0442\u044b \u043e \u043b\u044e\u0434\u044f\u0445 \u0438 \u043f\u0440\u043e\u0441\u043b\u0443\u0448\u0438\u0432\u0430\u043d\u0438\u0435 (A57, A58)"
    )
    ln()
    ln(
        "*\u041a\u043e\u043d\u0442\u0435\u043a\u0441\u0442:* \u0443\u043f\u0440\u0430\u0436\u043d\u0435\u043d\u0438\u044f 1.0\u20131.8, "
        "\u00ab\u03a0\u03b1\u03af\u03b6\u03c9 \u03ad\u03bd\u03b1\u03bd \u03c1\u03cc\u03bb\u03bf\u00bb, "
        "\u0442\u0435\u043a\u0441\u0442\u044b \u03a3\u03c4\u03ad\u03bb\u03b9\u03bf\u03c2 / \u039b\u03af\u03bb\u03b9\u03b1\u03bd "
        "\u0438 \u043a\u043e\u0440\u043e\u0442\u043a\u0438\u0435 \u043f\u043e\u0440\u0442\u0440\u0435\u0442\u044b, "
        "\u0437\u0430\u0434\u0430\u043d\u0438\u0435 \u043a \u0430\u0443\u0434\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044e, "
        "\u043e\u0440\u0444\u043e\u0433\u0440\u0430\u0444\u0438\u044f \u03c4\u03c3/\u03c4\u03b6, "
        "\u0437\u0430\u0434\u0430\u043d\u0438\u044f 2.3\u20132.4."
    )
    ln()
    ln("```text")
    ln(yparxei_aresei_roles)
    ln(listening_write_erase)
    ln("```")
    ln()
    ln(
        "*\u0420\u043e\u043b\u044c \u0410 / \u0411:* \u0421\u0446\u0435\u043d\u0430\u0440\u0438\u0438 "
        "\u00ab\u03a9\u03c1\u03b1\u03af\u03b1 \u03bc\u03c0\u03bb\u03bf\u03cd\u03b6\u03b1!\u00bb "
        "\u0438 \u043e\u0431\u043c\u0435\u043d \u043f\u043e \u0441\u043f\u0438\u0441\u043a\u0430\u043c \u043f\u043e\u0434\u0430\u0440\u043a\u043e\u0432; "
        "\u0437\u0430\u0442\u0435\u043c \u0443\u0441\u0442\u043d\u043e \u043e\u043f\u0438\u0448\u0438\u0442\u0435, "
        "\u0447\u0442\u043e \u0441\u043b\u044b\u0448\u0438\u0442\u0435 \u0432 A57\u2013A58 \u043f\u043e \u0442\u0430\u0431\u043b\u0438\u0446\u0435 2.1."
    )
    ln()
    ln(
        "*\u0427\u0435\u043a-\u0444\u0440\u0430\u0437\u044b:* \u0431\u043b\u043e\u043a "
        "\u00ab\u03a5\u03c0\u03ac\u03c1\u03c7\u03b5\u03b9\u00bb \u0438 "
        "\u00ab\u03b1\u03c1\u03ad\u03c3\u03b5\u03b9 / \u03b1\u03c1\u03ad\u03c3\u03bf\u03c5\u03bd\u00bb "
        "\u0432 \u043d\u0430\u0447\u0430\u043b\u0435 \u0434\u043b\u0438\u043d\u043d\u043e\u0439 \u0446\u0438\u0442\u0430\u0442\u044b."
    )

    ln()
    ln("### Блок 2: Шпаргалка для диалогов (фразы-клише)")
    ln()
    ln("*Срезы: три цветные шпаргалки «\u03a0\u03ce\u03c2 \u03c4\u03bf \u03bb\u03ad\u03bd\u03b5» после A54, A55, A56.*")
    ln()
    ln("```text")
    ln(pos_lene_a54)
    ln()
    ln(pos_lene_a55)
    ln()
    ln(pos_lene_a56)
    ln("```")
    ln()

    ln("### Блок 3: Тематический словарь и образцы")
    ln()
    ln(
        "*\u0424\u0440\u0430\u0433\u043c\u0435\u043d\u0442\u044b \u043e\u0446\u0438\u0444\u0440\u043e\u0432\u043a\u0438: "
        "\u043c\u0435\u0441\u0442\u043e\u0438\u043c\u0435\u043d\u0438\u044f \u0441 \u0434\u0430\u0442\u0435\u043b\u0435\u043c, "
        "\u043e\u043a\u043e\u043d\u0447\u0430\u043d\u0438\u044f \u043f\u0440\u0438\u043b\u0430\u0433\u0430\u0442\u0435\u043b\u044c\u043d\u044b\u0445, "
        "\u0446\u0432\u0435\u0442\u0430, \u043e\u0434\u0435\u0436\u0434\u0430, "
        "\u03a5\u03c0\u03ac\u03c1\u03c7\u03b5\u03b9, \u03b1\u03c1\u03ad\u03c3\u03b5\u03b9."
    )
    ln()
    ln("#### Дательные формы (\u03bc\u03bf\u03c5, \u03c3\u03bf\u03c5, \u2026)")
    ln()
    ln("```text")
    ln(gia_pronouns)
    ln("```")
    ln()
    ln("#### -ος, -η, -ο на примере \u03b1\u03ba\u03c1\u03b9\u03b2\u03cc\u03c2")
    ln()
    ln("```text")
    ln(gia_adj_osi_o)
    ln("```")
    ln()
    ln("#### -ος, -α, -ο на примере \u03ba\u03b1\u03b9\u03bd\u03bf\u03cd\u03c1\u03b9\u03bf\u03c2")
    ln()
    ln("```text")
    ln(gia_adj_osa_o)
    ln("```")
    ln()
    ln("#### \u03b1\u03c5\u03c4\u03cc\u03c2 \u00b7 \u03b5\u03ba\u03b5\u03af\u03bd\u03bf\u03c2")
    ln()
    ln("```text")
    ln(gia_autos_ekeinos)
    ln("```")
    ln()
    ln("#### Цвета (базовая сетка)")
    ln()
    ln("```text")
    ln(gia_colors_basic)
    ln("```")
    ln()
    ln("#### Одежда по рядам")
    ln()
    ln("```text")
    ln(gia_clothes_list)
    ln("```")
    ln()
    ln(
        "#### \u0426\u0432\u0435\u0442 \u0438 \u0440\u043e\u0434 "
        "(\u03c3\u03ba\u03bf\u03cd\u03c6\u03bf\u03c2 / \u03bc\u03c0\u03bb\u03bf\u03cd\u03b6\u03b1 / \u03c0\u03bf\u03c5\u03ba\u03ac\u03bc\u03b9\u03c3\u03bf)"
    )
    ln()
    ln("```text")
    ln(gia_colors_gender)
    ln("```")
    ln()
    ln(
        "#### \u03a5\u03c0\u03ac\u03c1\u03c7\u03b5\u03b9 \u03ba\u03b1\u03bd\u03ad\u03bd\u03b1\u03c2 / "
        "\u03ba\u03b1\u03bc\u03af\u03b1 / \u03ba\u03b1\u03bd\u03ad\u03bd\u03b1"
    )
    ln()
    ln("```text")
    ln(gia_yparxei)
    ln("```")
    ln()
    ln(
        "#### \u03b1\u03c1\u03ad\u03c3\u03b5\u03b9 / \u03b1\u03c1\u03ad\u03c3\u03bf\u03c5\u03bd "
        "\u00b7 \u03c3\u03bf\u03c5 \u03c0\u03ac\u03b5\u03b9 \u00b7 \u03bc\u03bf\u03c5 \u03ba\u03ac\u03bd\u03b5\u03b9"
    )
    ln()
    ln("```text")
    ln(gia_aresei)
    ln("```")

    out_path.write_text("\n".join(out) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
