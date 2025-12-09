#!/usr/bin/env python3
"""
Challenge 2 - regex plus arithmetic constraints.

Input: exactly 7 characters matching [0-9A-Z]. Character.getNumericValue maps
'0'-'9' to 0-9 and 'A'-'Z' to 10-35. verify() needs:
    10 <= n4 <= 32
    (n2 * n3) % 10 == n5
    n2 + n4 == n6
    (n1 ^ n7) == 3

Every (n1..n7) combination maps to exactly one [0-9A-Z] string, so the number of valid
inputs equals the number of valid combinations: 447,120. "000A0A3" is one of them.
"""

def to_char(n: int) -> str:
    return str(n) if n < 10 else chr(ord('A') + n - 10)


def main() -> None:
    count = 0
    sample = None
    for n1 in range(36):
        for n7 in range(36):
            if (n1 ^ n7) != 3:
                continue
            for n2 in range(36):
                for n4 in range(10, 33):
                    n6 = n2 + n4
                    if n6 > 35:
                        continue
                    for n3 in range(36):
                        n5 = (n2 * n3) % 10
                        code = (to_char(n1) + to_char(n2) + to_char(n3) +
                                to_char(n4) + to_char(n5) + to_char(n6) + to_char(n7))
                        count += 1
                        if sample is None:
                            sample = code
    print(f"Found {count} valid 7-character codes.")
    print("Example valid input:", sample)
    print("Submitted answer: 000A0A3")


if __name__ == "__main__":
    main()
