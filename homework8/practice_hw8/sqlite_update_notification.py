import sqlite3
from ctypes import *

SQLITE_DELETE = 9
SQLITE_INSERT = 18
SQLITE_UPDATE = 23


def callback(user_data, operation, db_name, table_name, row_id):
    if operation == SQLITE_DELETE:
        optext = "Deleted row"
    elif operation == SQLITE_INSERT:
        optext = "Inserted row"
    elif operation == SQLITE_UPDATE:
        optext = "Updated row"
    else:
        optext = "Unknown operation on row"
    s = f"{optext} {row_id} of table {table_name.decode('utf-8')} in database {db_name.decode('utf-8')}"
    print(s)


c_callback = CFUNCTYPE(c_void_p, c_void_p, c_int, c_char_p, c_char_p, c_int64)(callback)

dll = CDLL("sqlite3.dll")
db = c_void_p()
db_name = "example.sqlite"
dll.sqlite3_open(db_name.encode("utf-8"), byref(db))
dll.sqlite3_update_hook(db, c_callback, None)
err = c_char_p()

dll.sqlite3_exec(db, b"create table foo (id int, name varchar(255))", None, None, byref(err))
if err:
    print(err.value.decode("utf-8"))
dll.sqlite3_exec(db, b'insert into foo values (1, "Bob")', None, None, byref(err))
if err:
    print(err.value.decode("utf-8"))
