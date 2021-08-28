from homework7.task3.backspace_compare.backspace_compare import backspace_compare


def test_backspace_normal_strings_positive():
    first = "abe###DSA"
    second = "ab##DS#SA"

    assert backspace_compare(first, second)


def test_backspace_normal_strings_negative():
    first = "aaae###DSA"
    second = "ab##DS#SA"

    assert not backspace_compare(first, second)


def test_backspace_empty_string():
    first = "###DSA"
    second = "a#b##DS#SA"

    assert backspace_compare(first, second)
