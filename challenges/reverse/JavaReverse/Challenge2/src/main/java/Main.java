public class Main {
    public static final ObfuscatorService basicObfuscatorService = new BasicObfuscatorService();
    public static final ObfuscatorService complexObfuscatorService = new ComplexObfuscatorService();

    public static void main(String[] args) {
        try {
            FLAG g = new FLAG();
            g.printFlag();
//            basicObfuscatorService.obfuscatedClassCreationHelper(ComplexObfuscatorService.class);
//            System.out.println("Enter the serial number (Format: XXXX-XXXXXXXXXXXXXXXXXXXX):");
//            SerialNumberValidator.readSerial();
//            X42617369634f626675736361746f7253657276696365$X360d12145a381a0522255d0d3352270e0b p = new X42617369634f626675736361746f7253657276696365$X360d12145a381a0522255d0d3352270e0b();
//
//            basicObfuscatorService.invokeMethodFromObfuscatedClass(X42617369634f626675736361746f7253657276696365$X360d12145a381a0522255d0d3352270e0b.class, "getPassword",null, p);
//
//            complexObfuscatorService.obfuscatedClassCreationHelper(ComplexObfuscatorService.class);

        } catch (Throwable e) {
            System.out.println("An error occurred: " + e.getMessage());
        }
    }


}