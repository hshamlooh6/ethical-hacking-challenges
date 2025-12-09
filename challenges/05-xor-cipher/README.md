# Challenge 5 - XOR Cipher

**Flag:** `CTF{XOR_AND_PLAIN_TEXT_KEY}`
**Tools:** JADX-GUI, Python

## What it asks for

Each character is XORed with a repeating key `{5,4,5,9,9,2,0,6,2,3}`, and the result is
compared to `FPCrQMRYCMA[UEHKNYVF]PZBL[}`.

## How I did it

XOR undoes itself, so I XORed the ciphertext with the same key and got the flag back.
The script also re-encrypts the result to double-check it. See [`solve.py`](solve.py).

One small thing: JADX showed a couple of the ciphertext characters wrong in the GUI, so
I read the raw bytes from the class file to get the correct 27 characters.

## How you'd fix it

A short repeating XOR key that's hardcoded in the program is easy to break, especially
when the message is longer than the key. XOR is a building block, not a cipher on its
own. For real encryption use something like AES-GCM with a key that doesn't ship inside
the app.
