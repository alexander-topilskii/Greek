#!/usr/bin/env python3
"""Split lesson_1/lexicon.md 'Итоговая лексика' into themed sub-tables (~10–12 rows)."""
from __future__ import annotations

import re
from collections import OrderedDict
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
LEX = REPO / "book/pages/lesson_1/lexicon.md"
MAXR = 12

ORDER = (
    "famous",
    "geo",
    "eimai",
    "intro",
    "school",
    "readw",
    "numday",
    "food",
    "things",
    "sport",
    "phr",
    "misc",
)
TITLES = {
    "famous": "Знаменитости, писатели, кино, спорт",
    "geo": "География: страны, регионы",
    "eimai": "«Είμαι», местоимения, отрицание",
    "intro": "Имя, происхождение, вопросы",
    "school": "Школа, урок, задания",
    "readw": "Чтение, письмо, ударение",
    "numday": "Числа, дни, время",
    "food": "Еда, напитки",
    "things": "Быт, вещи, транспорт",
    "sport": "Спорт, досуг, места",
    "phr": "Учебные фразы, вывески, реплики",
    "misc": "Прочая лексика",
}

FAMOUS_KW = (
    "τσέχ",
    "моцарт",
    "gabri",
    "νερού",
    "dostoy",
    "ντοστο",
    "φιοντ",
    "pablo n",
    "de niro",
    "jordan",
    "τζόρ",
    "γκάν",
    "mandel",
    "markes",
    "маркес",
    "μαντ",
    "мадон",
    "madon",
    "μάντ",
    "μπράν",
    "mάρλον",
    "jenn",
    "лóп",
    "лопес",
    "feder",
    "лорк",
    "ч гев",
    "τσε γ",
    "γκεβ",
    "hans",
    "андерс",
    "ίκαρ",
    "икар",
    "μάο τσε",
    "mάο τ",
    "λόρκ",
    "mάρκ",
    "ρομπ",
    "λόπε",
    "ντε νί",
    "ντε ν",
)
GEO_G = (
    "αίγυπ",
    "αιθιοπ",
    "αλβαν",
    "αρμεν",
    "αυστρ",
    "αυστραλ",
    "αφγαν",
    "αφρ",
    "βέλγ",
    "βουλγ",
    "αθήνα",
    "κίνα",
    "ελλάδ",
    "τουρκ",
    "ρωσ",
    "μεξικ",
    "ουκρα",
    "ουγγ",
    "ιταλ",
    "λίβαν",
    "λευκορ",
    "υεμέ",
    "αγγλ",
    "ισπαν",
    "γαλλ",
    "καναδ",
    "ελβετ",
    "μαυρ",
    "ολλανδ",
    "ισρ",
)
GEO_RU = (
    "егип",
    "эфиоп",
    "албан",
    "армен",
    "австр",
    "австра",
    "афган",
    "афр",
    "бельг",
    "болг",
    "афин",
    "итал",
    "укра",
    "венг",
    "белар",
    "йемен",
    "маврит",
    "англ",
    "испан",
    "фран",
    "кана",
    "литв",
)

READW = (
    "γράφ",
    "γραφ",
    "διαβά",
    "τόν",
    "τόνος",
    "φωνή",
    "φωνίεν",
    "σβή",
    "ιδιο",
    "στί",
    "πινακ",
    "ψηφ",
    "αριθμ",
    "αντιστοιχ",
    "λογότυπ",
)

SCHOOL = (
    "μάθη",
    "σχολ",
    "συμπλ",
    "διορθ",
    "διάλογ",
    "παράδειγ",
    "υποδείγ",
    "φτιαχ",
    "οικονομ",
    "βιβλ",
    "ζωγραφ",
    "βιολογ",
    "μοντέλ",
    "αναγιν",  # αναγινωρίζω, «о «… рожден»
    "άσκη",
    "ασκή",
    "λέξεων",
    "εύκολ",
    "εύκ",  # лёгкий
)

FOOD = (
    "αγγού",
    "μπανα",
    "ντομά",
    "τσάι",
    "μπίρ",
    "σπαγ",
    "κέτσ",
    "τζατ",
    "τσίγ",
    "χάμ",
    "ανάνα",
    "τσιγ",
)

THINGS = (
    "αυτοκιν",
    "ομπρέ",
    "παπού",
    "τσάν",
    "τζιν",
    "ντίβ",
    "ντίσκ",
    "τζαμ",
    "κλουβ",
    "τζάγκ",
    "σούπερ",
    "σαντ",
    "φλιτζ",
    "ράδιο",
)

