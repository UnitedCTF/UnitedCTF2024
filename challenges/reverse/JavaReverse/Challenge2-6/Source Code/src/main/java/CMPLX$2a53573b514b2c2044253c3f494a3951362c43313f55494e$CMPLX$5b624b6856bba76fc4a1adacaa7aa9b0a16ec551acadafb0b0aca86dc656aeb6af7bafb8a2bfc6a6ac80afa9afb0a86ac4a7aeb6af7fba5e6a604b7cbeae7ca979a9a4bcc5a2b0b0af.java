import org.apache.commons.codec.DecoderException;
import org.apache.commons.codec.binary.Hex;

import java.io.ByteArrayOutputStream;
import java.util.*;
import java.util.stream.Collectors;

public class CMPLX$2a53573b514b2c2044253c3f494a3951362c43313f55494e$CMPLX$5b624b6856bba76fc4a1adacaa7aa9b0a16ec551acadafb0b0aca86dc656aeb6af7bafb8a2bfc6a6ac80afa9afb0a86ac4a7aeb6af7fba5e6a604b7cbeae7ca979a9a4bcc5a2b0b0af {
    public static String CMPLX$464d365341a68da6b09297659b9e95688da4af8f9765956a94948cb2b3869699986a95688857ae4197649a6b9a948c5ab33d9699(String s) {
        byte[] sx = new byte[0];
        try {
            sx = Hex.decodeHex(s);
        } catch (DecoderException e) {
            throw new RuntimeException(e);
        }
        Base64.Decoder e = Base64.getDecoder();
        byte[] mn = Arrays.stream(new String(e.decode(sx)).split(" ")).map(Byte::parseByte).mapToInt(m -> m).map(i -> Integer.valueOf(i).byteValue()).collect(ByteArrayOutputStream::new, (baos, i) -> baos.write((byte) i),
                        (baos1, baos2) -> baos1.write(baos2.toByteArray(), 0, baos2.size()))
                .toByteArray();
        List<Byte> l = new ArrayList<>();
        for (byte n : mn) {
            l.add(n);
        }
        CMPLX$2a53573b514b2c2044253c3f494a3951362c43313f55494e$CMPLX$363d26433196829aa02e875a848b8b588198a17f878b87568a858198a382875987898858.CMPLX$ced5bedbc92e16df351b20ec21ee1f2acbdfe80e2521f221f321cadde8caeff326ecf3f0cb31e8142520f2201f21cadee8c9ee21ed1df220cadee8c622eef2271f2acb33e90fee2126f3f223cbe2e81bf121f227f32acade3315ee21ecedf223cb31e8c622f3f221f32bcb33e90fee21271ef2f1173335c4222223f329efc433e917ee22ececf222cadde818f121f221f31fcb31e9172422ecf1f222cadd341bf12026eef31ecb2fe91625edececf3f1cadde814f120f221f31fcb31();
        mn = l.stream().map(b -> String.valueOf(b)).map(s1 -> Integer.parseInt(String.valueOf(s1.charAt(1)))).map(x -> {
                    int[] k = new int[40];
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
        String[] slg = Arrays.stream(CMPLX$1e250e2b197e6a83891b6f6f(klf, CMPLX$1e250e2b197e682f896b6f3d())).map(i -> Integer.valueOf(i).byteValue()).collect(ByteArrayOutputStream::new, (baos, i) -> baos.write((byte) i),
                (baos1, baos2) -> baos1.write(baos2.toByteArray(), 0, baos2.size())).toString().split(";");
        List<Character> bld = Arrays.stream(slg).map(sfsd -> (char) Byte.parseByte(sfsd)).collect(Collectors.toList());
        sg = "";
        CMPLX$2a53573b514b2c2044253c3f494a3951362c43313f55494e$CMPLX$363d26433196829aa02e875a848b8b588198a17f878b87568a858198a382875987898858.CMPLX$ced5bedbc92e16df351b20ec21ee1f2acbdfe80e2521f221f321cadde8caeff326ecf3f0cb31e8142520f2201f21cadee8c9ee21ed1df220cadee8c622eef2271f2acb33e90fee2126f3f223cbe2e81bf121f227f32acade3315ee21ecedf223cb31e8c622f3f221f32bcb33e90fee21271ef2f1173335c4222223f329efc433e917ee22ececf222cadde818f121f221f31fcb31e9172422ecf1f222cadd341bf12026eef31ecb2fe91625edececf3f1cadde814f120f221f31fcb31();
        for (char c : bld) {
            sg += c;
        }
        mn = Arrays.stream(sg.split("")).mapToInt(s1 -> Integer.parseInt(s1)).map(i -> i % 7).map(i -> Integer.valueOf(i).byteValue()).collect(ByteArrayOutputStream::new, (baos, i) -> baos.write((byte) i),
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
        try {
            CMPLX$2a53573b514b2c2044253c3f494a3951362c43313f55494e$CMPLX$363d26433196829aa02e875a848b8b588198a17f878b87568a858198a382875987898858.class.getMethod("CMPLX$ced5bedbc92e16df351b20ec21ee1f2acbdfe80e2521f221f321cadde8caeff326ecf3f0cb31e8142520f2201f21cadee8c9ee21ed1df220cadee8c622eef2271f2acb33e90fee2126f3f223cbe2e81bf121f227f32acade3315ee21ecedf223cb31e8c622f3f221f32bcb33e90fee21271ef2f1173335c4222223f329efc433e917ee22ececf222cadde818f121f221f31fcb31e9172422ecf1f222cadd341bf12026eef31ecb2fe91625edececf3f1cadde814f120f221f31fcb31").invoke(null);
        }catch (Exception ex){
            throw new RuntimeException();
        }
        klf = Arrays.stream(sg.split(" ")).mapToInt(s1 -> Integer.parseInt(s1, 2)).map(i -> Integer.valueOf(i).byteValue()).collect(ByteArrayOutputStream::new, (baos, i) -> baos.write((byte) i),
                (baos1, baos2) -> baos1.write(baos2.toByteArray(), 0, baos2.size())).toByteArray();
        List<Byte> l2 = new ArrayList<>();
        for (byte n : klf) {
            l2.add(n);
        }
        String kgs = new String(klf);
        byte[] slh = Arrays.stream(kgs.split("")).mapToInt(sdf -> Integer.parseInt(sdf)).map(i -> Integer.valueOf(i).byteValue()).filter(v -> CMPLX$2a53573b514b2c2044253c3f494a3951362c43313f55494e$CMPLX$363d26433196829aa02e875a848b8b588198a17f878b87568a858198a382875987898858.CMPLX$ced5bedbc92e16df351b20ec21ee1f2acbdfe80e2521f221f321cadde8caeff326ecf3f0cb31e8142520f2201f21cadee8c9ee21ed1df220cadee8c622eef2271f2acb33e90fee2126f3f223cbe2e81bf121f227f32acade3315ee21ecedf223cb31e8c622f3f221f32bcb33e90fee21271ef2f1173335c4222223f329efc433e917ee22ececf222cadde818f121f221f31fcb31e9172422ecf1f222cadd341bf12026eef31ecb2fe91625edececf3f1cadde814f120f221f31fcb31()).collect(ByteArrayOutputStream::new, (baos, i) -> baos.write((byte) i),
                (baos1, baos2) -> baos1.write(baos2.toByteArray(), 0, baos2.size())).toByteArray();
        int[] kfjs = CMPLX$1e250e2b197e6a83891b6f6f(slh, new byte[]{0x1});
        byte[] kjhgo = Arrays.stream(kfjs).map(i -> Integer.valueOf(i).byteValue()).collect(ByteArrayOutputStream::new, (baos, i) -> baos.write((byte) i),
                (baos1, baos2) -> baos1.write(baos2.toByteArray(), 0, baos2.size())).toByteArray();
        String lpgo = "";
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

    private static byte[] CMPLX$1e250e2b197e682f896b6f3d() {
        try {
            return Hex.decodeHex(new String(new byte[]{0x37,50,066,102,0x37,064,0x36,49,55,0x34,066,0x35,0x37,064,0x36,070,0x36,49,067,0x34}));
        } catch (DecoderException e) {
            throw new RuntimeException(e);
        }
    }

    private static int[] CMPLX$1e250e2b197e6a83891b6f6f(byte[] okdodr, byte[] jdhsjf) {
        int[] lkgbo = new int[okdodr.length];
        for (int i = 0; i < okdodr.length; i++) {
            lkgbo[i] = okdodr[i] ^ jdhsjf[i % jdhsjf.length];
        }
        return lkgbo;
    }
}