# Challenge 8 - HMAC-SHA256

**Answer:** `CgZ7nlPGUOgcmmxlE13MUiLlNusr9AWXImoLSsSdU4s=`
**Tools:** JADX-GUI, Python

## What it asks for

The program builds the message `"CTF{HMAC_WITH_SALT}_" + salt` and computes its
HMAC-SHA256 with a 16-byte key (the bytes 15 to 30). The salt comes from `new Random(99)`
after a loop, and the loop bound overflows a 32-bit int so it actually only runs once,
which leaves the salt as `-1244121273`.

## How I did it

Instead of just hardcoding the salt, I reproduced Java's `Random` in Python
([`../_lib/java_random.py`](../_lib/java_random.py)) and copied the overflow behavior in
the loop, so the salt comes out on its own. Then I computed the HMAC. The result matches
what the program expects. See [`solve.py`](solve.py).

Figuring out that the loop bound overflows was the annoying part - at first my Python
loop ran way more times than the Java one because Python integers don't overflow.

## How you'd fix it

HMAC is fine, the problem is where the inputs come from. The key is a fixed sequence
baked into the program and the salt comes from a random generator with a constant seed,
so both can be recovered by reading the code. Use `SecureRandom` for salts and keep the
HMAC key out of the client.
