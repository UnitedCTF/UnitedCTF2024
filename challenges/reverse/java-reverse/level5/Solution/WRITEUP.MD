# Ride Management System 5
## Write-up
### Solution (Français)
En analysant la classe `ObfuscatorService`, nous trouvons une méthode `obfuscatedClassCreationHelper()`. Nous pouvons voir que cette méthode prends une classe en paramètre et imprime les noms obfusqués pour toutes les fonctions, attributs ainsi que le nom de la classe. 

```java
 public void obfuscatedClassCreationHelper(Class<?> clazz) {
        if (!this.debug) {
            System.out.println("ENABLE DEBUG MODE TO SEE THE OBFUSCATED CLASS STRUCTURE");
        } else {
            Field[] fields = clazz.getDeclaredFields();
            Method[] methods = clazz.getDeclaredMethods();
            Field[] var4 = fields;
            int var5 = fields.length;

            PrintStream var10000;
            String var10001;
            int var6;
            for(var6 = 0; var6 < var5; ++var6) {
                Field field = var4[var6];
                var10000 = System.out;
                var10001 = field.getName();
                var10000.println("Field: " + var10001 + " -> " + this.obfuscate(field.getName()));
            }

            Method[] var8 = methods;
            var5 = methods.length;

            for(var6 = 0; var6 < var5; ++var6) {
                Method method = var8[var6];
                var10000 = System.out;
                var10001 = method.getName();
                var10000.println("Method: " + var10001 + " -> " + this.obfuscate(method.getName()));
            }

            var10000 = System.out;
            var10001 = clazz.getName();
            var10000.println("Class: " + var10001 + " -> " + this.obfuscate(this.getClass().getCanonicalName()) + "$" + this.obfuscate(clazz.getName()));
        }
    }
```
Si nous reprenons la méthode `obfuscate()` du `BasicObfuscatorService`:
```java
    protected String obfuscate(String text) {
        byte[] textBytes = text.getBytes();
        byte[] obfuscatedBytes = new byte[textBytes.length];
        for (int i = 0; i < textBytes.length; i++) {
            obfuscatedBytes[i] = (byte) (textBytes[i] ^ XOR_KEY[i % XOR_KEY.length]);
        }
        return "X" + new String(Hex.encodeHex(obfuscatedBytes));
    }
```
```java
    private static byte[] getXORKey() {
        return new byte[]{102, 108, 97, 103, 45, 87, 104, 97, 116, 68, 49, 100, 87, 51, 83, 97, 121, 65, 98, 48, 85, 84, 83, 101, 99, 114, 51, 84, 115, 63};
    }
```
Nous pouvons voir qu'une classe obfusquée avec le `BasicObfuscatorService` va donc etre nommée:

`X240d120e4e180a0701375205235c21321c3314593631` + `$` + `X` + `hex(className ^ flag-WhatD1dW3SayAb0UTSecr3Ts?)`

`X240d120e4e180a0701375205235c21321c3314593631` est le nom obfusqué de `BasicObfuscatorService`

Étant donnée que le XOR est une opération réversible, si nous prenons une classe obfusqué par le `BasicObfuscatorService`(classes qui commencent par `X240d120e4e180a0701375205235c21321c3314593631`), nous pouvons retrouver le nom original de la classe.

La classe `X240d120e4e180a0701375205235c21321c3314593631$X000000000000001823744408336a6314347509551a363510101107631a0f083e041148255d00162854` est une classe vide, ne contenant aucune information. Si nous essayons de prendre le nom de la classe obfusqué, donc : `000000000000001823744408336a6314347509551a363510101107631a0f083e041148255d00162854`, nous pouvons parser l'hexadécimal et faire un XOR avec `flag-WhatD1dW3SayAb0UTSecr3Ts?` pour retrouver `flag-WhyW0uldY0uM4keObfusc47i0nRever5able`
### Solution (English)

By analyzing the `ObfuscatorService` class, we find a method `obfuscatedClassCreationHelper()`. This method takes a class as a parameter and prints the obfuscated names of all the functions, attributes, and the class name.
```java
 public void obfuscatedClassCreationHelper(Class<?> clazz) {
        if (!this.debug) {
            System.out.println("ENABLE DEBUG MODE TO SEE THE OBFUSCATED CLASS STRUCTURE");
        } else {
            Field[] fields = clazz.getDeclaredFields();
            Method[] methods = clazz.getDeclaredMethods();
            Field[] var4 = fields;
            int var5 = fields.length;

            PrintStream var10000;
            String var10001;
            int var6;
            for(var6 = 0; var6 < var5; ++var6) {
                Field field = var4[var6];
                var10000 = System.out;
                var10001 = field.getName();
                var10000.println("Field: " + var10001 + " -> " + this.obfuscate(field.getName()));
            }

            Method[] var8 = methods;
            var5 = methods.length;

            for(var6 = 0; var6 < var5; ++var6) {
                Method method = var8[var6];
                var10000 = System.out;
                var10001 = method.getName();
                var10000.println("Method: " + var10001 + " -> " + this.obfuscate(method.getName()));
            }

            var10000 = System.out;
            var10001 = clazz.getName();
            var10000.println("Class: " + var10001 + " -> " + this.obfuscate(this.getClass().getCanonicalName()) + "$" + this.obfuscate(clazz.getName()));
        }
    }
```
If we look at the `obfuscate()` method from the `BasicObfuscatorService`:
```java
    protected String obfuscate(String text) {
        byte[] textBytes = text.getBytes();
        byte[] obfuscatedBytes = new byte[textBytes.length];
        for (int i = 0; i < textBytes.length; i++) {
            obfuscatedBytes[i] = (byte) (textBytes[i] ^ XOR_KEY[i % XOR_KEY.length]);
        }
        return "X" + new String(Hex.encodeHex(obfuscatedBytes));
    }
```
```java
    private static byte[] getXORKey() {
        return new byte[]{102, 108, 97, 103, 45, 87, 104, 97, 116, 68, 49, 100, 87, 51, 83, 97, 121, 65, 98, 48, 85, 84, 83, 101, 99, 114, 51, 84, 115, 63};
    }
```

We can see that a class obfuscated with the `BasicObfuscatorService` will be named:

`X240d120e4e180a0701375205235c21321c3314593631` + `$` + `X` + `hex(className ^ flag-WhatD1dW3SayAb0UTSecr3Ts?)`

`X240d120e4e180a0701375205235c21321c3314593631` is the obfuscated name of `BasicObfuscatorService`.

Since XOR is a reversible operation, if we take a class obfuscated by the `BasicObfuscatorService` (classes that start with `X240d120e4e180a0701375205235c21321c3314593631`), we can retrieve the original class name.

The class `X240d120e4e180a0701375205235c21321c3314593631$X000000000000001823744408336a6314347509551a363510101107631a0f083e041148255d00162854` is an empty class, containing no information. If we take the obfuscated class name, which is `000000000000001823744408336a6314347509551a363510101107631a0f083e041148255d00162854`, we can parse the hexadecimal and perform a XOR with `flag-WhatD1dW3SayAb0UTSecr3Ts?` to retrieve `flag-WhyW0uldY0uM4keObfusc47i0nRever5able`.