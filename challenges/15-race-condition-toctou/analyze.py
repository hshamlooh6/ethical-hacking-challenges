#!/usr/bin/env python3
"""
Challenge 15 - TOCTOU race condition, working out which threads to use.

A SecureVault starts at balance 100. withdraw(threadId) checks balance >= 70, then for
"vulnerable" threads it sleeps 10ms before subtracting 70. That sleep is the race
window. A thread is vulnerable if:
    (threadId * threadId) % 10 == 9   -> threads 3, 7
    (threadId >> 1) == 3              -> threads 6, 7

To force the balance to -40 you need one vulnerable thread (to open the window) and one
fast thread (to slip in during the sleep). Start the vulnerable one first, e.g. thread 3
then thread 0. Timeline: T3 checks (100, passes, sleeps), T0 checks (still 100, passes,
withdraws, balance 30), T3 wakes up and withdraws, balance -40.

The millisecond-by-millisecond timeline in my report is just an example, not something
I measured. Real sleep and scheduling timing varies, so the race is really a
probability, which is why the order (vulnerable thread first) matters.

Flag: CTF{THREAD_DIAGNOSIS_FOR_RACE_CONDITION}
"""


def vulnerable(tid: int) -> bool:
    return (tid * tid) % 10 == 9 or (tid >> 1) == 3


def main() -> None:
    vuln = [t for t in range(10) if vulnerable(t)]
    fast = [t for t in range(10) if not vulnerable(t)]
    print("Vulnerable threads (have the sleep window):", vuln)
    print("Fast threads (slip in during the sleep)   :", fast)
    print("Combination that works: first =", 3, "(vulnerable), second =", 0, "(fast)")
    print("Flag: CTF{THREAD_DIAGNOSIS_FOR_RACE_CONDITION}")


if __name__ == "__main__":
    main()
