#!/usr/bin/env python3
"""
Challenge 10 - "double encryption": AES-128-CBC with a simple XOR on top.

The ciphertext bytes were XORed with (i % 16) after the AES-CBC step. I undo the XOR
first, then AES-decrypt. Key = bytes 15,14,...,0; IV = bytes 0..15. Putting a weak XOR
over AES doesn't add anything, it's just security by obscurity.
"""
import base64

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.padding import PKCS7

CIPHERTEXT_B64 = "ZoyMYEjIDBhG2z8mECsTG05S8XyjbzAzqlABtNA4us0="


def main() -> None:
    ct = bytearray(base64.b64decode(CIPHERTEXT_B64))
    for i in range(len(ct)):
        ct[i] ^= (i % 16)
    key = bytes(range(15, -1, -1))
    iv = bytes(range(16))
    dec = Cipher(algorithms.AES(key), modes.CBC(iv)).decryptor()
    padded = dec.update(bytes(ct)) + dec.finalize()
    unpad = PKCS7(128).unpadder()
    pt = unpad.update(padded) + unpad.finalize()
    print("Flag:", pt.decode())


if __name__ == "__main__":
    main()
