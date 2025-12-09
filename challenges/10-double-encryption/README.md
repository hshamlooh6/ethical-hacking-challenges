# Challenge 10 - "Double Encryption"

**Flag:** `CTF{DOUBLE_ENCRYPTION}`
**Tools:** JADX-GUI, Python

## What it asks for

This one does AES-128-CBC and then XORs each ciphertext byte with `(i % 16)` on top. The
key is the bytes 15 down to 0, and the IV is 0 to 15 again.

## How I did it

I undid the XOR first (it's just position-based), then decrypted the AES like challenge
9. See [`solve.py`](solve.py).

## How you'd fix it

Putting a simple XOR on top of AES adds nothing - it's security by obscurity, and anyone
reading the code peels it off in one line. Don't stack homemade layers. One solid
algorithm like AES-GCM with proper key handling is the way to go.
