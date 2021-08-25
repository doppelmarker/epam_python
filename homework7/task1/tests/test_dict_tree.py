from homework7.task1.dict_tree.dict_tree import find_occurrences

data = {
    "first": ["RED", "BLUE"],
    "RED": {
        None: ["simple", "list", "of", "RED", "valued"],
    },
    "third": {
        "abc": {1, 4, 3},
        "RED": "RED",
        "complex_key": {
            "key1": True,
            "key2": "RED",
            "key3": ["a", (123,), "of", "values", {"nested_key": "RED"}],
        },
    },
    "fourth": "RED",
}


def test_count_red_8_times_positive():
    searching = "RED"

    expected = 8

    actual = find_occurrences(data, searching)

    assert actual == expected


def test_count_none_1_times_positive():
    searching = None

    expected = 1

    actual = find_occurrences(data, searching)

    assert actual == expected


def test_count_tuple123_2_times_negative():
    searching = (123,)

    expected = 2

    actual = find_occurrences(data, searching)

    assert not actual == expected
