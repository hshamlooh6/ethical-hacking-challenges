#!/usr/bin/env python3
"""
Challenge 9 - AES-128-CBC with a seeded key and a predictable IV.

Key: 16 bytes from new Random(89893).nextInt(256). IV: just the bytes 0..15. Both are
fixed and visible in the code, so the ciphertext decrypts without any real secret.

Needs the 'cryptography' package (pip install cryptography). I originally solved this
in Java, and that version is in solve_java/Solve9.java.
"""
import base64
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_lib"))
from java_random import JavaRandom  # noqa: E402

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.padding import PKCS7

CIPHERTEXT_B64 = "9NNfdf4EJdw3WER+yCk85JzYqELI4py5GJS8rZZJHAejA+kvEIV2w1vTM/H9gws0"


def main() -> None:
    r = JavaRandom(89893)
    key = bytes(r.next_int_bound(256) for _ in range(16))
    iv = bytes(range(16))
    ct = base64.b64decode(CIPHERTEXT_B64)
    dec = Cipher(algorithms.AES(key), modes.CBC(iv)).decryptor()
    padded = dec.update(ct) + dec.finalize()
    unpad = PKCS7(128).unpadder()
    pt = unpad.update(padded) + unpad.finalize()
    print("Flag:", pt.decode())


if __name__ == "__main__":
    main()
