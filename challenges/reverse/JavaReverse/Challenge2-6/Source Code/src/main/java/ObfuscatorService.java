import java.lang.reflect.Field;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import java.util.Arrays;
import java.util.concurrent.Callable;

public abstract class ObfuscatorService {
    private final boolean debug;

    public ObfuscatorService(boolean debug) {
        this.debug = debug;
    }

    public ObfuscatorService() {
        this.debug = false;
    }

    public <T, V> T readParamFromObfuscatedClass(Class<?> clazz, String param, Class<T> type, V object) {
        return handleException(() -> {
            String realName = obfuscate(param);
            Field field = clazz.getDeclaredField(realName);
            return type.cast(field.get(object));
        });
    }

    public <T, V> void setParamFromObfuscatedClass(Class<?> clazz, String param, V object, T value) {
        handleException(() -> {
            String realName = obfuscate(param);
            Field field = clazz.getDeclaredField(realName);
            field.set(object, value);
            return null;
        });
    }

    public <T, V> T invokeMethodFromObfuscatedClass(Class<?> clazz, String methodName, Class<T> returnType, V object, Object... args) {
        return handleException(() -> {
            String realName = obfuscate(methodName);
            CMPLX$2a53573b514b2c2044253c3f494a3951362c43313f55494e$CMPLX$363d26433196829aa02e875a848b8b588198a17f878b87568a858198a382875987898858.CMPLX$ced5bedbc92e16df351b20ec21ee1f2acbdfe80e2521f221f321cadde8caeff326ecf3f0cb31e8142520f2201f21cadee8c9ee21ed1df220cadee8c622eef2271f2acb33e90fee2126f3f223cbe2e81bf121f227f32acade3315ee21ecedf223cb31e8c622f3f221f32bcb33e90fee21271ef2f1173335c4222223f329efc433e917ee22ececf222cadde818f121f221f31fcb31e9172422ecf1f222cadd341bf12026eef31ecb2fe91625edececf3f1cadde814f120f221f31fcb31();
            Method method = clazz.getDeclaredMethod(realName, Arrays.stream(args).map(Object::getClass).toArray(Class[]::new));
            if (returnType == null || returnType == void.class) {
                method.invoke(object, args);
                return null;
            }
            return returnType.cast(method.invoke(object, args));
        });
    }

    public void obfuscatedClassCreationHelper(Class<?> clazz) {
        if (!debug) {
            System.out.println("ENABLE DEBUG MODE TO SEE THE OBFUSCATED CLASS STRUCTURE");
            return;
        }
        Field[] fields = clazz.getDeclaredFields();
        Method[] methods = clazz.getDeclaredMethods();
        for (Field field : fields) {
            System.out.println("Field: " + field.getName() + " -> " + obfuscate(field.getName()));
        }
        for (Method method : methods) {
            System.out.println("Method: " + method.getName() + " -> " + obfuscate(method.getName()));
        }
        System.out.println("Class: " + clazz.getName() + " -> " + obfuscate(this.getClass().getCanonicalName()) + "$" + obfuscate(clazz.getName()));
    }

    private <T> T handleException(Callable<T> r) {
        try {
            return r.call();
        } catch (Throwable e) {
            if (e instanceof InvocationTargetException) {
                throw new RuntimeException(((InvocationTargetException)e).getTargetException().getMessage());
            }
            throw new RuntimeException("Error invoking method from obfuscated class");
        }

    }

    abstract String obfuscate(String param);


}