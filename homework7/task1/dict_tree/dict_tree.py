"""
Given a dictionary (tree), that can contains multiple nested structures.
Write a function, that takes element and finds the number of occurrences
of this element in the tree.
Tree can only contains basic structures like:
    str, list, tuple, dict, set, int, bool
"""
from collections import Counter
from collections.abc import Iterable

# Example tree:
example_tree = {
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


def is_iterable(arg):
    return isinstance(arg, Iterable) and not isinstance(arg, str)


def get_all_items(d):
    if isinstance(d, dict):
        for k, v in d.items():
            yield from get_all_items(k)
            yield from get_all_items(v)
    elif is_iterable(d):
        for v in d:
            yield from get_all_items(v)
    else:
        yield d


def find_occurrences(d, element):
    return Counter(get_all_items(d))[element]


if __name__ == "__main__":
    print(find_occurrences(example_tree, "RED"))
