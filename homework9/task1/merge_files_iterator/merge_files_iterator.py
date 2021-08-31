"""
Write a function that merges integer from sorted files and returns an iterator
file1.txt:
1
3
5
file2.txt:
2
4
6
# >>> list(merge_sorted_files(["file1.txt", "file2.txt"]))
[1, 2, 3, 4, 5, 6]
"""
import os
from pathlib import Path
from typing import Iterator, List, Union


class FilesIterator:
    def __init__(self, file_names):
        self.file_names = file_names
        self.cur_file = None
        self.cur_filename = None
        self.path = os.path.dirname(__file__)

    def __iter__(self):
        self.n = 0
        self.cur_filename = self.file_names[self.n]
        self.cur_file = open(os.path.join(self.path, self.cur_filename))
        return self

    def __next__(self):
        result = self.cur_file.readline().strip()
        if result == "":
            self.cur_file.close()
            self.cur_file = None
            self.n += 1
            if self.n < len(self.file_names):
                self.cur_filename = self.file_names[self.n]
                self.cur_file = open(os.path.join(self.path, self.cur_filename))
                result = self.cur_file.readline().strip()
        if self.n < len(self.file_names):
            return result
        else:
            raise StopIteration


# def merge_sorted_files(file_list: List[Union[Path, str], ...]) -> Iterator:
#     return FilesIterator(file_list)


def merge_sorted_files(file_list) -> Iterator:
    return FilesIterator(file_list)


print(
    list(
        merge_sorted_files(
            [
                "file1.txt",
                "file2.txt",
            ]
        )
    )
)
