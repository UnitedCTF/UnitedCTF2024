import java.io.ByteArrayOutputStream;
import java.util.Arrays;
import java.util.Base64;
import java.util.HexFormat;

public class ComplexObfuscatorService extends ObfuscatorService {
    protected String obfuscate(String text) {
        int depth = 10;
        Base64.Encoder encoder = Base64.getEncoder();
        byte[] key = new byte[depth];
        String b64 = text;
        for (int i = 0; i < depth; i++) {
            b64 = new String(encoder.encode(b64.getBytes()));
            key[i] = b64.getBytes()[i];
        }
        int[] res = xor(text.getBytes(), key);
        byte[] res2 = Arrays.stream(res).map(i -> Integer.valueOf(i + res.length).byteValue()).collect(ByteArrayOutputStream::new, (baos, i) -> baos.write((byte) i),
                        (baos1, baos2) -> baos1.write(baos2.toByteArray(), 0, baos2.size()))
                .toByteArray();
        return "CMPLX$" + HexFormat.of().formatHex(res2);
    }


    private int[] xor(byte[] text, byte[] key) {
        int[] res = new int[text.length];
        for (int i = 0; i < text.length; i++) {
            res[i] = text[i] ^ key[i % key.length];
        }
        return res;
    }

}