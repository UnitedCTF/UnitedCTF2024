# Ride Management System 1
## Write-up
### Solution (Français)
Lorsque nous exécutons le logiciel, un numéro de série nous est demandé. Si nous entrons un caractère qui n'est pas un chiffre, le StackTrace suivant est affiché :

```java 
Exception in thread "main" java.util.InputMismatchException
        at java.base/java.util.Scanner.throwFor(Scanner.java:939)
        at java.base/java.util.Scanner.next(Scanner.java:1594)
        at java.base/java.util.Scanner.nextInt(Scanner.java:2258)
        at java.base/java.util.Scanner.nextInt(Scanner.java:2212)
        at Main.ZmxhZy1Eb250UHJpbnRUaGVTdGFja1RyYWNl(Main.java:32)
        at Main.whatEvenIsBase64(Main.java:24)
        at Main.secretFunction(Main.java:19)
        at Main.readSomething(Main.java:10)
        at Main.main(Main.java:6)
```

Nous pouvons voir une méthode `ZmxhZy1Eb250UHJpbnRUaGVTdGFja1RyYWNl` ainsi que `whatEvenIsBase64`.

Nous pouvons utiliser cette dernière comme indice afin de décrypter `ZmxhZy1Eb250UHJpbnRUaGVTdGFja1RyYWNl`, ce qui nous donne:

 `flag-DontPrintTheStackTrace`
### Solution (English)

When we run the software, a serial number is requested. If we enter a character that is not a digit, the following StackTrace is displayed:

```java 
Exception in thread "main" java.util.InputMismatchException
        at java.base/java.util.Scanner.throwFor(Scanner.java:939)
        at java.base/java.util.Scanner.next(Scanner.java:1594)
        at java.base/java.util.Scanner.nextInt(Scanner.java:2258)
        at java.base/java.util.Scanner.nextInt(Scanner.java:2212)
        at Main.ZmxhZy1Eb250UHJpbnRUaGVTdGFja1RyYWNl(Main.java:32)
        at Main.whatEvenIsBase64(Main.java:24)
        at Main.secretFunction(Main.java:19)
        at Main.readSomething(Main.java:10)
        at Main.main(Main.java:6)
```

We can see a method `ZmxhZy1Eb250UHJpbnRUaGVTdGFja1RyYWNl` as well as `whatEvenIsBase64`.

We can use the latter as a clue to decrypt `ZmxhZy1Eb250UHJpbnRUaGVTdGFja1RyYWNl`, which gives us:

 `flag-DontPrintTheStackTrace`