def enumerate_gen(iterable, start=0):
    i = start
    for item in iterable:
        yield i, item
        i += 1


class Enumerate:
    def __init__(self, iterable, start=0):
        self.iterable = iterable
        self.index = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.iterable):
            new_state = self.index, self.iterable[self.index]
            self.index += 1
            return new_state
        else:
            raise StopIteration


sample_list = [1, 2, 3, 4, 5]
for i, item in Enumerate(sample_list):
    print(i, item)
