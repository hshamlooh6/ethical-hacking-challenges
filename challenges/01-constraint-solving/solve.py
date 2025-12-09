#!/usr/bin/env python3
"""
Challenge 1 - constraint solving / reverse engineering.

The decompiled verify() reads six digits n1..n6 from a 6-character input and checks:
    f1: n2 + n3 == n5 % 10     (so n2 + n3 has to be a single digit, i.e. 9 or less)
    f2: n2 + 2  == n6
    f3: n1 + 2  == n4  and  n1 >= 6
    f4: all six characters are unique

The brute force below applies f1 exactly like the Java does. My original search script
instead set n5 = (n2 + n3) % 10 and never re-checked f1, so it printed 28 "answers",
and 13 of them (like 637805, where 3 + 7 = 10) don't actually pass. The real set has
15. 623854, which is what I submitted, works either way.
"""
from itertools import product


def valid(code: str) -> bool:
    if len(code) != 6 or not code.isdigit():
        return False
    n1, n2, n3, n4, n5, n6 = (int(c) for c in code)
    f1 = (n2 + n3) == (n5 % 10)
    f2 = (n2 + 2) == n6
    f3 = (n1 + 2) == n4 and n1 >= 6
    f4 = len(set(code)) == 6
    return f1 and f2 and f3 and f4


def main() -> None:
    solutions = [''.join(p) for p in product('0123456789', repeat=6) if valid(''.join(p))]
    print(f"Found {len(solutions)} valid solution(s):")
    for s in solutions:
        print(" ", s)
    assert "623854" in solutions
    print("\nSubmitted answer: 623854")


if __name__ == "__main__":
    main()
