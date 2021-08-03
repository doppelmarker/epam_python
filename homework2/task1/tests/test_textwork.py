import os

from homework2.task1.textwork.textwork import get_longest_diverse_words, get_rarest_char


def test_get_longest_diverse_words():
    cur_path = os.path.dirname(__file__)
    assert get_longest_diverse_words(os.path.join(cur_path, "../textwork/data.txt")) == [
        "Entscheidungsschlacht",
        "Werkstättenlandschaft",
        "résistance-Bewegungen",
        "Wiederbelebungsübungen",
        "Mehrheitsvorstellungen",
        "zoologisch-politischen",
        "symbolischsakramentale",
        "Souveränitätsansprüche",
        "Verfassungsverletzungen",
        "politisch-strategischen",
    ]


def test_get_rarest_char():
    cur_path = os.path.dirname(__file__)
    assert get_rarest_char(os.path.join(cur_path, "../textwork/data.txt")) == ")(X’îY‹›"
