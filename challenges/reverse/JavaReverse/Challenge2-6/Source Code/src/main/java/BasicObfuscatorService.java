import org.apache.commons.codec.binary.Hex;

@Deprecated
public class BasicObfuscatorService extends ObfuscatorService {

    private static final byte[] XOR_KEY = getXORKey();

    private static byte[] getXORKey() {
        return new byte[]{102, 108, 97, 103, 45, 87, 104, 97, 116, 68, 49, 100, 87, 51, 83, 97, 121, 65, 98, 48, 85, 84, 83, 101, 99, 114, 51, 84, 115, 63};
    }

    protected String obfuscate(String text) {
        byte[] textBytes = text.getBytes();
        byte[] obfuscatedBytes = new byte[textBytes.length];
        for (int i = 0; i < textBytes.length; i++) {
            obfuscatedBytes[i] = (byte) (textBytes[i] ^ XOR_KEY[i % XOR_KEY.length]);
        }
        return "X" + new String(Hex.encodeHex(obfuscatedBytes));
    }
}