SPORT = (
    "αθλη",
    "ποδό",
    "ποδόσ",
    "μπάλ",
    "μπάσ",
    "τοξ",
    "τσίρκ",
    "τραγ",
    "κινητ",
    "θεατ",
)


def parse_rows(text: str) -> list[tuple[str, str]]:
    m = re.search(
        r"### Итоговая лексика\n\n\| ελληνικά \| по-русски \|\n\|[-| ]+\|\n(.*)\Z",
        text,
        re.S,
    )
    if m:
        body = m.group(1)
    else:
        i = text.find("### Итоговая лексика\n")
        if i < 0:
            raise SystemExit("no Итоговая")
        rest = text[i + len("### Итоговая лексика\n") :]
        m2 = re.search(r"^\n?##(?!#)", rest, re.M)
        body = rest if not m2 else rest[: m2.start()]
    rows: list[tuple[str, str]] = []
    for line in body.splitlines():
        line = line.rstrip()
        if not line.startswith("|"):
            continue
        p = re.match(r"^\|\s*([^|]*?)\s*\|\s*([^|]*?)\s*\|", line)
        if not p:
            continue
        g, r = p.group(1).strip(), p.group(2).strip()
        if g == "ελληνικά" and r == "по-русски":
            continue
        if re.match(r"^[-:|\s]+$", g.replace(" ", "")):
            continue
        rows.append((g, r))
    if not rows:
        raise SystemExit("empty")
    return rows


def _maybe_name_line(gr: str, ru: str) -> bool:
    g, r = gr.strip(), ru.strip()
    if len(g) > 50 or not g or re.search(r"\d", g + r):
        return False
    if re.search(r"[,;·]", g) and "/" not in g:
        return False
    if re.search(
        r"(οικογέν|πατέρ|από|λένε|είναι|είμαι|πώς|τόν|μάθ|σχολ|άσκη|γει|καλη|πραγμ)",
        g.lower(),
    ):
        return False
    return bool(r and r[0].isupper() and " " not in r and 2 < len(r) < 24)


