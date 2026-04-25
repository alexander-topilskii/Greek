#!/usr/bin/env python3
"""Remove editor/meta parentheticals from lexicon table cells (one-off or batch)."""
from __future__ import annotations

import re
import sys
from pathlib import Path

# Ordered: longer/more specific first
META_PATTERNS: tuple[re.Pattern[str], ...] = (
    re.compile(
        r"\s*\(стр\.\s*[0-9–—]+[^)]*(?:\)|$)",
        re.IGNORECASE,
    ),
    re.compile(
        r"\s*\(в упр\.\s*[^)]+\)",
        re.IGNORECASE,
    ),
    re.compile(
        r"\s*\(заголовок[^)]*\)",
        re.IGNORECASE,
    ),
    re.compile(
        r"\s*\(фрагмент[^)]*\)",
        re.IGNORECASE,
    ),
    re.compile(
        r"\s*\(омограф[^)]*\)",
        re.IGNORECASE,
    ),
    re.compile(
        r"\s*\(иллюстр\.\s*[^)]+\)",
        re.IGNORECASE,
    ),
    re.compile(
        r"\s*\(пример[^)]*\)",
        re.IGNORECASE,
    ),
    re.compile(
        r"\s*\(имя[^)]*\)",
        re.IGNORECASE,
    ),
    re.compile(
        r"\s*\(фамилия\)",
    ),
    re.compile(
        r"\s*\(рубрика\)",
    ),
    re.compile(
        r"\s*\(вывеска\)",
    ),
    re.compile(
        r"\s*\(название[^)]*\)",
    ),
    re.compile(
        r"\s*\(марка\)",
    ),
    re.compile(
        r"\s*\(метафора[^)]*\)",
    ),
    re.compile(
        r"\s*\(игра[^)]*\)",
    ),
    re.compile(
        r"\s*\(ном\.\)",
    ),
    re.compile(
        r"\s*\(3 л\.\)",
    ),
    re.compile(
        r"\s*\(варианты\)",
    ),
    re.compile(
        r"\s*\(контекст\)",
    ),
    re.compile(
        r"\s*\(о\)\s*",
    ),
    re.compile(
        r"\s*\(т\)\s*",
    ),
    re.compile(
        r"\s*\(в задании\)",
    ),
    re.compile(
        r"\s*\(в блоке[^)]*\)",
    ),
    re.compile(
        r"\s*\(к упр\.\s*[^)]+\)",
    ),
    re.compile(r"\s*\(стиль\)"),
    re.compile(
        r"\s*\(заголовки[^)]*\)",
        re.IGNORECASE,
    ),
    re.compile(r"\s*\(к вам\)"),
    re.compile(r"\s*\(вариант\)", re.IGNORECASE),
    re.compile(
        r"\s*\(предлог[^)]*\)",
    ),
    re.compile(r"\s*\(аудио\)", re.IGNORECASE),
    re.compile(r"\s*\(мнемоника[^)]*\)"),
    re.compile(r"\s*\(облачка[^)]*\)"),
    re.compile(r"\s*\(блок[^)]*\)"),
    re.compile(r"\s*\(вы\)", re.IGNORECASE),
    re.compile(
        r"\s*\(после [^)]+\)",
    ),
    re.compile(r"\s*\(район\)", re.IGNORECASE),
    re.compile(r"\s*\(разг\.\)"),
    re.compile(r"\s*\(предмет\)", re.IGNORECASE),
    re.compile(r"\s*\(на коллаже\)", re.IGNORECASE),
    re.compile(
        r"\s*\(кит\.\s*[^)]+\)",
    ),
    re.compile(
        r"\s*\(в вузе\)",
    ),
    re.compile(
        r"\s*\(в диалоге\)",
    ),
    re.compile(
        r"\s*\(представление\)",
    ),
    re.compile(
        r"\s*\(улица\)",
    ),
    re.compile(
        r"\s*\(частица\)",
    ),
    re.compile(
        r"\s*\(форма\)",
    ),
    re.compile(
        r"\s*\(ж\.\s*в\s*греч\.\)",
    ),
    re.compile(
        r"\s*\(ты/вы\)",
    ),
    re.compile(
        r"\s*\(вин\.\s*п\.\)",
    ),
    re.compile(
        r"\s*\(вежл\.\)",
    ),
    re.compile(
        r"\s*\(притяж\.\)",
    ),
    re.compile(
        r"\s*\(тел\.\)",
    ),
    re.compile(
        r"\s*\(арт\.\)",
    ),
    re.compile(
        r"\s*\(сын\)",
    ),
    re.compile(
        r"\s*\(специальность\)",
    ),
    re.compile(
        r"\s*\(акростих\)",
    ),
    re.compile(
        r"\s*\(звательный\)",
    ),
    re.compile(
        r"\s*\(в\s*знач\.\s*«[^»]+»\)",
    ),
    re.compile(
        r"\s*—\s*упр\.\s*[0-9]+",
    ),
    re.compile(
        r"\s*—\s*άσκηση\s*[0-9]+",
        re.IGNORECASE,
    ),
    re.compile(
        r"\s*\(профессия,\s*ном\.\)",
    ),
    re.compile(
        r"\s*\(гражданство\)",
    ),
    re.compile(
        r"\s*\(вопросы\)",
    ),
    re.compile(
        r"\s*\(A[0-9][0-9]*\)",
    ),
    re.compile(
        r"\s*\(ж\.\)",
    ),
    re.compile(
        r"\s*\(ср\.\)",
    ),
    re.compile(
        r"\s*\(м\s*/\s*ж\s*/\s*ср\.\)",
    ),
    re.compile(r"\s*\(остановка\)", re.IGNORECASE),
    re.compile(r"\s*\(марина\)", re.IGNORECASE),
    re.compile(r"\s*\(станция\)", re.IGNORECASE),
    re.compile(r"\s*\(площадь\)", re.IGNORECASE),
    re.compile(r"\s*\(на карте\)", re.IGNORECASE),
    re.compile(r"\s*\(адрес\)", re.IGNORECASE),
    re.compile(r"\s*\(м\s*/\s*ж\)", re.IGNORECASE),
    re.compile(r"\s*\(они\)", re.IGNORECASE),
    re.compile(r"\s*\(из транспорта\)", re.IGNORECASE),
    re.compile(r"\s*\(города\)", re.IGNORECASE),
    re.compile(r"\s*\(о часах\)", re.IGNORECASE),
    re.compile(r"\s*\(часа\)", re.IGNORECASE),
    re.compile(r"\s*\(илл\.\)"),
    re.compile(r"\s*\(отрицания\)", re.IGNORECASE),
    re.compile(r"\s*\(e-mail\)", re.IGNORECASE),
    re.compile(r"\s*\(город\)", re.IGNORECASE),
    re.compile(r"\s*\(длится\)", re.IGNORECASE),
    re.compile(r"\s*\(Александрос\)", re.IGNORECASE),
    re.compile(r"\s*\(файлов\)", re.IGNORECASE),
    re.compile(r"\s*\(обратный билет\)", re.IGNORECASE),
    re.compile(r"\s*\(работает\)", re.IGNORECASE),
    re.compile(r"\s*\(проезжает мимо\)", re.IGNORECASE),
    re.compile(r"\s*\(времени\)", re.IGNORECASE),
    re.compile(r"\(метро\)", re.IGNORECASE),
    re.compile(r"\s*\(машину\)", re.IGNORECASE),
    re.compile(
        r"\(в «без четверти»\)",
    ),
    re.compile(
        r"\(в «ηλεκτρικά»\)",
    ),
    re.compile(r"\(Стамбул\)", re.IGNORECASE),
    re.compile(
        r"\s*\(обращение\)",
    ),
    re.compile(
        r"\s*\(смысл\)",
    ),
    re.compile(
        r"\s*\(выражение\)",
    ),
    re.compile(
        r"\s*\(междом\.\)",
    ),
    re.compile(
        r"\s*\(сейчас\)",
    ),
    re.compile(
        r"\s*\(вин\.\)",
    ),
    re.compile(
        r"\s*\(о животном\)",
    ),
    re.compile(
        r"\s*\(порядк\.\)",
    ),
    re.compile(
        r"\s*\(кроссворд\)",
    ),
    re.compile(
        r"\s*\(день недели\)",
    ),
    re.compile(
        r"\s*\(вы\)",
    ),
    re.compile(
        r"\s*\(роли\)",
    ),
    re.compile(
        r"\s*\(артикль\)",
    ),
    re.compile(
        r"\s*\(варианты написания\)",
    ),
    re.compile(
        r"\s*\(διάδρομος\)",
    ),
    re.compile(
        r"\s*\(плиф\.\)",
    ),
    re.compile(
        r"\s*\(τίτλος\)",
    ),
    re.compile(
        r"\s*\(τίτλος ενότητας\)",
    ),
    re.compile(
        r"\s*\(начало записки\)",
    ),
    re.compile(
        r"\s*\(на чеке\)",
    ),
    re.compile(
        r"\s*\(род\)",
    ),
    re.compile(
        r"\s*\(мн\.\)",
    ),
    re.compile(
        r"\s*\(овощ\)",
    ),
    re.compile(
        r"\s*\(ж\.р\.\)",
    ),
    re.compile(
        r"\s*\(м\.р\.\s*вин\.\)",
    ),
    re.compile(
        r"\s*\(письменно\)",
    ),
    re.compile(
        r"\s*\(заголовок\)",
    ),
    re.compile(
        r"\s*\(коробок\)",
    ),
    re.compile(
        r"\s*\(пива\)",
    ),
    re.compile(
        r"\s*\(250 г\)",
    ),
    re.compile(
        r"\s*\(750 г\)",
    ),
    re.compile(
        r"\s*\(бумага\)",
    ),
    re.compile(
        r"\s*\(журнал\)",
    ),
    re.compile(
        r"\s*\(кинотеатр\)",
    ),
    re.compile(
        r"\s*\(газета\)",
    ),
    re.compile(
        r"\s*\(фильм\)",
    ),
)


NUM_EXERCISE = re.compile(r"\s*\([0-9]+[.][0-9][^)]*\)")


def clean_table_row(line: str) -> str:
    s = line
    for p in META_PATTERNS:
        s = p.sub("", s)
    s = NUM_EXERCISE.sub("", s)
    s = re.sub(r"\*\(A([0-9]+)\)\*", r" — A\1", s)
    s = re.sub(r"\s*\*\([^)]*\)\*", "", s)
    s = re.sub(r"  +", " ", s)
    s = re.sub(r"\s+\|", " |", s)
    return s


def main() -> None:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else None
    if not path or not path.is_file():
        print("Usage: clean_lexicon_meta.py <path/to/lexicon.md>", file=sys.stderr)
        sys.exit(1)
    text = path.read_text(encoding="utf-8")
    out: list[str] = []
    for line in text.splitlines(keepends=True):
        raw = line.rstrip("\n\r")
        if raw.lstrip().startswith("|") and raw.count("|") >= 2:
            raw = clean_table_row(raw)
            out.append(raw + "\n")
        else:
            out.append(line)
    path.write_text("".join(out), encoding="utf-8")


if __name__ == "__main__":
    main()
