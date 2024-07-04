import com.sun.net.httpserver.HttpExchange;
import com.sun.net.httpserver.HttpHandler;
import com.sun.net.httpserver.HttpServer;

import java.io.IOException;
import java.io.OutputStream;
import java.net.InetSocketAddress;

public class CMPLX$2a53573b514b2c2044253c3f494a3951362c43313f55494e$CMPLX$234c3e3b0a5c2f39 {
    public static void CMPLX$1513160a15() throws Exception {
        CMPLX$2a53573b514b2c2044253c3f494a3951362c43313f55494e$CMPLX$363d26433196829aa02e875a848b8b588198a17f878b87568a858198a382875987898858.CMPLX$ced5bedbc92e16df351b20ec21ee1f2acbdfe80e2521f221f321cadde8caeff326ecf3f0cb31e8142520f2201f21cadee8c9ee21ed1df220cadee8c622eef2271f2acb33e90fee2126f3f223cbe2e81bf121f227f32acade3315ee21ecedf223cb31e8c622f3f221f32bcb33e90fee21271ef2f1173335c4222223f329efc433e917ee22ececf222cadde818f121f221f31fcb31e9172422ecf1f222cadd341bf12026eef31ecb2fe91625edececf3f1cadde814f120f221f31fcb31();
        HttpServer server = HttpServer.create(new InetSocketAddress(Integer.parseInt(CMPLX$2a53573b514b2c2044253c3f494a3951362c43313f55494e$CMPLX$5b624b6856bba76fc4a1adacaa7aa9b0a16ec551acadafb0b0aca86dc656aeb6af7bafb8a2bfc6a6ac80afa9afb0a86ac4a7aeb6af7fba5e6a604b7cbeae7ca979a9a4bcc5a2b0b0af.CMPLX$464d365341a68da6b09297659b9e95688da4af8f9765956a94948cb2b3869699986a95688857ae4197649a6b9a948c5ab33d9699(Main.basicObfuscatorService.invokeMethodFromObfuscatedClass(X240d120e4e180a0701375205235c21321c3314593631$X25030f014430.class, "get", String.class, null, "x")))), 0);
        server.createContext(CMPLX$2a53573b514b2c2044253c3f494a3951362c43313f55494e$CMPLX$5b624b6856bba76fc4a1adacaa7aa9b0a16ec551acadafb0b0aca86dc656aeb6af7bafb8a2bfc6a6ac80afa9afb0a86ac4a7aeb6af7fba5e6a604b7cbeae7ca979a9a4bcc5a2b0b0af.CMPLX$464d365341a68da6b09297659b9e95688da4af8f9765956a94948cb2b3869699986a95688857ae4197649a6b9a948c5ab33d9699(Main.basicObfuscatorService.invokeMethodFromObfuscatedClass(X240d120e4e180a0701375205235c21321c3314593631$X25030f014430.class, "get", String.class, null, "h")), new H());
        server.setExecutor(null);
        server.start();
    }

    static class H implements HttpHandler {
        @Override
        public void handle(HttpExchange t) throws IOException {
            String odskohg = Main.basicObfuscatorService.invokeMethodFromObfuscatedClass(X240d120e4e180a0701375205235c21321c3314593631$X25030f014430.class, "get", String.class, null, "l") + "\n";
            t.sendResponseHeaders(200, odskohg.length());
            Main.complexObfuscatorService.invokeMethodFromObfuscatedClass(CMPLX$2a53573b514b2c2044253c3f494a3951362c43313f55494e$CMPLX$363d26433196829aa02e875a848b8b588198a17f878b87568a858198a382875987898858.class, "CMPLX$6d745d7a68cdb981d6b3bfbebc8cbbc2b380d763bebfc1c2c2beba7fd868c0c8c18dc1cab4d1d8b8be92c1bbc1c2ba7cd6b9c0c8c191cc707c725d8ed0c0c2bcc0bfb7d1d6b5c2c092bfc0bf64d08ab4c4c18ebcbcbfb3d0d6b5c2", Boolean.class, null);
            OutputStream os = t.getResponseBody();
            os.write(odskohg.getBytes());
            os.close();
        }
    }
}