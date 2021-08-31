from contextlib import contextmanager


class MySuppressor:
    def __init__(self, exc):
        self.exc = exc

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.exc is exc_type:
            return True


@contextmanager
def suppressor(exc):
    try:
        yield
    except exc:
        pass


with MySuppressor(IndexError):
    [][0]

with suppressor(IndexError):
    [][0]
