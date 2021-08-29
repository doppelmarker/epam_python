import os


class KeyValueStorage:
    def __init__(self, file_path):
        super(KeyValueStorage, self).__setattr__("data", dict())

        cur_path = os.path.dirname(__file__)
        with open(os.path.join(cur_path, file_path)) as file:
            for line in file:
                key, value = line.strip().split("=")
                try:
                    self.data[key] = int(value)
                except ValueError:
                    self.data[key] = value

    def __getitem__(self, item):
        try:
            return self.data[item]
        except KeyError:
            return "No such key!"
            # raise AttributeError

    def __setitem__(self, key, value):
        try:
            self.data[key] = int(value)
        except ValueError:
            self.data[key] = value

    __getattr__ = __getitem__

    __setattr__ = __setitem__


storage = KeyValueStorage("task1.txt")
print(storage["name"])
print(storage["song"])
print(storage.songdasdass)
storage.songdasdass = "12345"
print(storage.songdasdass)
