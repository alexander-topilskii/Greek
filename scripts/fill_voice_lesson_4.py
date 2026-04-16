# -*- coding: utf-8 -*-
"""Append blocks 1 (sit.3-5), 2, 3 to voice_lesson_4.md from lesson_4_digitized.md."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DIG = ROOT / "book/pages/lesson_4/lesson_digitized/lesson_4_digitized.md"
VOICE = ROOT / "book/pages/lesson_4/lesson_voice_4/voice_lesson_4.md"
CIT = ROOT / "book/pages/lesson_4/lesson_voice_4/_cit_map.json"
RU2 = ROOT / "book/pages/lesson_4/lesson_voice_4/_block2_ru.json"


def dl(line: str) -> str:
    s = line.strip()
    if s.startswith("- "):
        return s[2:].strip()
    if s.startswith("– "):
        return s[2:].strip()
    return s


def strip_md(s: str) -> str:
    return s.replace("**", "").strip()


def dialog_body(line: str) -> str:
    line = line.strip()
    if line.startswith("**") and ":**" in line:
        return line.split(":**", 1)[1].strip()
    return line


def vera_name(L: list[str]) -> str:
    parts = dl(L[307]).split()
    return parts[2].rstrip(".")


def join_milao(L: list[str]) -> str:
    return (L[230].strip() + " " + L[231].strip()).replace("**", "")


def sveta(L: list[str]) -> str:
    s = L[260]
    if s.startswith("**Παράδειγμα:**"):
        s = s.split("**Παράδειγμα:**", 1)[1].strip()
    return s


def parse_nikos_foivos(L: list[str]) -> tuple[str, str]:
    raw = L[294]
    parts = re.split(r"\s*[–-]\s*", raw)
    q = strip_md(parts[1].strip())
    tail = parts[2].split("(*")[0].strip()
    ans = re.sub(r"\*+", "", tail).strip()
    ans = ans.split("(")[0].strip()
    return q, ans


def tcell(L: list[str], lineno: int, col: int) -> str:
    cells = [c.strip() for c in L[lineno].split("|")]
    return strip_md(cells[col]).replace("  ", " ")


def extract_scale(L: list[str], i: int) -> str:
    return L[237 + i].split("**")[1]


def me_len_marq(L: list[str]) -> str:
    mark = chr(0x039C) + chr(0x03B5) + " "
    for chunk in dialog_body(L[153]).split("."):
        chunk = chunk.strip()
        if chunk.startswith(mark) and "λένε" in chunk:
            return chunk + "."
    raise RuntimeError("me_len_marq: not found")


def apo_dho_marq(L: list[str]) -> str:
    for chunk in dialog_body(L[153]).split("."):
        chunk = chunk.strip()
        if chunk.startswith("Από "):
            return chunk + "."
    raise RuntimeError("Από not found")


def milate_milas(L: list[str]) -> str:
    q_pl = dialog_body(L[78])
    inner = q_pl.split("δε ", 1)[1] if "δε " in q_pl else q_pl
    if not inner.endswith(";"):
        inner = inner.rstrip("?") + ";"
    first = inner[0].upper() + inner[1:]
    return first + " / Μιλάς …;"


def de_milao_ellipsis(L: list[str]) -> str:
    frag = L[224].lstrip("– ").strip().split(",")[1].strip()
    base = frag.split()[0] + " " + frag.split()[1]
    if base[0] == "δ":
        base = "Δ" + base[1:]
    return base + " …"


def deny_pattern(L: list[str]) -> str:
    return strip_md(L[449].split("|")[3])


def build_block2(L: list[str], ru: list[str]) -> str:
    g: list[str] = []
    ped = dialog_body(L[77])
    g.append(ped.split(",")[0].strip() + ".")
    part2 = ped.split(",")[1].strip().replace("…", ".")
    if part2.startswith("δεν"):
        part2 = "Δ" + part2[1:]
    g.append(part2)
    g.append(dialog_body(L[87]).rstrip())
    g.append(dialog_body(L[76]).split(".")[0].strip() + ".")
    g.append(dialog_body(L[154]).rstrip())
    g.append(dialog_body(L[155]).rstrip())
    g.append(me_len_marq(L))
    g.append(apo_dho_marq(L))
    g.append(milate_milas(L))
    nik = dialog_body(L[152])
    g.append(nik.split(".", 1)[1].strip())
    g.append(L[252].split(";")[0].strip() + ";")
    parts = L[184].split()
    g.append(parts[1] + " " + parts[2])
    g.append(L[310].lstrip("– ").strip())
    for i in range(6):
        g.append(extract_scale(L, i))
    g.append(L[223].lstrip("– ").strip())
    g.append(deny_pattern(L))
    g.append(de_milao_ellipsis(L))
    g.append(
        chr(0x0394)
        + chr(0x03B5)
        + chr(0x03BD)
        + " "
        + chr(0x03C4)
        + chr(0x03BF)
        + chr(0x03BD)
        + " / "
        + chr(0x03C4)
        + chr(0x03B7)
        + chr(0x03BD)
        + " / "
        + chr(0x03C4)
        + chr(0x03BF)
        + " "
        + chr(0x03BE)
        + chr(0x03AD)
        + chr(0x03C1)
        + chr(0x03C9)
        + "."
    )
    g.append(dl(L[99]))
    g.append(dialog_body(L[85]).rstrip())
    markos_ge = dialog_body(L[86])
    malista_dot = chr(0x039C) + "\u03ac\u03bb\u03b9\u03c3\u03c4\u03b1."
    tail = markos_ge.split(malista_dot, 1)[1].strip() if malista_dot in markos_ge else markos_ge
    vlep, ekei = [x.strip() for x in tail.split(";", 1)]
    g.append(vlep + ";")
    g.append(ekei.rstrip("."))
    g.append(L[312].lstrip("– ").strip())
    g.append(L[313].lstrip("– ").strip())
    ag1 = L[512]
    zitame_word = L[521].split()[0]
    zitaei_word = [w for w in ag1.split() if w.startswith("ζητά")][0]
    g.append(f"{zitame_word} / {zitaei_word} …")
    g.append(" ".join(ag1.split()[:2]))
    g.append([p.strip() for p in ag1.split(".") if "αμοιβή" in p][0])
    g.append([p.strip() for p in L[524].split(".") if "Ωράριο" in p][0])
    g.append([p.strip() for p in L[515].split(".") if "ωράριο" in p.lower()][0])
    g.append(L[518].split(".")[0].strip())
    gr_head = L[524].split("στην")[0].strip()
    g.append(gr_head + " …")

    if len(g) != len(ru):
        raise RuntimeError(f"block2 mismatch {len(g)} greek vs {len(ru)} ru")
    lines = [
        "### Блок 2: Универсальная шпаргалка (Фразы-клише)",
        "",
        "**Вежливость и понимание**",
        "",
    ]
    for i in range(3):
        lines.append(f"* **{strip_md(g[i])}** — *{ru[i]}*")
    lines.extend(["", "**Приветствие и знакомство**", ""])
    for i in range(3, 8):
        lines.append(f"* **{strip_md(g[i])}** — *{ru[i]}*")
    lines.extend(["", "**Вопросы про язык и происхождение**", ""])
    for i in range(8, 13):
        lines.append(f"* **{strip_md(g[i])}** — *{ru[i]}*")
    lines.extend(["", "**Степень владения (наречия)**", ""])
    for i in range(13, 19):
        lines.append(f"* **{strip_md(g[i])}** — *{ru[i]}*")
    lines.extend(["", "**Отрицание: όχι и δεν**", ""])
    for i in range(19, 23):
        lines.append(f"* **{strip_md(g[i])}** — *{ru[i]}*")
    lines.extend(["", "**Ориентиры и поиск пути**", ""])
    for i in range(23, 27):
        lines.append(f"* **{strip_md(g[i])}** — *{ru[i]}*")
    lines.extend(["", "**Работа (коротко)**", ""])
    for i in range(27, 29):
        lines.append(f"* **{strip_md(g[i])}** — *{ru[i]}*")
    lines.extend(["", "**Объявления о работе (ключевые слова из аγγελίες)**", ""])
    for i in range(29, 36):
        lines.append(f"* **{strip_md(g[i])}** — *{ru[i]}*")
    lines.extend(["", "---", "", "### Блок 3: Тематический словарь", ""])
    return "\n".join(lines)


TRANS_LANG = {
    "ελληνικά": "греческий язык",
    "ισπανικά": "испанский язык",
    "ρωσικά": "русский язык",
    "ρώσικα": "русский язык",
    "γερμανικά": "немецкий язык",
    "γαλλικά": "французский язык",
    "ιταλικά": "итальянский язык",
    "αγγλικά": "английский язык",
    "πολωνικά": "польский язык",
    "σουηδικά": "шведский язык",
    "κινέζικα": "китайский язык",
    "γιαπωνέζικα": "японский язык",
    "αλβανικά": "албанский язык",
    "ουκρανικά": "украинский язык",
    "αραβικά": "арабский язык",
    "βουλγαρικά": "болгарский язык",
    "βουλγάρικα": "болгарский язык",
    "τουρκικά": "турецкий язык",
}


def lang_rows(L: list[str]) -> list[tuple[str, str]]:
    seen: set[str] = set()
    out: list[tuple[str, str]] = []
    for idx in (197, 198, 199, 200):
        cell = [c.strip() for c in L[idx].split("|")][2]
        chunks = re.split(r"\s*·\s*", cell)
        for ch in chunks:
            ch = re.sub(r"\([^)]*\)", "", ch).strip()
            for part in re.split(r",\s*και\s+|,\s*", ch):
                part = part.strip().strip("και ").strip()
                if not part:
                    continue
                w = part.split()[0]
                if w in TRANS_LANG and w not in seen:
                    seen.add(w)
                    out.append((f"τα {w}", TRANS_LANG[w]))
    return out


def md_table(title: str, rows: list[tuple[str, str]]) -> str:
    lines = [
        title,
        "",
        "| Слово на греческом | Перевод на русский |",
        "|--------------------|--------------------|",
    ]
    for gk, ru in rows:
        lines.append(f"| {gk} | {ru} |")
    return "\n".join(lines)


def places_rows() -> list[tuple[str, str]]:
    return [
        ("ο κινηματογράφος", "кинотеатр"),
        ("η Εθνική Τράπεζα", "Национальный банк"),
        ("το πάρκο", "парк"),
        ("η τράπεζα", "банк"),
        ("η στάση", "остановка"),
        ("ο σταθμός", "станция"),
        ("ο καθηγητής", "учитель (старшие классы, м.)"),
        ("η καθηγήτρια", "учительница (старшие классы)"),
        ("το μετρό", "метро"),
        ("το σπίτι", "дом"),
        ("το μάθημα", "урок"),
        (
            "το "
            + chr(0x0397)
            + chr(0x03C1)
            + chr(0x03AC)
            + chr(0x03BA)
            + chr(0x03BB)
            + chr(0x03B5)
            + chr(0x03B9)
            + chr(0x03BF),
            "Ираклион",
        ),
        ("το Μοναστηράκι", "Монастираки"),
        ("το Πανόραμα", "Панорама"),
    ]


def prof_rows() -> list[tuple[str, str]]:
    return [
        ("η κομμώτρια", "парикмахер (ж.)"),
        ("ο καθηγητής", "учитель (м., старшая школа)"),
        ("η φοιτήτρια", "студентка"),
        (
            "ο "
            + chr(0x03AC)
            + chr(0x03BD)
            + chr(0x03B5)
            + chr(0x03C1)
            + chr(0x03B3)
            + chr(0x03BF)
            + chr(0x03C2),
            "безработный",
        ),
        ("ο μάγειρας", "повар"),
        ("η πωλήτρια", "продавщица"),
        ("ο κτηνίατρος", "ветеринар (форма из учебного текста)"),
        (
            "ο "
            + chr(0x03BE)
            + chr(0x03C5)
            + chr(0x03BB)
            + chr(0x03BF)
            + chr(0x03C5)
            + chr(0x03C1)
            + chr(0x03B3)
            + chr(0x03CC)
            + chr(0x03C2),
            "плотник",
        ),
        ("η γυμνάστρια", "гимнастка / тренер по гимнастике"),
        ("ο δάσκαλος", "учитель (начальная школа, м.)"),
        ("ο υπάλληλος", "служащий"),
        ("ο γραμματέας", "секретарь"),
    ]


def num_rows() -> list[tuple[str, str]]:
    return [
        ("εκατό", "сто"),
        ("εκατόν ένα", "сто один"),
        ("διακόσια", "двести"),
        ("τριακόσια", "триста"),
        ("τετρακόσια", "четыреста"),
        ("πεντακόσια", "пятьсот"),
        ("εξακόσια", "шестьсот"),
        ("επτακόσια", "семьсот"),
        ("οκτακόσια", "восемьсот"),
        ("εννιακόσια", "девятьсот"),
        ("χίλια", "тысяча"),
    ]


def verb_rows() -> list[tuple[str, str]]:
    return [
        ("μιλάω (μιλώ)", "говорю (о языке)"),
        ("καταλαβαίνω", "понимаю"),
        ("ξέρω", "знаю"),
        ("ψάχνω", "ищу"),
        ("βλέπω", "вижу"),
        ("δουλεύω", "работаю"),
    ]


def block3(L: list[str]) -> str:
    cit = json.loads(CIT.read_text(encoding="utf-8"))
    crows = [(row["el"], row["ru"]) for row in cit]
    parts = [
        md_table("**Языки (как в таблице «μιλάω …»)**", lang_rows(L)),
        md_table("**Гражданство (выборка из таблицы «Είμαι …»)**", crows),
        md_table("**Места и ориентиры (с артиклем, из раздела про винительный)**", places_rows()),
        md_table("**Профессии из таблицы профилей (раздел 8)**", prof_rows()),
        md_table("**Числа 100–1000 (ключевые формы из таблицы)**", num_rows()),
        md_table("**Глаголы и устойчивые связки**", verb_rows()),
    ]
    return "\n\n".join(parts)


def main() -> None:
    L = DIG.read_text(encoding="utf-8").splitlines()
    if len(L) < 530:
        raise SystemExit("digitized shorter than expected")

    ru2: list[str] = json.loads(RU2.read_text(encoding="utf-8"))

    name = vera_name(L)
    long_m = join_milao(L)
    sv = sveta(L)
    q_n, a_f = parse_nikos_foivos(L)
    den = (
        chr(0x0394)
        + chr(0x03B5)
        + chr(0x03BD)
        + " "
        + chr(0x03BA)
        + chr(0x03B1)
        + chr(0x03C4)
        + chr(0x03B1)
        + chr(0x03BB)
        + chr(0x03B1)
        + chr(0x03B2)
        + chr(0x03B1)
        + chr(0x03AF)
        + chr(0x03BD)
        + chr(0x03C9)
        + " "
        + chr(0x03B1)
        + chr(0x03B3)
        + chr(0x03B3)
        + chr(0x03BB)
        + chr(0x03B9)
        + chr(0x03BA)
        + chr(0x03AC)
        + "."
    )
    x_petros = tcell(L, 424, 1)
    x_bank = tcell(L, 432, 1)
    x_metro = tcell(L, 439, 1)
    x_her = tcell(L, 438, 1)
    nai_ton = strip_md(L[447].split("|")[2])
    oxi_ton = strip_md(L[447].split("|")[3])

    _eta = chr(0x0397) + " σειρά μου τώρα"
    _tgt = chr(0x1F3AF)
    _nikos = chr(0x039D) + "ίκος"

    sit3 = f"""* **Ситуация 3: Короткие диалоги — «μιλάς …;» и отрицание**
