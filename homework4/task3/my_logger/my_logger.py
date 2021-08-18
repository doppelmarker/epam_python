from __future__ import print_function

import sys


def my_logger(text: str):
    eprint(text) if text.startswith("error") else print(text)


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)
