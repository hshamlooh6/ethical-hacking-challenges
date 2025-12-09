# Ethical Hacking - 15 Reverse Engineering & Security Challenges

This is my project for the Ethical Hacking course at the University of Bahrain
(ITCE401), submitted on 9 December 2025. The assignment gave us a Java program
(`EthicalHacking.jar`) with 15 hidden challenges, and the job was to decompile it with
[JADX](https://github.com/skylot/jadx), figure out how each challenge works, solve it,
and explain what I did.

The challenges cover a bit of everything: reverse engineering, classical and modern
cryptography, cracking a hashed password, SQL injection, and a threading race condition.
For each one I wrote up how I solved it and also added a short section on how a developer
should actually fix the vulnerability, since that felt like the more useful half.

> **About the ethics:** everything here was done on a deliberately vulnerable program
> made for the course, in a lab, with permission. See [DISCLAIMER.md](DISCLAIMER.md).
> I didn't upload the instructor's files (the JAR, the database, or the key files) -
> only my write-ups and my own scripts. More on that under
> [What's not here](#whats-not-here).

## What I practiced

| Area | Challenges | What's involved |
|------|-----------|------------------|
| Reverse engineering | 1, 2, 6 | Reading decompiled Java, solving constraints, spotting a logic bug |
| Encoding | 3 | Layered Base64, predictable random generator |
| Classical crypto | 4, 5 | Keyed ROT, repeating-key XOR |
| Password hashing | 7 | Dictionary attack on a SHA-1/MD5 chain |
| Applied crypto | 8, 9, 10, 11 | HMAC-SHA256, AES-128-CBC, RSA/PKCS#8, key and IV handling |
| SQL injection | 12, 13, 14 | UNION bypass, stacked-query INSERT, UNION+JOIN data theft |
| Concurrency | 15 | TOCTOU race condition |

## The challenges

| # | Challenge | Folder |
|---|-----------|--------|
| 1 | Constraint solving | [`01-constraint-solving`](challenges/01-constraint-solving) |
| 2 | Regex + math constraints | [`02-regex-xor-constraints`](challenges/02-regex-xor-constraints) |
| 3 | Layered Base64 | [`03-base64-layers`](challenges/03-base64-layers) |
| 4 | Keyed ROT cipher | [`04-rot-cipher-key`](challenges/04-rot-cipher-key) |
| 5 | Repeating-key XOR | [`05-xor-cipher`](challenges/05-xor-cipher) |
| 6 | Logic flaw (input ignored) | [`06-logic-flaw-xor-reverse-base64`](challenges/06-logic-flaw-xor-reverse-base64) |
| 7 | Hash-chain cracking | [`07-hash-chain-cracking`](challenges/07-hash-chain-cracking) |
| 8 | HMAC-SHA256 | [`08-hmac-sha256`](challenges/08-hmac-sha256) |
| 9 | AES-128-CBC | [`09-aes-cbc-fixed-seed`](challenges/09-aes-cbc-fixed-seed) |
| 10 | "Double encryption" (AES+XOR) | [`10-double-encryption`](challenges/10-double-encryption) |
| 11 | RSA key selection | [`11-rsa-key-selection`](challenges/11-rsa-key-selection) |
| 12 | SQLi - UNION login bypass | [`12-sqli-union-auth-bypass`](challenges/12-sqli-union-auth-bypass) |
| 13 | SQLi - stacked INSERT | [`13-sqli-stacked-insert`](challenges/13-sqli-stacked-insert) |
| 14 | SQLi - UNION+JOIN data theft | [`14-sqli-union-join-exfil`](challenges/14-sqli-union-join-exfil) |
| 15 | Race condition (TOCTOU) | [`15-race-condition-toctou`](challenges/15-race-condition-toctou) |

## Running the scripts

```bash
# Python 3.9+. The AES challenges need one package:
pip install -r requirements.txt

python3 challenges/01-constraint-solving/solve.py
python3 challenges/07-hash-chain-cracking/solve.py
python3 challenges/12-sqli-union-auth-bypass/demo.py   # builds its own small test DB
```

Challenges 9 and 10 use the `cryptography` package. Challenge 9 also has a plain Java
version if you'd rather not install anything. For the SQL injection ones (12-14), since I
can't include the instructor's database, the scripts build a tiny copy of the schema so
you can see the payload actually work.

## Things I corrected after the course

When I was cleaning this up for GitHub I re-ran all my solutions and found a few mistakes
in my original report. I fixed them here because I'd rather the public version be right:

- **Challenge 1:** my first script listed 28 answers but 13 were actually invalid (I
  forgot to re-check one condition). The real count is 15. The answer I submitted was
  still a valid one.
- **Challenge 3:** the Base64 layer count is 12, not "about 15", and Python's random
  doesn't actually match Java's.
- **Challenge 4:** the cipher isn't reversible in a unique way (because of how Java
  handles negative `%`), so the flag is ambiguous - the intended one is
  `CTF{ROT_WITH_K_Y}`.
- **Challenge 15:** the millisecond timeline in my report was just an example, not
  something I measured.

Each challenge's README explains its own correction.

## What's not here

I left out the instructor's `EthicalHacking.jar`, the `database.db`, and the `.key` files
on purpose, so I'm not handing out the answers for future students or sharing material
that isn't mine. The write-ups explain the decompiled logic, and the scripts either run
on public inputs or rebuild a small local copy of what they need.

## License

My code and write-ups are under the [MIT license](LICENSE). The course files they talk
about aren't mine and aren't included.
