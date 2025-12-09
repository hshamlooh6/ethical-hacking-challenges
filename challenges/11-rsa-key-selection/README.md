# Challenge 11 - Picking the Right RSA Key

**Flag:** `CTF{ASYMMETRIC_ENCRYPTION}`
**Tools:** JADX-GUI, Java

## What it asks for

The program looks for a file called `private.key`, but the folder actually has three
different keys (`private_223467228e.key`, `private_49e3ae3ff1.key`,
`private_660b2eb14a.key`). Two of them fail to load with an "algid parse error", and the
third is the real RSA key that decrypts the message.

## How I did it

I looped over the three files and tried RSA decryption on each inside a try/catch,
printing whichever one worked. The one that worked was `private_660b2eb14a.key`. The Java
snippet is in [`README_SOLVE.md`](README_SOLVE.md). I didn't include the actual key files
here since they're the instructor's, so there's no runnable script in this folder.

## How you'd fix it

The real weakness is key management - leaving private keys lying around in the app folder
where you can just try them one by one. Private keys belong in a protected store (an HSM,
a key manager, or an OS keystore with tight permissions), not next to the program. RSA
is fine when the keys are stored properly and a modern padding like OAEP is used.
