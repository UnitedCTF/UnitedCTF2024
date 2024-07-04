import java.util.Scanner;

public class SerialNumberValidator {
    public final static String MASTER_SERIAL_NO = "flag-D0ntPuT5ecr3ts1nC0d3";

    public static void readSerial() {
        boolean valid = false;
        while (!valid) {
            Scanner scanner = new Scanner(System.in);
            String serialNumber = scanner.nextLine();
            if (!validateSerialNumberFormat(serialNumber)) {
                System.out.println("Invalid serial number format");
                continue;
            }
            valid = validateSerialNumber(serialNumber);
        }
    }


    private static boolean validateSerialNumber(String serialNumber) {
        if (serialNumber.equals(MASTER_SERIAL_NO)) {
            return true;
        }
        //  TODO: Implement the logic to validate the serial number
        System.out.println("Invalid serial number");
        return false;
    }

    private static boolean validateSerialNumberFormat(String serialNumber) {
        return serialNumber.matches("[0-9a-zA-Z]{4}-[0-9a-zA-Z]{20}");
    }
}