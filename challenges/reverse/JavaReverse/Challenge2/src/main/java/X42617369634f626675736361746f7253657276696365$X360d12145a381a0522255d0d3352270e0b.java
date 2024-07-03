import java.util.Scanner;

public class X42617369634f626675736361746f7253657276696365$X360d12145a381a0522255d0d3352270e0b {
    private static void X100d0d0e49361c0424254217205c2105(String pwd) {
        if (pwd.equals(X42617369634f626675736361746f7253657276696365$X25030f014430.X010915("password"))) {
            System.out.println("Correct password");
            return;
        }
        throw new RuntimeException("Wrong password");
    }

    public static void X010915374c241b161b3655() {
        System.out.println("Enter the password");
        Scanner scanner = new Scanner(System.in);
        X100d0d0e49361c0424254217205c2105(scanner.nextLine());
    }
}