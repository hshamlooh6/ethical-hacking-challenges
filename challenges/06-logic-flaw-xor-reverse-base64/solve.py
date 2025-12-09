#!/usr/bin/env python3
"""
Challenge 6 - the real bug is a logic flaw, not the crypto.

main() calls in.nextLine() but throws the result away, then calls
verify("CTF{REVERSE_THE_FLOW}") with the answer hardcoded. So whatever you type does
nothing and the flag is right there in the source. I confirm it by running the forward
pipeline (XOR, then reverse the string, then Base64) and matching the stored target.
"""
import base64

KEY = [2, 3, 4, 9, 1, 5, 0, 6, 2, 3]
TARGET = "f1RNSkZaREFQXEdQUENWQFNyQldB"


def xor(text: str) -> str:
    return ''.join(chr(ord(c) ^ KEY[i % 10]) for i, c in enumerate(text))


def main() -> None:
    flag = "CTF{REVERSE_THE_FLOW}"
    produced = base64.b64encode(xor(flag)[::-1].encode()).decode()
    print("Pipeline output:", produced)
    print("Stored target  :", TARGET)
    print("Match:", produced == TARGET)
    print("Flag:", flag)


if __name__ == "__main__":
    main()
