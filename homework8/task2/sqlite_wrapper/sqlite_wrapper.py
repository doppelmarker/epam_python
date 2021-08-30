import sqlite3


class NoTableError(BaseException):
    pass


class NoSuchItemError(BaseException):
    pass


def exists_table(database_name, table_name):
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()
    query = "SELECT 1 FROM sqlite_master WHERE type='table' and name = ?"
    return cursor.execute(query, (table_name,)).fetchone() is not None


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


def update_data(f):
    def wrapper(*args):
        self = args[0]
        self.data.clear()
        if exists_table(self.database_name, self.table_name):
            query = f"SELECT * from {self.table_name}"
            cursor = self.conn.execute(query)
            while row_dict := cursor.fetchone():
                self.data.append(row_dict)
            print("Data updated!")
        else:
            raise NoTableError(f"No table with name '{self.table_name}' in DB!")
        result = f(*args)
        return result

    return wrapper


class TableData:
    def __init__(self, database_name, table_name):
        self.data = list()
        self.database_name = database_name
        self.table_name = table_name
        self.conn = sqlite3.connect(database_name)

        self.conn.row_factory = dict_factory

        if exists_table(database_name, table_name):
            query = f"SELECT * from {table_name}"
            cursor = self.conn.execute(query)
            while row_dict := cursor.fetchone():
                self.data.append(row_dict)
        else:
            raise NoTableError(f"No table with name '{table_name}' in DB!")

    @update_data
    def __len__(self):
        return len(self.data)

    @update_data
    def __getitem__(self, item):
        for row_dict in self.data:
            if item in row_dict.values():
                return row_dict
        raise NoSuchItemError(f"No item '{item}' stored in DB!")

    def __iter__(self):
        self.n = 0
        return self

    @update_data
    def __next__(self):
        try:
            if self.n < len(self.data):
                return self.data[self.n]
            else:
                raise StopIteration
        finally:
            self.n += 1


presidents = TableData("example.sqlite", "presidents")

while True:
    for president in presidents:
        print(president)

# while True:
#     print(presidents["Yeltsin"])

# while True:
#     print(len(presidents))
