# Challenge 7 - Cracking a Hashed Password

**Flag / password:** `123456`
**Tools:** JADX-GUI, Python (hashlib)

## What it asks for

The check is `sha1(md5(sha1(password)))` compared to a stored hash. So it hashes your
password three times with no salt.

## How I did it

You can't reverse a hash, but you don't need to - the password is weak. I made a short
list of common passwords, ran them through the same three hashes, and `123456` matched
on the second try. See [`solve.py`](solve.py).

## How you'd fix it

This is the main lesson of the whole project for me: stacking fast hashes barely helps.
The real problems are a weak password, no salt (so the same password always gives the
same hash and rainbow tables work), and fast hash functions you can guess billions of
times a second on a GPU. Passwords should be stored with a slow, salted algorithm made
for it - bcrypt, scrypt, or Argon2 - never MD5 or SHA-1, chained or not.
