# Challenge 9 - AES-128-CBC

**Flag:** `CTF{SYMMETRIC_ENCRYPTION_WTHI_AES}` (the `WTHI` typo is in the flag itself)
**Tools:** JADX-GUI, Python or Java

## What it asks for

It uses AES-128 in CBC mode. The 16-byte key comes from `new Random(89893).nextInt(256)`
and the IV is just the bytes 0 to 15. Both are fixed and visible in the code, so there's
really no secret here.

## How I did it

I rebuilt the key (using the Java `Random` reimplementation) and the IV, then decrypted
the ciphertext. There are two versions: [`solve.py`](solve.py) in Python, and
[`solve_java/Solve9.java`](solve_java/Solve9.java) in plain Java if you don't want to
install anything.

## How you'd fix it

AES itself is strong - the weak part is the key and IV handling. A key built from a
hardcoded seed isn't secret, and a fixed/sequential IV breaks CBC (identical blocks
leak). Use a random key from a proper key store, a fresh random IV per message, and
ideally AES-GCM so tampering gets detected too.
