"""
Given two strings. Return if they are equal when both are typed into
empty text editors. # means a backspace character.
Note that after backspacing an empty text, the text will continue empty.
Examples:
    Input: s = "ab#c", t = "ad#c"
    Output: True
    # Both s and t become "ac".
    Input: s = "a##c", t = "#a#c"
    Output: True
    Explanation: Both s and t become "c".
    Input: a = "a#c", t = "b"
    Output: False
    Explanation: s becomes "c" while t becomes "b".
"""


def get_backspaced_str(string: str):
    new_str = ""
    for char in string:
        if char != "#":
            new_str += char
        else:
            new_str = new_str[:-1]
    return new_str


def backspace_compare(first: str, second: str):
    return get_backspaced_str(first) == get_backspaced_str(second)
