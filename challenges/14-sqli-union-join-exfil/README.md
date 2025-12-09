# Challenge 14 - SQL Injection (Stealing Data Across Tables)

**Payload (username):**
`' UNION SELECT name,username,balance FROM users JOIN account_balance ON users.id=account_balance.user_id ORDER BY balance DESC LIMIT 1--`
**Tools:** JADX-GUI, SQLite

## What it asks for

The program wants the user with the highest balance, and it expects that balance to show
up in the `role` column. The original query selects three columns (name, username, role).
The trick is that SQL lines up UNION columns by position, not name, so if I UNION a query
that selects (name, username, balance), the balance lands where the program reads `role`.

## How I did it

I used UNION with a JOIN to pull the balance from the `account_balance` table, sorted by
balance descending, and took the top row with `LIMIT 1`. That's Charlie with 10000, and
since 10000 ends up in the role slot, the program's check passes. [`demo.py`](demo.py)
builds both tables locally and runs it end to end.

## How you'd fix it

Parameterized queries stop this completely. On top of that, this is really a data-leak
bug, so the login query shouldn't have access to JOIN financial tables, and you shouldn't
trust column names for anything since SQL unions by position.
