# Challenge 11 solver note

This challenge ships three PKCS#8 private-key files but the program wants
`private.key`. Two of the three fail to parse (`algid parse error, not a sequence`);
the third (`private_660b2eb14a.key`) is the real RSA key and decrypts the ciphertext
to `CTF{ASYMMETRIC_ENCRYPTION}`.

The key files are the instructor's material and are **not** redistributed here, so
there is no runnable solver. The approach, in Java (JDK only):

```java
byte[] der = Base64.getDecoder().decode(new String(Files.readAllBytes(Paths.get(keyFile))));
PrivateKey pk = KeyFactory.getInstance("RSA")
        .generatePrivate(new PKCS8EncodedKeySpec(der));
Cipher c = Cipher.getInstance("RSA");
c.init(Cipher.DECRYPT_MODE, pk);
System.out.println(new String(c.doFinal(Base64.getDecoder().decode(CIPHERTEXT))));
```

Wrap it in a loop over the three key paths inside try/catch and print the one that
succeeds.
