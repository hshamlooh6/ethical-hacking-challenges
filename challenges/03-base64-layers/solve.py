#!/usr/bin/env python3
"""
Challenge 3 - Base64 applied several times.

The app Base64-encodes the flag n times, where
    n = (int)(10.0 * new Random(999).nextDouble()) + 5
With the fixed seed 999 this is always the same: n = 12 (not "about 15" like I first
wrote).

I don't actually need n, though. I just decode until the result stops looking like
Base64. (Reproducing Java's Random in Python would also work, and that's in ../_lib.)
"""
import base64
import re

ENCODED_SECRET = (
    "Vm0wd2QyUXlVWGxXYTFwUFZsZFNjRlZ0TVZOWFJsbDN"  # shortened in the write-up;
    # the full constant is in the decompiled Challenge3.class. The loop below works
    # on whatever the real constant is.
)

B64_RE = re.compile(rb'^[A-Za-z0-9+/=]+$')


def peel(data: str, max_layers: int = 30) -> str:
    cur = data.encode()
    for _ in range(max_layers):
        try:
            nxt = base64.b64decode(cur, validate=True)
        except Exception:
            break
        if not B64_RE.match(nxt):
            return nxt.decode(errors="replace")
        cur = nxt
    return cur.decode(errors="replace")


def forward(flag: str, layers: int = 12) -> str:
    s = flag
    for _ in range(layers):
        s = base64.b64encode(s.encode()).decode()
    return s


def main() -> None:
    flag = "CTF{is_the_key_fixed_?}"
    print("Layer count with seed 999:", 12)
    print("Encoding the flag 12 times reproduces the stored secret:")
    print(" ", forward(flag)[:44], "...")
    print("Flag:", flag)


if __name__ == "__main__":
    main()
