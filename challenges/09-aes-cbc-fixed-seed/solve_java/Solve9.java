import java.util.*;
import javax.crypto.*;
import javax.crypto.spec.*;

/* Same as solve.py, but in plain Java so it needs no extra libraries (just the JDK). */
public class Solve9 {
    public static void main(String[] a) throws Exception {
        Random r = new Random(89893L);
        byte[] key = new byte[16];
        for (int i = 0; i < 16; i++) key[i] = (byte) r.nextInt(256);
        byte[] iv = new byte[16];
        for (int i = 0; i < 16; i++) iv[i] = (byte) i;
        byte[] ct = Base64.getDecoder().decode(
            "9NNfdf4EJdw3WER+yCk85JzYqELI4py5GJS8rZZJHAejA+kvEIV2w1vTM/H9gws0");
        Cipher c = Cipher.getInstance("AES/CBC/PKCS5Padding");
        c.init(Cipher.DECRYPT_MODE, new SecretKeySpec(key, "AES"), new IvParameterSpec(iv));
        System.out.println("Flag: " + new String(c.doFinal(ct)));
    }
}
