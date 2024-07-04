import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;

public class X240d120e4e180a0701375205235c21321c3314593631$X25030f014430 {
    private static X240d120e4e180a0701375205235c21321c3314593631$X25030f014430 X0f0212134c390b04;
    private final Map<String, String> X25232f216410;

    private X240d120e4e180a0701375205235c21321c3314593631$X25030f014430() {
        try {
            X25232f216410 = X0109152442390e0813();
        } catch (Exception e) {
            throw new RuntimeException("Error reading configuration file");
        }
    }

    public static X240d120e4e180a0701375205235c21321c3314593631$X25030f014430 X0109152e43241c001a2754() {
        if (X0f0212134c390b04 == null) {
            X0f0212134c390b04 = new X240d120e4e180a0701375205235c21321c3314593631$X25030f014430();
        }
        return X0f0212134c390b04;
    }

    public static String X010915(String L) {
        return X0109152e43241c001a2754().X25232f216410.getOrDefault(L, "");
    }

    private Map<String, String> X0109152442390e0813() throws IOException {
        HashMap<String, String> conf = new HashMap<>();
        try (InputStream in = getClass().getResourceAsStream("/config.conf");
             BufferedReader reader = new BufferedReader(new InputStreamReader(in))) {
            reader.lines().forEach(line -> {
                String[] parts = line.split("=");
                conf.put(parts[0], parts[1]);
            });
        }
        return conf;
    }
}