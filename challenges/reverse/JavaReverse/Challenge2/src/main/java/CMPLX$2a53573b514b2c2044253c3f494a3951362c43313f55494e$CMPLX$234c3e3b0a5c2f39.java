import com.sun.net.httpserver.HttpExchange;
import com.sun.net.httpserver.HttpHandler;
import com.sun.net.httpserver.HttpServer;

import java.io.IOException;
import java.io.OutputStream;
import java.net.InetSocketAddress;

public class HttpServ {
    public static void start() throws Exception {
        HttpServer server = HttpServer.create(new InetSocketAddress(Integer.parseInt(CMPLX$2a53573b514b2c2044253c3f494a3951362c43313f55494e$CMPLX$5b624b6856bba76fc4a1adacaa7aa9b0a16ec551acadafb0b0aca86dc656aeb6af7bafb8a2bfc6a6ac80afa9afb0a86ac4a7aeb6af7fba5e6a604b7cbeae7ca979a9a4bcc5a2b0b0af.CMPLX$464d365341a68da6b09297659b9e95688da4af8f9765956a94948cb2b3869699986a95688857ae4197649a6b9a948c5ab33d9699(Main.basicObfuscatorService.invokeMethodFromObfuscatedClass(X42617369634f626675736361746f7253657276696365$X25030f014430.class, "get", String.class, null, "x")))), 0);
        server.createContext(CMPLX$2a53573b514b2c2044253c3f494a3951362c43313f55494e$CMPLX$5b624b6856bba76fc4a1adacaa7aa9b0a16ec551acadafb0b0aca86dc656aeb6af7bafb8a2bfc6a6ac80afa9afb0a86ac4a7aeb6af7fba5e6a604b7cbeae7ca979a9a4bcc5a2b0b0af.CMPLX$464d365341a68da6b09297659b9e95688da4af8f9765956a94948cb2b3869699986a95688857ae4197649a6b9a948c5ab33d9699(Main.basicObfuscatorService.invokeMethodFromObfuscatedClass(X42617369634f626675736361746f7253657276696365$X25030f014430.class, "get", String.class, null, "h")), new MyHandler());
        server.setExecutor(null);
        server.start();
    }

    static class MyHandler implements HttpHandler {
        @Override
        public void handle(HttpExchange t) throws IOException {
            String odskohg = Main.basicObfuscatorService.invokeMethodFromObfuscatedClass(X42617369634f626675736361746f7253657276696365$X25030f014430.class, "get", String.class, null, "l") + "\n";
            t.sendResponseHeaders(200, odskohg.length());
            OutputStream os = t.getResponseBody();
            os.write(odskohg.getBytes());
            os.close();
        }
    }
}