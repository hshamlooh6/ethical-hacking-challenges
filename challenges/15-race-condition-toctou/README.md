# Challenge 15 - Race Condition (TOCTOU)

**Flag:** `CTF{THREAD_DIAGNOSIS_FOR_RACE_CONDITION}`
**Working threads:** first `3`, then `0`
**Tools:** JADX-GUI, analysis in Java/Python

## What it asks for

There's a vault that starts at 100. `withdraw(threadId)` checks if the balance is at
least 70, and for certain "vulnerable" threads it sleeps 10ms *before* subtracting 70.
That little sleep is the whole problem - it's a gap between checking and acting (a
time-of-check to time-of-use bug). A thread is vulnerable if `(threadId*threadId) % 10 ==
9` (threads 3 and 7) or `(threadId >> 1) == 3` (threads 6 and 7), so 3, 6, and 7.

## How I did it

To push the balance to exactly -40, I needed one vulnerable thread to open the window and
one fast thread to sneak in during the sleep, and the vulnerable one has to start first.
With 3 then 0: thread 3 checks (100, passes, sleeps), thread 0 checks (still 100, passes,
withdraws, balance 30), then thread 3 wakes up and withdraws, balance -40. The script
[`analyze.py`](analyze.py) works out the vulnerable/fast threads and picks a pair.

## A note on my report

The exact millisecond timeline I wrote ("at time 1, at time 7...") is just an example to
explain it, not something I measured. Real sleeps and thread scheduling aren't that
precise, so the race is more of a probability - which is exactly why starting the
vulnerable thread first matters, so the window is definitely open before the fast thread
reads the balance.

## How you'd fix it

Make the check-and-subtract one atomic step: a `synchronized` block, a lock, an
`AtomicInteger` with `compareAndSet`, or a database transaction with proper isolation.
The bug is the gap between checking and using the balance, so closing that gap fixes it.
