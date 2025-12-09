"""
A small version of java.util.Random written in Python (it's just a linear
congruential generator).

A few challenges build their "secret" salt, key, or loop count from
new Random(someFixedSeed). Because the algorithm and the seed are both known, the
output is completely repeatable, which is really the point: seeding a random
generator with a constant means it isn't secret at all.
"""

MASK = (1 << 48) - 1
MULT = 0x5DEECE66D
ADD = 0xB


class JavaRandom:
    def __init__(self, seed: int):
        self.seed = (seed ^ MULT) & MASK

    def _next(self, bits: int) -> int:
        self.seed = (self.seed * MULT + ADD) & MASK
        val = self.seed >> (48 - bits)
        # Java returns a signed 32-bit int, so wrap values above 2^31
        if val >= (1 << 31):
            val -= (1 << 32)
        return val

    def next_int(self) -> int:
        return self._next(32)

    def next_int_bound(self, bound: int) -> int:
        if bound <= 0:
            raise ValueError("bound must be positive")
        if (bound & -bound) == bound:  # bound is a power of two
            return (bound * self._next(31)) >> 31
        while True:
            bits = self._next(31)
            val = bits % bound
            if bits - val + (bound - 1) >= 0:
                return val

    def next_double(self) -> float:
        hi = self._next(26)
        lo = self._next(27)
        return ((hi << 27) + lo) / float(1 << 53)
