# Challenge 4 - ROT Cipher With a Key

**Flag (intended):** `CTF{ROT_WITH_K_Y}`
**Tools:** JADX-GUI, Python

## What it asks for

It's a rotation cipher with a repeating key `{9,7,5,6,1,5,0,6,2,3}`. Each character
becomes `(ord(c) + key[i % 10] - 97) % 26`, then back to a letter, and it's compared to
`L[KgSTTeYL]OdQ`^c`.

## How I did it

To reverse it I just subtracted the key value at each position. That gave me a string
that matches. See [`solve.py`](solve.py).

## The interesting part

This is the one I found most interesting. In Java, `%` can give a negative result, so
this cipher isn't actually one-to-one - different inputs can encrypt to the same thing.
The answer I submitted was `CTFaROT_WITH_K_Yc`, which does encrypt to the target, but
the flag the instructor meant is almost certainly `CTF{ROT_WITH_K_Y}`. The reason is
`{` and `a` both encrypt to the same character, and so do `}` and `c`. My solver shows
both strings producing the exact same ciphertext. So my answer worked, but it was really
one of many possible inputs, not "the" flag.

## How you'd fix it

Don't write your own cipher, and definitely don't use one where decryption isn't unique.
If you need something keyed and reversible, use a real algorithm like AES.
