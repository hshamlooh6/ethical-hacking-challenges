#!/usr/bin/env python3
"""
Challenge 5 - repeating-key XOR.

cipher[i] = plain[i] XOR key[i % 10]. XOR undoes itself, so running the same key over
the ciphertext gives the plaintext back.
"""
KEY = [5, 4, 5, 9, 9, 2, 0, 6, 2, 3]
CIPHERTEXT = "FPCrQMRYCMA[UEHKNYVF]PZBL[}"


def xor(text: str) -> str:
    return ''.join(chr(ord(c) ^ KEY[i % 10]) for i, c in enumerate(text))


def main() -> None:
    flag = xor(CIPHERTEXT)
    print("Flag:", flag)
    assert xor(flag) == CIPHERTEXT  # round-trips, so the key is right


if __name__ == "__main__":
    main()
