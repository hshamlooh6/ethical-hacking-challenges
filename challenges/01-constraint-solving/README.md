# Challenge 1 - Constraint Solving

**Flag / accepted input:** `623854`
**Tools:** JADX-GUI, Python

## What it asks for

The program wants a 6-character secret. I opened `Challenge1.class` in JADX and read
the `verify()` method. It splits the input into six digits (n1..n6) and only accepts it
if all of these are true:

- `n2 + n3 == n5 % 10`
- `n2 + 2 == n6`
- `n1 + 2 == n4`, and `n1 >= 6`
- all six characters are different

## How I did it

Since it's only 6 digits, I just brute forced every combination in Python and kept the
ones that pass all four conditions. The script is [`solve.py`](solve.py).

## Something I got wrong the first time

In my first script I set `n5 = (n2 + n3) % 10` and then added the candidate to my list
without actually re-checking the first condition. The problem is the Java check is
`n2 + n3 == n5 % 10`, which is only possible when `n2 + n3` is a single digit (<= 9).
Because I skipped that, my script printed 28 "answers" and 13 of them don't really work
(for example `637805`: 3 + 7 = 10, which can never match). When I apply the condition
properly there are only **15** valid answers:

```
614853 621834 623854 625874 627894 631845 634875 654897
714953 715963 721934 723954 726984 731945 741956
```

The answer I handed in, `623854`, is one of the real ones, so the submission was fine -
it was just my full list that was off.

## How you'd fix this kind of thing

The whole check sits inside the client where anyone can decompile it, so it isn't really
security. Real validation should run on a server, and a password shouldn't be something
you can rebuild just by reading the rules in the bytecode. If it has to be a secret,
store a salted hash of it instead.
