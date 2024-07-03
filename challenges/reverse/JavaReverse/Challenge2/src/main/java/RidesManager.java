import java.util.HashMap;
import java.util.Map;

public class RidesManager {
    private final Map<String, Object> rides = new HashMap<>();

    private void showMenu() {
        System.out.println("1. Add ride");
        System.out.println("2. Show rides");
        System.out.println("3. Exit");
    }

}