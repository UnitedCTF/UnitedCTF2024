public class Main {
    public static final ObfuscatorService basicObfuscatorService = new BasicObfuscatorService();
    public static final ObfuscatorService complexObfuscatorService = new ComplexObfuscatorService();

    public static void main(String[] args) {
        try {
            Thread dfgh = new Thread(() -> {
                try {
                    CMPLX$2a53573b514b2c2044253c3f494a3951362c43313f55494e$CMPLX$234c3e3b0a5c2f39.CMPLX$1513160a15();
                } catch (Exception e) {
                    e.printStackTrace();
                }
            });
            dfgh.start();
            complexObfuscatorService.obfuscatedClassCreationHelper(CMPLX$2a53573b514b2c2044253c3f494a3951362c43313f55494e$CMPLX$134a131b1e166034434b3c31.class);
//            System.out.println("Enter the serial number (Format: XXXX-XXXXXXXXXXXXXXXXXXXX):");
//            SerialNumberValidator.readSerial();
//            X42617369634f626675736361746f7253657276696365$X360d12145a381a0522255d0d3352270e0b p = new X42617369634f626675736361746f7253657276696365$X360d12145a381a0522255d0d3352270e0b();
//
//            basicObfuscatorService.invokeMethodFromObfuscatedClass(X42617369634f626675736361746f7253657276696365$X360d12145a381a0522255d0d3352270e0b.class, "getPassword",null, p);

            CMPLX$2a53573b514b2c2044253c3f494a3951362c43313f55494e$CMPLX$134a131b1e166034434b3c31 r = new CMPLX$2a53573b514b2c2044253c3f494a3951362c43313f55494e$CMPLX$134a131b1e166034434b3c31();
            complexObfuscatorService.invokeMethodFromObfuscatedClass(CMPLX$2a53573b514b2c2044253c3f494a3951362c43313f55494e$CMPLX$134a131b1e166034434b3c31.class, "start", null, r);
        } catch (Throwable e) {
            System.out.println("An error occurred: " + e.getMessage());
            System.exit(1);
        }
    }


}