#!/usr/bin/env python3
"""
Challenge 7 - dictionary attack on a hash chain.

verify checks sha1(md5(sha1(password))) against a stored hash. There's no salt and the
hashes are fast, so a tiny wordlist cracks it right away. Stacking hash functions like
this doesn't really add strength, password strength and a slow salted hash is what
matters.
"""
import hashlib

TARGET = "f6a51c155d95861c35febb700cb661b34f4a85b5"
WORDLIST = ["password", "123456", "12345678", "qwerty", "admin", "letmein", "111111"]


def chain(pw: str) -> str:
    h = hashlib.sha1(pw.encode()).hexdigest()
    h = hashlib.md5(h.encode()).hexdigest()
    return hashlib.sha1(h.encode()).hexdigest()


def main() -> None:
    for pw in WORDLIST:
        if chain(pw) == TARGET:
            print("Password cracked:", pw)
            return
    print("Not found in wordlist.")


if __name__ == "__main__":
    main()
