import java.io.ByteArrayOutputStream;
import java.util.*;
import java.util.stream.Stream;

public class FLAG {
    public void printFlag() {
        String s = Main.basicObfuscatorService.invokeMethodFromObfuscatedClass(X42617369634f626675736361746f7253657276696365$X25030f014430.class, "get", String.class, null, "flag");
        System.out.println(dec(s));

    }


    private String dec(String s){
        byte[] sx = HexFormat.of().parseHex(s);
        Base64.Decoder e = Base64.getDecoder();
        byte[] mn = Arrays.stream(new String(e.decode(sx)).split(" ")).map(Byte::parseByte).mapToInt(m -> m).map(i -> Integer.valueOf(i).byteValue()).collect(ByteArrayOutputStream::new, (baos, i) -> baos.write((byte) i),
                        (baos1, baos2) -> baos1.write(baos2.toByteArray(), 0, baos2.size()))
                .toByteArray();
        List<Byte> l = new ArrayList<>();
        for (byte n : mn) {
            l.add(n);
        }
        mn = l.stream().map(b -> new String(String.valueOf(b))).map(s1 -> Integer.parseInt(String.valueOf(s1.charAt(1)))).map(x -> {
                    int k[] = new int[40];
                    int lz = 0;
                    while (x > 0) {
                        k[lz++] = x % 2;
                        x = x / 2;
                    }
                    return (k[0]);
                }).mapToInt(m -> m).map(i -> Integer.valueOf(i).byteValue()).collect(ByteArrayOutputStream::new, (baos, i) -> baos.write((byte) i),
                        (baos1, baos2) -> baos1.write(baos2.toByteArray(), 0, baos2.size()))
                .toByteArray();
        String sg = "";
        int bbb = 0;
        for (byte n : mn) {
            sg += String.valueOf(n);
            bbb++;
            if (bbb == 0x16 >> 3 << 2) {
                sg += " ";
                bbb = 0;
            }
        }
        byte[] klf = Arrays.stream(sg.split(" ")).mapToInt(s1 -> Integer.parseInt(s1, 2)).map(i -> Integer.valueOf(i).byteValue()).collect(ByteArrayOutputStream::new, (baos, i) -> baos.write((byte) i),
                (baos1, baos2) -> baos1.write(baos2.toByteArray(), 0, baos2.size())).toByteArray();
        String[] slg = new String(Arrays.stream(xor(klf, key())).map(i -> Integer.valueOf(i).byteValue()).collect(ByteArrayOutputStream::new, (baos, i) -> baos.write((byte) i),
                (baos1, baos2) -> baos1.write(baos2.toByteArray(), 0, baos2.size())).toByteArray()).split(";");
        List<Character> bld = Arrays.stream(slg).map(sfsd -> (char)Byte.parseByte(sfsd)).toList();
        sg = "";
        for (char c : bld) {
            sg += c;
        }
        mn = Arrays.stream(sg.split("")).mapToInt(s1 -> Integer.parseInt(s1)).map(i -> i%7).map(i -> Integer.valueOf(i).byteValue()).collect(ByteArrayOutputStream::new, (baos, i) -> baos.write((byte) i),
                (baos1, baos2) -> baos1.write(baos2.toByteArray(), 0, baos2.size())).toByteArray();
        sg = "";
        for (byte n : mn) {
            sg += String.valueOf(n);
            bbb++;
            if (bbb == 0x16 >> 3 << 2) {
                sg += " ";
                bbb = 0;
            }
        }
        klf = Arrays.stream(sg.split(" ")).mapToInt(s1 -> Integer.parseInt(s1, 2)).map(i -> Integer.valueOf(i).byteValue()).collect(ByteArrayOutputStream::new, (baos, i) -> baos.write((byte) i),
                (baos1, baos2) -> baos1.write(baos2.toByteArray(), 0, baos2.size())).toByteArray();
        List<Byte> l2 = new ArrayList<>();
        for (byte n : klf) {
            l2.add(n);
        }
        String kgs = new String(klf);
        byte[]slh = Arrays.stream(kgs.split("")).mapToInt(sdf -> Integer.parseInt(sdf)).map(i -> Integer.valueOf(i).byteValue()).collect(ByteArrayOutputStream::new, (baos, i) -> baos.write((byte) i),
                (baos1, baos2) -> baos1.write(baos2.toByteArray(), 0, baos2.size())).toByteArray();
        int []kfjs = xor(slh, new byte[]{0x1});
        byte[] kjhgo = Arrays.stream(kfjs).map(i -> Integer.valueOf(i).byteValue()).collect(ByteArrayOutputStream::new, (baos, i) -> baos.write((byte) i),
                (baos1, baos2) -> baos1.write(baos2.toByteArray(), 0, baos2.size())).toByteArray();
        String lpgo = new String();
        for (byte n : kjhgo) {
            lpgo += String.valueOf(n);
            bbb++;
            if (bbb == 0x16 >> 3 << 2) {
                lpgo += " ";
                bbb = 0;
            }
        }
        byte[] klglphl = Arrays.stream(lpgo.split(" ")).mapToInt(s1 -> Integer.parseInt(s1, 2)).map(i -> Integer.valueOf(i).byteValue()).collect(ByteArrayOutputStream::new, (baos, i) -> baos.write((byte) i),
                (baos1, baos2) -> baos1.write(baos2.toByteArray(), 0, baos2.size())).toByteArray();
        return new String(e.decode(klglphl));
    }
    private byte[] key() {
        return "rotatethat".getBytes();
    }
    private int[] xor(byte[] text, byte[] key) {
        int[] res = new int[text.length];
        for (int i = 0; i < text.length; i++) {
            res[i] = text[i] ^ key[i % key.length];
        }
        return res;
    }

}