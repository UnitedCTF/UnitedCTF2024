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