import java.lang.reflect.Field;
import java.util.HexFormat;

@Deprecated
//DEPRECATED: XOR key got leaked! Who thought it was a good idea to store the XOR key in the source code?
public class BasicObfuscatorService extends ObfuscatorService {

    private static final byte[] XOR_KEY = getXORKey();

    protected String obfuscate(String text) {
        byte[] textBytes = text.getBytes();
        byte[] obfuscatedBytes = new byte[textBytes.length];
        for (int i = 0; i < textBytes.length; i++) {
            obfuscatedBytes[i] = (byte) (textBytes[i] ^ XOR_KEY[i % XOR_KEY.length]);
        }
        return "X" + HexFormat.of().formatHex(obfuscatedBytes);
    }


    private static byte[] getXORKey() {
        return new byte[]{102, 108, 97, 103, 45, 87, 104, 97, 116, 68, 49, 100, 87, 51, 83, 97, 121, 65, 98, 48, 85, 84, 83, 101, 99, 114, 51, 84, 115, 63};
    }
}