# Challenge 13 - SQL Injection (Creating an Admin)

**Payload (username):**
`x'; INSERT INTO admins (username, password, name, role) VALUES ('tester@app.com', 'hash', 'tester', 'admin');--`
**Tools:** JADX-GUI, SQLite

## What it asks for

This one runs a `SELECT` through `executeUpdate()` instead of `executeQuery()`.
`executeUpdate()` is meant for changing data and it lets you run several statements
separated by `;`. The filters block `select` and `where` but not `insert`, so I can end
the first statement and add my own INSERT to make a new admin.

## How I did it

The payload closes the username, `;` ends the SELECT, then INSERTs a row into `admins`
with the exact values the check wants, and `--` comments out the leftover password check.
After that the new `tester` admin exists. [`demo.py`](demo.py) shows this on a local copy
of the database (using `executescript` to act like Java's multi-statement
`executeUpdate`).

## How you'd fix it

Parameterized statements again, plus use the right method (`executeQuery` for reads, not
`executeUpdate` for a SELECT), turn off multiple statements on the driver, and use a
limited DB account so the app can't INSERT into `admins` in the first place. Blacklisting
words isn't a real defense.
