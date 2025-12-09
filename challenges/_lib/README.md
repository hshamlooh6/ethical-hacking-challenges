# Shared helpers

[`java_random.py`](java_random.py) — a small pure-Python reimplementation of
`java.util.Random` (a Linear Congruential Generator). Several challenges derive
"secret" salts, keys, or iteration counts from `new Random(fixedSeed)`. Because the
algorithm and seed are both known, the output is fully reproducible — which is the
whole point: a PRNG seeded with a constant is not a source of secrecy. Used by
challenges 8 and 9 (and to verify 3).
