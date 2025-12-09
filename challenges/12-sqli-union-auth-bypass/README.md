# Challenge 12 - SQL Injection (Login Bypass with UNION)

**Payload (username):** `' UNION SELECT id,name,role FROM admins--`
**Tools:** JADX-GUI, SQLite

## What it asks for

It's a login that builds its SQL by gluing strings together:

```
SELECT id,name,role FROM users WHERE username='<input>' AND password=('<md5>')
```

The admins are in a separate `admins` table that this query never looks at. There are
three "protections": only one single quote allowed in the username, the word `where` is
blocked, and the password is MD5'd. None of them stop a UNION.

## How I did it

The payload closes the username string with one quote, UNIONs a SELECT from `admins` with
the same 3 columns, and `--` comments out the rest of the query (including the password
check). So it logs in as the admin `victor`. The filters don't help - UNION doesn't need
a second quote or the word `where`, and the comment removes the password check anyway.

The instructor's `database.db` isn't included, so [`demo.py`](demo.py) builds a small
copy of the schema and runs the real vulnerable query with the payload so you can see it
work.

## How you'd fix it

Use prepared statements / parameterized queries - never build SQL by concatenating user
input. Blocking quotes and keywords doesn't work (this challenge gets past all of it).
Also give the login query the least privilege it needs, so it can't read an `admins`
table it has no reason to touch.
