import string
from typing import Any, List, Sequence


def custom_range(sequence: Sequence, *args) -> List[Any]:
    if len(args) == 1:
        idx = sequence.index(*args)
        return [element for element in sequence[:idx]]
    elif len(args) == 2:
        start, end = args[0], args[1]
        idx1 = sequence.index(start)
        idx2 = sequence.index(end)
        return [element for element in sequence[idx1:idx2]]
    elif len(args) == 3:
        start, end, step = args[0], args[1], args[2]
        idx1 = sequence.index(start)
        idx2 = sequence.index(end)
        return [element for element in sequence[idx1:idx2:step]]
    else:
        args_amount = 1 + len(args)
        raise TypeError(f"custom_range expected at most 4 arguments, got {args_amount}")


string = string.ascii_lowercase
print(string)
print(custom_range(string, "g"))
print(custom_range(string, "g", "p"))
print(custom_range(string, "p", "g", -2))

items = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(custom_range(items, 2, 9))
# print(custom_range(string, 'p', 'g', -2, '2'))
