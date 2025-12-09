# Challenge 2 - Regex + Math Constraints

**Flag / accepted input:** `000A0A3` (one of many valid inputs)
**Tools:** JADX-GUI, Python

## What it asks for

The input has to be exactly 7 characters and match `[0-9A-Z]`. Java's
`getNumericValue` turns `0-9` into 0..9 and `A-Z` into 10..35. Then `verify()` needs:

- `10 <= n4 <= 32`
- `(n2 * n3) % 10 == n5`
- `n2 + n4 == n6`
- `n1 XOR n7 == 3`

## How I did it

Same idea as challenge 1 but with the character mapping. I looped through the values,
skipped early whenever the XOR condition failed to save time, and counted everything
that passed. Each valid combination maps to exactly one `[0-9A-Z]` string, so the number
of valid inputs is **447,120**. `000A0A3` is the one I used. See [`solve.py`](solve.py).

## How you'd fix it

Same story as challenge 1 - this is a client-side check that gives away the whole rule.
Validate on the server and don't treat "passes a regex plus some math" as a real secret.
