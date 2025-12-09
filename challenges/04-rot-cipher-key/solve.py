#!/usr/bin/env python3
"""
Challenge 4 - keyed ROT cipher that isn't actually reversible.

Each character: loc = (ord(c) + key[i % 10] - 97) % 26, then back to a letter.
The catch is that Java's % can return negative numbers, so this map isn't one-to-one
and different inputs can encrypt to the same thing. Subtracting the key gives back one
valid input, but not the only one. I submitted "CTFaROT_WITH_K_Yc"; the intended flag
is almost certainly "CTF{ROT_WITH_K_Y}", since '{' and 'a' encrypt to the same
character (and so do '}' and 'c'). This script prints both and shows they collide.
"""
KEY = [9, 7, 5, 6, 1, 5, 0, 6, 2, 3]
TARGET = "L[KgSTTeYL]OdQ`^c"


def jmod(v: int, m: int = 26) -> int:
    # match Java's %, where the sign follows the dividend
    r = abs(v) % m
    return r if v >= 0 else -r


def enc(text: str) -> str:
    return ''.join(chr(97 + jmod(ord(c) + KEY[i % 10] - 97)) for i, c in enumerate(text))


def main() -> None:
    naive = ''.join(chr(ord(c) - KEY[i % 10]) for i, c in enumerate(TARGET))
    intended = "CTF{ROT_WITH_K_Y}"
    print("Subtract-the-key result:", naive, "->", "match" if enc(naive) == TARGET else "no")
    print("Intended flag          :", intended, "->", "match" if enc(intended) == TARGET else "no")
    print("\nBoth encrypt to the same thing, so the cipher can't be reversed uniquely.")
    print("Flag (intended):", intended)


if __name__ == "__main__":
    main()
