"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""
from typing import List

import nltk


# Returns a dictionary of text elements:
# 'E': [3, 1, 1]
# ===============
# amount  | length | amount of
# in text |        | unique elements
def parse(file_path: str):
    parsed_parts = {}
    buf = ""

    with open(file_path) as file:
        for line in file:
            if not line.isspace():
                line_parts = nltk.tokenize.word_tokenize(line.encode("utf-8").decode("unicode-escape"))
                i = 0
                parts_amount = len(line_parts)
                while i < parts_amount:
                    current_part = line_parts[i]
                    if i == 0 and buf:
                        current_part = buf + current_part
                        buf = ""
                    if i == parts_amount - 1 and current_part[-1] == "-":
                        buf = current_part[:-1]
                        break
                    if current_part not in parsed_parts:
                        parsed_parts[current_part] = [1, len(current_part), len(set(current_part))]
                    else:
                        parsed_parts[current_part][0] += 1
                    i += 1
    return parsed_parts


def get_longest_diverse_words(file_path: str) -> List[str]:
    parsed_parts = parse(file_path)
    parsed_parts = {k: v for k, v in sorted(parsed_parts.items(), key=lambda item: (item[1][1], item[1][2]))}
    return list(parsed_parts)[-10:]


def get_rarest_char(file_path: str) -> str:
    ...


def count_punctuation_chars(file_path: str) -> int:
    ...


def count_non_ascii_chars(file_path: str) -> int:
    ...


def get_most_common_non_ascii_char(file_path: str) -> str:
    ...
