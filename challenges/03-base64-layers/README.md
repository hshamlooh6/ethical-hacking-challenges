# Challenge 3 - Base64, Over and Over

**Flag:** `CTF{is_the_key_fixed_?}`
**Tools:** JADX-GUI, Python

## What it asks for

The app runs Base64 on your input a bunch of times and compares it to a stored string.
The number of times is `n = (int)(10.0 * new Random(999).nextDouble()) + 5`.

## How I did it

I didn't bother reproducing the exact count at first - I just kept Base64-decoding the
stored string until the result stopped looking like Base64, and that gave me the flag.
That's in [`solve.py`](solve.py).

## A correction

In my report I said it was encoded "about 15 times." It's actually exactly **12** with
that seed. I checked it two ways: encoding `CTF{is_the_key_fixed_?}` 12 times gives back
the stored string, and a small reimplementation of Java's `Random`
([`../_lib/java_random.py`](../_lib/java_random.py)) returns 12 for seed 999. Also, my
original script used Python's `random.seed(999)` to "get" the count, but that doesn't
actually match Java - Python and Java use completely different random generators. It only
worked because my decode-until-not-Base64 loop doesn't depend on the count at all.

## How you'd fix it

Base64 is encoding, not encryption - it hides nothing, and doing it many times doesn't
change that. And seeding a random generator with a fixed number means it's totally
predictable. If you need something unpredictable, use `SecureRandom`.
