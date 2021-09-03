"""
Write a function that takes directory path, a file extension and an optional tokenizer.
It will count lines in all files with that extension if there are no tokenizer.
If a the tokenizer is not none, it will count tokens.
For dir with two files from hw1.py:
# >>> print(Path.cwd())
>>> test_dir = Path(Path.cwd(), "../..", "task1/merge_files_iterator")
>>> universal_file_counter(test_dir, "txt")
8
>>> universal_file_counter(test_dir, "txt", str.split)
6
>>> universal_file_counter(Path.cwd(), "txt")
33
>>> universal_file_counter(Path.cwd(), "txt", str.split)
58
"""
from pathlib import Path
from typing import Callable, Optional


def lines_amount(path):
    with open(path) as f:
        for i, l in enumerate(f):
            pass
    return i + 2


def tokens_amount(path, tokenizer):
    with open(path) as f:
        content = f.read()
        return len(tokenizer(content))


def my_file_counter(dir_path: Path, file_extension: str, tokenizer: Optional[Callable] = None):
    for path in Path(dir_path).rglob("*." + file_extension):
        if tokenizer is None:
            yield lines_amount(path)
        else:
            yield tokens_amount(path, tokenizer)


def universal_file_counter(dir_path: Path, file_extension: str, tokenizer: Optional[Callable] = None) -> int:
    return sum(my_file_counter(dir_path, file_extension, tokenizer))
