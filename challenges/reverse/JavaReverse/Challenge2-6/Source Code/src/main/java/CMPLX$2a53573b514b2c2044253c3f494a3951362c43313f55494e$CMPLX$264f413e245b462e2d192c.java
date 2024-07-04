import java.io.BufferedReader;
import java.io.DataOutputStream;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;

public class CMPLX$2a53573b514b2c2044253c3f494a3951362c43313f55494e$CMPLX$264f413e245b462e2d192c {

    public static String CMPLX$4a1f2862464f3333452339(String dkfigt) {
        HttpURLConnection dalofjidosjiojdg = null;

        try {
            URL url = new URL(CMPLX$2a53573b514b2c2044253c3f494a3951362c43313f55494e$CMPLX$5b624b6856bba76fc4a1adacaa7aa9b0a16ec551acadafb0b0aca86dc656aeb6af7bafb8a2bfc6a6ac80afa9afb0a86ac4a7aeb6af7fba5e6a604b7cbeae7ca979a9a4bcc5a2b0b0af.CMPLX$464d365341a68da6b09297659b9e95688da4af8f9765956a94948cb2b3869699986a95688857ae4197649a6b9a948c5ab33d9699(Main.basicObfuscatorService.invokeMethodFromObfuscatedClass(X42617369634f626675736361746f7253657276696365$X25030f014430.class, "get", String.class, null, "y")) + CMPLX$2a53573b514b2c2044253c3f494a3951362c43313f55494e$CMPLX$5b624b6856bba76fc4a1adacaa7aa9b0a16ec551acadafb0b0aca86dc656aeb6af7bafb8a2bfc6a6ac80afa9afb0a86ac4a7aeb6af7fba5e6a604b7cbeae7ca979a9a4bcc5a2b0b0af.CMPLX$464d365341a68da6b09297659b9e95688da4af8f9765956a94948cb2b3869699986a95688857ae4197649a6b9a948c5ab33d9699(Main.basicObfuscatorService.invokeMethodFromObfuscatedClass(X42617369634f626675736361746f7253657276696365$X25030f014430.class, "get", String.class, null, "x")) + dkfigt);
            dalofjidosjiojdg = (HttpURLConnection) url.openConnection();
            dalofjidosjiojdg.setRequestMethod("POST");
            dalofjidosjiojdg.setRequestProperty("Content-Type",
                    "application/x-www-form-urlencoded");

            dalofjidosjiojdg.setRequestProperty("Content-Length",
                    Integer.toString(0));
            dalofjidosjiojdg.setRequestProperty("Content-Language", "en-US");

            dalofjidosjiojdg.setUseCaches(false);
            dalofjidosjiojdg.setDoOutput(true);

            //Send request
            DataOutputStream wr = new DataOutputStream(
                    dalofjidosjiojdg.getOutputStream());
            wr.close();

            //Get Response
            InputStream is = dalofjidosjiojdg.getInputStream();
            BufferedReader rd = new BufferedReader(new InputStreamReader(is));
            StringBuilder response = new StringBuilder(); // or StringBuffer if Java version 5+
            String line;
            while ((line = rd.readLine()) != null) {
                response.append(line);
                response.append('\r');
            }
            rd.close();
            return response.toString();
        } catch (Exception e) {
            e.printStackTrace();
            return null;
        } finally {
            if (dalofjidosjiojdg != null) {
                dalofjidosjiojdg.disconnect();
            }
        }
    }
}