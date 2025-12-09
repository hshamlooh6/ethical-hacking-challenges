# Challenge 6 - The Input Doesn't Even Matter

**Flag:** `CTF{REVERSE_THE_FLOW}`
**Tools:** JADX-GUI, Python

## What it asks for

At first it looks like a three-step cipher (XOR, then reverse the string, then Base64)
compared to a stored value. But when I read `main()` in JADX I noticed something: it
calls `in.nextLine()` to read your input and then just throws the result away. Right
after, it calls `verify("CTF{REVERSE_THE_FLOW}")` with the answer written directly in
the code. So whatever you type does nothing - the flag is literally sitting in `main()`.

## How I did it

I read the flag straight out of the decompiled code, then ran the three steps forward on
it to confirm it matches the stored target. See [`solve.py`](solve.py).

## How you'd fix it

Two problems here: the answer is hardcoded in client code, and the program reads input
and ignores it (which is just a bug). Real input should be validated on the server
against a stored hash.