def theme(gr: str, ru: str) -> str:
    t = (gr + " " + ru).lower()
    g, r = gr.lower().strip(), ru.lower()
    g0 = g.lstrip("«\"”")

    if any(k in t for k in FAMOUS_KW):
        return "famous"
    if any(x in g for x in GEO_G) or any(x in r for x in GEO_RU):
        return "geo"
    if (
        g0.startswith(("έξω", "στη γραμματεία", "ααα", "εεε", "αα!"))
        or re.match(r"^χα+π", g0)
        or gr.strip().upper().startswith(("ΧΑΠ", "ΠΑΡ."))
        or (g0.startswith("έλα!") and "εδώ" in t)
        or re.search(r"αα{3,}|εε{3,}|happening", t, re.I)
    ):
        return "phr"
    if "υπόδειγμα" in g and "ταβ" in g:
        return "phr"
    if re.search(
        r"τα εφτ|7 αδε|7 брат|о «|загол",
        t,
    ):
        return "phr"
    if any(k in t for k in READW) and not re.match(
        r"^άσκη|^ασκή",
        g,
    ):
        return "readw"
    if re.match(
        r"^άσκη|^ασκή|^τί |^ασκ",
        g,
    ) or re.search(
        r"τί θα|τι θα|μάθ|άσ|ασ|σχ|συμπ|παρ|υπο|ανα|διά|επ|φτια|λέξ|οικ|βι|ζ|εύ|μον|λό",
        t,
    ):
        if re.search(
            r"μάθ|σχ|άσ|ασ|συμπ|παρ|επ|υπο|ανα|διά|οικ|βι|ζ|εύ|μον|λό|τί|τι θ",
            t,
        ) or re.match(
            r"^(ά|μά|τί|ασ|φ|υ|οικ|παρ|ανα|δ|επ)",
            g,
        ):
            return "school"
    if re.match(
        r"^ναι!?$",
        g,
    ) and "да" in r:
        return "eimai"
    if re.search(
        r"^όχι",
        g,
    ) and "δεν" in g and ("нет" in r or "я не" in r):
        return "eimai"
    if re.search(
        r"ε[ίι]σ(αι|ασ|τε|αστε)\b",
        t,
    ):
        return "eimai"
    if re.search(
        r"^αυτ(ός|ή|ό)\b",
        g,
    ) or re.search(
        r"^αυτό\b",
        g,
    ) or re.search(
        r"^εγώ\b",
        g,
    ):
        return "eimai"
    if re.search(
        r"χαίρω|ευχ|παρακ|κυρ[ίι]ε|κυρία",
        t,
    ) and re.search(
        r"^χ|ευ|παρα|κυρ",
        g,
    ):
        return "eimai"
    if re.search(
        r"^γε|^καλ",
        g,
    ) or re.search(
        r"^κά|κυρ[ίι]ε|κυρία",
        g,
    ):
        return "intro"
    if re.search(
        r"^πώς|με λ|λέ|όνο|από π|από|πατ|οικογ|γον",
        g,
    ) or (
        re.search(
            r"^πώ",
            g,
        )
        and re.search(
            r"λέ|ν",
            t,
        )
    ):
        if re.search(
            r"^πώ",
            g,
        ) and (
            "тó" in r
            or "тo" in r
            or "слов" in r
            or "удар" in t
        ):
            return "readw"
        return "intro"
    if "από" in t and re.search(
        r"από",
        g,
    ) and re.search(
        r"(из |откуд|где )",
        t,
    ):
        return "intro"
    nwords = (
        "μηδέν", "ένα", "δύο", "τρία", "τέσσ", "τέτρα", "πέντε", "έξι",
        "εφτ", "οκτ", "οχτ", "επτ", "δέκα", "δεκα",
    )
    for w in nwords:
        if re.match(
            r"^" + re.escape(w) + r"($|[\s,;/|])",
            g,
        ):
            return "numday"
    if re.search(
        r"οκτ[ώo]|οχτ[ώo]",
        t,
    ) and len(
        g,
    ) < 18:
        return "numday"
    if re.search(
        r"παρασκευ|δευτέ|τριη",
        t,
    ) and re.search(
        r"понед|ср|втор|среда|сред|четв|празд|воск|пят|суб|утр|дн[яе]|ноч|день|ден",
        r,
    ):
        return "numday"
    if re.search(
        r"εννέ|4:00|4\.|μετά τι|πρω[ίi]|αύρ|αύ|νυχ",
        t,
    ) and re.search(
        r"ноль|три|9|0|4:|посл|утр|6|1|2|3|4|5|7|8",
        r,
    ):
        return "numday"
    if any(
        k in t for k in FOOD
    ) or re.search(
        r"сэнд|wich|gамб",
        t,
    ):
        return "food" if "ταβ" not in t and "tав" not in t else "phr"
    if any(
        k in t for k in THINGS
    ) or re.search(
        r"^σούπ",
        g,
    ):
        return "things"
    if any(
        k in t for k in SPORT
    ):
        return "sport"
    if re.search(
        r"^έλ|^έξ|ταβ|συγ|για|εντά|καλή|γραμ|σειρά|μετά|ποτ(έ|ε)?|αναί|σέρ|ωρ[αά]|ώρ|εδώ|είμα|πάρ",
        t,
    ):
        return "phr"
    if _maybe_name_line(
        gr, ru
    ):
        return "intro"
    return "misc"

def chunk(
    rows: list[tuple[str, str]], mx: int
) -> list[list[tuple[str, str]]]:
    return [rows[i : i + mx] for i in range(0, len(rows), mx)]


def run() -> str:
    text = LEX.read_text(encoding="utf-8")
    rows = parse_rows(text)
    buckets: OrderedDict[str, list[tuple[str, str]]] = OrderedDict()
    for k in ORDER:
        buckets[k] = []
    for g, r in rows:
        b = theme(g, r)
        buckets[b if b in buckets else "misc"].append(
            (g, r)
        )
    parts: list[tuple[str, list[tuple[str, str]]]] = []
    for k in ORDER:
        lst = buckets.get(k) or []
        if not lst:
            continue
        chs = chunk(lst, MAXR)
        for n, ch in enumerate(
            chs, 1
        ):
            tname = TITLES[k] if len(chs) == 1 else f"{TITLES[k]} (часть {n})"
            parts.append((tname, ch))
    head = text.partition("### Итоговая лексика")[
        0
    ].rstrip()
    out = [head + "\n", "### Итоговая лексика", ""]
    for tname, rws in parts:
        out.append("#### " + tname)
        out.append("")
        out.append(
            "| ελληνικά | по-русски |"
        )
        out.append(
            "|----------|----------|"
        )
        for g, r in rws:
            out.append(f"| {g} | {r} |")
        out.append("")
    return "\n".join(
        out
    ).rstrip() + "\n"


if __name__ == "__main__":
    s = run()
    LEX.write_text(
        s, encoding="utf-8"
    )
    print(
        "ok", len(
            s
        )
    )