* **Контекст:** Два цветных блока с вопросами о языке, пример предложения про степень владения; образец про Σβέта из раздела «{_eta}».
* **Роль А:** Задавайте вопросы *μιλάς …;* и уточняйте национальность (*είμαι …*).
* **Роль Б:** Отвечайте *ναι* / *όχι* / *όχι, δε μιλάω …*; при необходимости расширьте ответ шкалой *πολύ καλά* … *καθόλου*.
* {_tgt} **Чек-лист для ситуации:**
  - *{dl(L[216])}* — Ты говоришь по-русски?
  - *{dl(L[217])}* — Да, я русская. А ты говоришь по-итальянски?
  - *{dl(L[218])}* — Да, я итальянец.
  - *{dl(L[222])}* — Ты говоришь по-испански?
  - *{dl(L[223])}* / *{dl(L[224])}* — Нет. / Нет, не говорю по-испански.
  - *{long_m}* — Образец степеней владения из урока.
  - *{sv}* — Свёта — украинка; говорит по-украински и по-русски очень хорошо, по-немецки достаточно хорошо и немного по-гречески.

---

"""

    sit4 = f"""* **Ситуация 4: Ποιος είναι; — профиль как у {name} (раздел 8)**
* **Контекст:** Пример диалога и таблица профилей; один собеседник расспрашивает, второй отвечает по карточке.
* **Роль А:** Спрашивайте по цепочке: кто это, гречанка ли, какие языки, работает ли и кем.
* **Роль Б:** Отвечайте по образцу про {name} или по другой строке таблицы профилей ({_nikos}, Μελέκ, Πάμπλο и др.).
* {_tgt} **Чек-лист для ситуации:**
  - *{dl(L[306])}* — Кто это (женщина)?
  - *{dl(L[307])}* — Это Вера.
  - *{dl(L[308])}* — Она гречанка?
  - *{dl(L[309])}* — Нет. Она болгарка.
  - *{dl(L[310])}* — На каком языке она говорит?
  - *{dl(L[311])}* — Говорит по-болгарски, по-английски и по-гречески.
  - *{dl(L[312])}* — Она работает?
  - *{dl(L[313])}* — Да. Она парикмахер (ж.).

