from collections import namedtuple
from typing import Iterator

Page = namedtuple("Page", ["text", "number"])


class Book:
    def __init__(self) -> None:
        self.pages = []

    def add_page(self, text: str) -> None:
        self.pages.append(Page(text, number=len(self.pages) + 1))

    def __iter__(self) -> Iterator[Page]:
        return BookIter(self)


class PurchasableBook(Book):
    def __init__(self, purchased: bool = False) -> None:
        self.purchased = purchased
        super().__init__()

    def __iter__(self) -> "PurchasableBookIter":
        return PurchasableBookIter(self)


class BookIter:
    def __init__(self, book: Book) -> None:
        self.pages = book.pages
        self.book = book
        self._cursor = 0  # self._cursor = -1

    def __iter__(self) -> "BookIter":
        return self

    def __next__(self) -> Page:
        if len(self.pages) > self._cursor:  # self._cursor += 1
            result = self.pages[self._cursor]  # if len(self.pages) > self._cursor:
            self._cursor += 1  # return self.pages[self._cursor]
            return result
        raise StopIteration  # raise StopIteration


class PurchasableBookIter(BookIter):
    def __init__(self, book: Book):
        self.purchased = book.purchased
        super().__init__(book)

    def __next__(self) -> Page:
        if not self.purchased and self._cursor > 0:
            print("Buy the book to view next pages!")
            raise StopIteration
        return super().__next__()


purchased_book = PurchasableBook()
for i in range(1, 5):
    purchased_book.add_page(f"page_{i}")

# for page in purchased_book:
#     print(page)

it = iter(purchased_book)

for page in it:
    print(page)

purchased_book.purchased = True
it = iter(purchased_book)

for page in it:
    print(page)
