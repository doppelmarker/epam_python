import os

from homework2.task1.textwork.textwork import get_longest_diverse_words


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
