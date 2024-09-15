# Ride Management System 4
## Write-up
### Solution (Français)
Dans les fichiers, nous remarquons les classes `ObfuscatorService`, `BasicObfuscatorService` ainsi que `ComplexObfuscatorService`. En analysant `BasicObfuscatorService`, nous remarquons que la méthode `obfuscate()` ne fait qu'un simple XOR avec une clée sous le format de `byte[]`. 

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
Si nous convertissons les bytes de la clée en texte, nous trouvons que la valeur de la clée est `flag-WhatD1dW3SayAb0UTSecr3Ts?`

### Solution (English)

In the files, we notice the classes `ObfuscatorService`, `BasicObfuscatorService`, and `ComplexObfuscatorService`. By analyzing `BasicObfuscatorService`, we see that the `obfuscate()` method performs a simple XOR with a key in the format of a `byte[]`.

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

If we convert the key bytes to text, we find that the key's value is `flag-WhatD1dW3SayAb0UTSecr3Ts?`