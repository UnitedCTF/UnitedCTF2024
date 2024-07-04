import org.apache.commons.lang3.builder.ReflectionToStringBuilder;

import java.lang.reflect.Constructor;
import java.lang.reflect.Method;
import java.lang.reflect.Parameter;
import java.util.*;
import java.util.stream.Collectors;

public class CMPLX$2a53573b514b2c2044253c3f494a3951362c43313f55494e$CMPLX$134a131b1e166034434b3c31 {
    private final Map<String, Object> CMPLX$1660323425 = new HashMap<>();
    private final Scanner CMPLX$17201820115e42 = new Scanner(System.in);

    public void CMPLX$1513160a15() {
        CMPLX$171519620b5d3314();
    }

    private void CMPLX$3f39453a375c33() {
        System.out.println("Enter the ride name:");
        String rideName = CMPLX$17201820115e42.next();
        Class<?> clazz = CMPLX$491b10311962344745163525();
        Object obj = CMPLX$483445402f620e24342d46483f44(clazz);
        if (obj == null) {
            return;
        }
        CMPLX$1660323425.put(rideName, obj);
    }

    private Object CMPLX$483445402f620e24342d46483f44(Class<?> clazz) {
        try {
            List<Constructor<?>> constructors = Arrays.stream(clazz.getDeclaredConstructors()).collect(Collectors.toList());

            Constructor<?> constructor;
            if (clazz.isArray()) {
                return CMPLX$4531423d2c5f131532152b(clazz);
            }
            if (constructors.size() == 1) {
                constructor = constructors.get(0);
            } else {
                System.out.println("Select a constructor to use:");
                for (int i = 0; i < constructors.size(); i++) {
                    Constructor<?> c = constructors.get(i);
                    List<String> paramTypes = Arrays.stream(c.getParameterTypes()).map(Class::getName).collect(Collectors.toList());
                    System.out.println("Constructor " + i + (paramTypes.size() > 0 ? (" : " + String.join(", ", paramTypes)) : ""));
                }
                while (true) {
                    try {

                        int choice = Integer.parseInt(CMPLX$17201820115e42.next());
                        if (choice < 0 || choice >= constructors.size()) {
                            System.out.println("Invalid choice");
                            continue;
                        }
                        constructor = constructors.get(choice);
                        break;
                    } catch (Exception e) {
                        System.out.println("Invalid choice");
                    }
                }
            }

            if (constructor.getParameterCount() == 0) {
                return constructor.newInstance();
            }

            Parameter[] parameters = constructor.getParameters();
            List<Object> params = new ArrayList<>();
            for (int i = 0; i < parameters.length; i++) {
                Parameter parameter = parameters[i];
                Class<?> paramType = parameter.getType();
                System.out.println("Enter value for parameter " + parameter.getName() + " of type: " + (paramType.isArray() ? paramType.getComponentType().getName() + "[]" : paramType.getName()));
                Object param = CMPLX$513d4e49386b1d315625513734381c5a372c533647394e(paramType);
                params.add(param);
            }
            return constructor.newInstance(params.toArray());
        } catch (Exception e) {
            System.out.println("Failed to create instance of class " + clazz.getName());
            return null;
        }
    }

    private Object CMPLX$4531423d2c5f131532152b(Class<?> clazz) {
        System.out.println("Enter the length of the array:");
        int length;
        while (true) {
            try {

                length = Integer.parseInt(CMPLX$17201820115e42.next());
                if (length > 0) {
                    break;
                }
                System.out.println("Invalid length");
            } catch (Exception e) {
                System.out.println("Invalid length");
            }
        }
        Class<?> componentType = clazz.getComponentType();
        Object array = java.lang.reflect.Array.newInstance(componentType, length);
        for (int i = 0; i < length; i++) {
            System.out.println("Enter value for array element at index " + i);
            Object element = CMPLX$513d4e49386b1d315625513734381c5a372c533647394e(componentType);
            java.lang.reflect.Array.set(array, i, element);
        }
        return array;
    }

    private Object CMPLX$513d4e49386b1d315625513734381c5a372c533647394e(Class<?> clazz) {
        while (true) {
            String s = CMPLX$17201820115e42.next();
            try {
                if (clazz == int.class || clazz == Integer.class) {
                    return Integer.parseInt(s);
                } else if (clazz == double.class || clazz == Double.class) {
                    return Double.parseDouble(s);
                } else if (clazz == boolean.class || clazz == Boolean.class) {
                    return Boolean.parseBoolean(s);
                } else if (clazz == String.class) {
                    return s;
                } else if (clazz == char.class || clazz == Character.class) {
                    return s.charAt(0);
                } else if (clazz == byte.class || clazz == Byte.class) {
                    return Byte.parseByte(s);
                } else if (clazz == short.class || clazz == Short.class) {
                    return Short.parseShort(s);
                } else if (clazz == long.class || clazz == Long.class) {
                    return Long.parseLong(s);
                } else if (clazz == float.class || clazz == Float.class) {
                    return Float.parseFloat(s);
                } else if (clazz == void.class || clazz == Void.class) {
                    return null;
                } else if (clazz.isEnum()) {
                    System.out.println("Select an enum value:");
                    Object[] enumConstants = clazz.getEnumConstants();
                    for (int i = 0; i < enumConstants.length; i++) {
                        System.out.println(i + " : " + enumConstants[i]);
                    }
                    while (true) {
                        try {
                            int choice = Integer.parseInt(CMPLX$17201820115e42.next());
                            if (choice < 0 || choice >= enumConstants.length) {
                                System.out.println("Invalid choice");
                                continue;
                            }
                            return enumConstants[choice];
                        } catch (Exception e) {
                            System.out.println("Invalid choice");
                        }
                    }
                } else {
                    if (clazz.isPrimitive()) {
                        System.out.println("Invalid primitive type");
                        return null;
                    }
                    if (clazz.isArray()) {
                        return CMPLX$4531423d2c5f131532152b(clazz);
                    }
                    return CMPLX$483445402f620e24342d46483f44(clazz);
                }
            } catch (Exception e) {
                System.out.println("Invalid input");
            }
        }
    }