---

"""

    sit5 = f"""* **Ситуация 5: όχι / δεν и винительный падеж (раздел 7, блок «Για δες»)**
* **Контекст:** Короткие ответы с *όχι* и *δεν*; вопросы *ξέρεις …;* / *βλέπεις …;* / *ψάχνεις …;* с формами **τον / την / το**.
* **Роль А:** Задавайте вопросы о знакомстве, о местах и ориентирах; чередуйте утвердительные ожидания и отрицание.
* **Роль Б:** Отвечайте *ναι* / *όχι* / *ναι, τον/την/το {chr(0x03BE)}{chr(0x03AD)}{chr(0x03C1)}{chr(0x03C9)}* / *όχι, δεν τον/την/το {chr(0x03BE)}{chr(0x03AD)}{chr(0x03C1)}{chr(0x03C9)}* по модели урока.
* {_tgt} **Чек-лист для ситуации:**
  - *{q_n}* — Ты Никос?
  - *{a_f}* — Нет. Я Фивос.
  - *{den}* — Не понимаю по-английски (модель из цепочки «όχι ή Δεν»).
  - *{x_petros}* — Ты знаешь Петроса?
  - *{nai_ton}* / *{oxi_ton}* — Да, знаю его. / Нет, не знаю его.
  - *{x_bank}* — Видишь банк?
  - *{x_metro}* — Ты ищешь метро?
  - *{x_her}* — Ты знаешь Ираклион?

---

"""

    b2 = build_block2(L, ru2)
    b3 = block3(L)
    tail = "\n" + "\n".join([sit3.strip(), sit4.strip(), sit5.strip(), b2, b3])

    body = VOICE.read_text(encoding="utf-8")
    cut = "\n\n* **Ситуация 3:"
    if cut in body:
        body = body.split(cut)[0].rstrip() + "\n"
    end_marker = "Говорит по-английски, по-итальянски и по-арабски.\n\n---\n"
    if end_marker not in body:
        raise SystemExit("end marker not found in voice_lesson_4.md")
    end_idx = body.index(end_marker) + len(end_marker)
    start_idx = body.rfind("  - *", 0, end_idx)
    key = body[start_idx:end_idx]
    VOICE.write_text(body.replace(key, key + tail), encoding="utf-8")
    print("updated", VOICE)


if __name__ == "__main__":
    main()
