import sqlite3
 
connection = sqlite3.connect("db.sqlite3")
tables = connection.execute(
    "SELECT name FROM sqlite_master WHERE type='table' AND name LIKE 'applications_%'"
).fetchall()
 
for (table_name,) in tables:
    print(table_name)
    for column in connection.execute(f"PRAGMA table_info({table_name})"):
        # column = (position, name, type, not_null, default, primary_key)
        print("    ", column[1], column[2], "NOT NULL" if column[3] else "")