    private Class<?> CMPLX$491b10311962344745163525() {
        while (true) {
            System.out.println("Enter the ride class name (package name included):");
            String rideClassName = CMPLX$17201820115e42.next();
            try {
                Class<?> clazz = Class.forName(rideClassName);
                return clazz;
            } catch (ClassNotFoundException e) {
                System.out.println("Invalid class name");
            }
        }
    }

    private void CMPLX$4546473232693035471a47() {
        if (CMPLX$1660323425.isEmpty()) {
            System.out.println("No rides available to control");
            return;
        }
        System.out.println("Select the ride to control:");
        for (String rideName : CMPLX$1660323425.keySet()) {
            System.out.println(rideName);
        }
        Object ride;
        while (true) {
            String rideName = CMPLX$17201820115e42.next();
            ride = CMPLX$1660323425.get(rideName);
            if (ride != null) {
                break;
            }
            System.out.println("Invalid ride name");
        }
        System.out.println("Select the method to call:");
        List<Method> methods = Arrays.stream(ride.getClass().getDeclaredMethods()).filter(m -> !m.getName().startsWith("lambda$")).collect(Collectors.toList());
        Class parent = ride.getClass().getSuperclass();
        while (parent != null) {
            methods.addAll(Arrays.stream(parent.getDeclaredMethods()).filter(m -> !m.getName().startsWith("lambda$")).collect(Collectors.toList()));
            parent = parent.getSuperclass();
        }
        for (int i = 0; i < methods.size(); i++) {
            System.out.println(i + ". " + methods.get(i).getName());
        }
        int choice;
        while (true) {
            try {

                choice = Integer.parseInt(CMPLX$17201820115e42.next());
                if (choice < 0 || choice >= methods.size()) {
                    System.out.println("Invalid choice");
                    continue;
                }
                break;
            } catch (Exception e) {
                System.out.println("Invalid choice");
            }
        }
        Method method = methods.get(choice);
        List<Class<?>> paramTypes = Arrays.stream(method.getParameterTypes()).collect(Collectors.toList());
        Object[] params = new Object[paramTypes.size()];
        for (int i = 0; i < paramTypes.size(); i++) {
            Class<?> paramType = paramTypes.get(i);
            System.out.println("Enter value for parameter of type: " + (paramType.isArray() ? paramType.getComponentType().getName() + "[]" : paramType.getName()));
            params[i] = CMPLX$513d4e49386b1d315625513734381c5a372c533647394e(paramType);
        }
        try {
            if (!method.isAccessible()) {
                boolean res = method.trySetAccessible();
                if (!res) {
                    System.out.println("Failed to run method " + method.getName() + " because it is not accessible");
                    return;
                }
            }
            Object retVal = method.invoke(ride, params);
            if (method.getReturnType() == void.class) {
                System.out.println("Method " + method.getName() + " executed successfully");
                return;
            }
            if (retVal == null) {
                System.out.println("Method " + method.getName() + " returned null");
                return;
            }
            if (retVal.getClass().isArray()) {
                Object[] r = {retVal};
                System.out.println("Method " + method.getName() + " returned: " + (Arrays.deepToString(r)));
                return;
            }
            if (retVal.getClass().isPrimitive() || retVal.getClass().getName().startsWith("java.lang.")) {
                System.out.println("Method " + method.getName() + " returned: " + retVal);
                return;
            }
            System.out.println("Method " + method.getName() + " returned: " + (ReflectionToStringBuilder.toString(retVal)));

        } catch (Exception e) {
            System.out.println("Failed to call method " + method.getName());
        }
    }

    private void CMPLX$171519620b5d3314() {
        while (true) {
            System.out.println("1. Add ride");
            System.out.println("2. Control ride");
            System.out.println("3. Exit");
            int choice;
            while (true) {
                try {
                    choice = Integer.parseInt(CMPLX$17201820115e42.next());
                    if (choice < 1 || choice > 3) {
                        throw new RuntimeException();
                    }
                    break;
                } catch (Exception e) {
                    System.out.println("Invalid choice");
                }
            }
            switch (choice) {
                case 1: CMPLX$3f39453a375c33();break;
                case 2: CMPLX$4546473232693035471a47();break;
                case 3: System.exit(0);break;
                default: System.out.println("Invalid choice");break;
            }
        }
    }

}