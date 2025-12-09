#!/usr/bin/env python3
"""
Challenge 8 - HMAC-SHA256 with a fixed key and a Random-based salt.

Key: the 16 bytes 15..30. Salt: comes from new Random(99), but a loop bound overflows
a 32-bit int so the loop only runs once, which leaves salt = -1244121273. Message:
"CTF{HMAC_WITH_SALT}_" + salt. Instead of hardcoding the salt I rebuild Java's Random
stream in Python (see ../_lib/java_random.py) so it comes out on its own.
"""
import base64
import hashlib
import hmac
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_lib"))
from java_random import JavaRandom  # noqa: E402


def i32(x: int) -> int:
    # wrap to a signed 32-bit int, like Java does in the loop bound
    x &= 0xFFFFFFFF
    return x - 2**32 if x >= 2**31 else x


def derive_salt() -> int:
    r = JavaRandom(99)
    i = 0
    while i < i32(r.next_int() + 1196652909):  # bound overflows, so this runs once
        r.next_int()
        i += 1
    return r.next_int()


def main() -> None:
    salt = derive_salt()
    key = bytes(range(15, 31))
    message = f"CTF{{HMAC_WITH_SALT}}_{salt}".encode()
    mac = base64.b64encode(hmac.new(key, message, hashlib.sha256).digest()).decode()
    print("Derived salt:", salt)
    print("Answer (HMAC-SHA256, Base64):", mac)


if __name__ == "__main__":
    main()
