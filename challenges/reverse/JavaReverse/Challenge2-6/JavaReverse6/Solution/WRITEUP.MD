# JavaReverse 6
## Write-up
### Solution (Français)


----
#### TLDR:
En exploitant l'utilisation de la reflection dans le logiciel on peux créer un object `CMPLX$2a53573b514b2c2044253c3f494a3951362c43313f55494e$CMPLX$575e476452b7a36bc09da9a8a676a5ac9d6ac14da8a9abacaca8a469c252aab2ab77abb49ebbc2a2a87caba5abaca466c0a3aab2ab7bb65a665c4778baaaafa6a5a69db8c2`.

A partir de cet objet on peut appeller la méthode privée `CMPLX$2a311a37258a753c92217a78797d7f4b6c8f92717b7e794f` 
pour print le flag.

Flag: `flag-CarefulW1thRef1ec7i0n`

----
Nous avons plusieurs classes qui commencent par `CMPLX$2a53573b514b2c2044253c3f494a3951362c43313f55494e`, nous indiquant qu'elles ont été obfusqués par le `ComplexObfuscatorService`.

```java
protected String obfuscate(String text) {
    int depth = 10;
    Base64.Encoder encoder = Base64.getEncoder();
    byte[] key = new byte[depth];
    String b64 = text;

    for(int i = 0; i < depth; ++i) {
        b64 = new String(encoder.encode(b64.getBytes()));
        key[i] = b64.getBytes()[i];
    }

    int[] res = this.xor(text.getBytes(), key);
    byte[] res2 = ((ByteArrayOutputStream)Arrays.stream(res).map((ix) -> {
        return Integer.valueOf(ix + res.length).byteValue();
    }).collect(ByteArrayOutputStream::new, (baos, ix) -> {
        baos.write((byte)ix);
    }, (baos1, baos2) -> {
        baos1.write(baos2.toByteArray(), 0, baos2.size());
    })).toByteArray();
    String var10000 = new String(Hex.encodeHex(res2));
    return "CMPLX$" + var10000;
}
```

 Parmis elles se trouve `CMPLX$2a53573b514b2c2044253c3f494a3951362c43313f55494e$CMPLX$575e476452b7a36bc09da9a8a676a5ac9d6ac14da8a9abacaca8a469c252aab2ab77abb49ebbc2a2a87caba5abaca466c0a3aab2ab7bb65a665c4778baaaafa6a5a69db8c2`, qui contient la méthode `CMPLX$2a311a37258a753c92217a78797d7f4b6c8f92717b7e794f`.
 
Nous voyons dans cette fonction une variable `encFlag`, et que nous imprimons l'output de `CMPLX$2a53573b514b2c2044253c3f494a3951362c43313f55494e$CMPLX$5b624b6856bba76fc4a1adacaa7aa9b0a16ec551acadafb0b0aca86dc656aeb6af7bafb8a2bfc6a6ac80afa9afb0a86ac4a7aeb6af7fba5e6a604b7cbeae7ca979a9a4bcc5a2b0b0af.CMPLX$464d365341a68da6b09297659b9e95688da4af8f9765956a94948cb2b3869699986a95688857ae4197649a6b9a948c5ab33d9699(encFlag)`. 

```java
private void CMPLX$2a311a37258a753c92217a78797d7f4b6c8f92717b7e794f() {
    Main.complexObfuscatorService.invokeMethodFromObfuscatedClass(CMPLX$2a53573b514b2c2044253c3f494a3951362c43313f55494e$CMPLX$363d26433196829aa02e875a848b8b588198a17f878b87568a858198a382875987898858.class, "CMPLX$6d745d7a68cdb981d6b3bfbebc8cbbc2b380d763bebfc1c2c2beba7fd868c0c8c18dc1cab4d1d8b8be92c1bbc1c2ba7cd6b9c0c8c191cc707c725d8ed0c0c2bcc0bfb7d1d6b5c2c092bfc0bf64d08ab4c4c18ebcbcbfb3d0d6b5c2", Boolean.class, (Object)null, new Object[0]);
    String encFlag = 264f413e245b462e2d192c.CMPLX$4a1f2862464f3333452339(5b624b6856bba76fc4a1adacaa7aa9b0a16ec551acadafb0b0aca86dc656aeb6af7bafb8a2bfc6a6ac80afa9afb0a86ac4a7aeb6af7fba5e6a604b7cbeae7ca979a9a4bcc5a2b0b0af.CMPLX$464d365341a68da6b09297659b9e95688da4af8f9765956a94948cb2b3869699986a95688857ae4197649a6b9a948c5ab33d9699((String)Main.basicObfuscatorService.invokeMethodFromObfuscatedClass(X240d120e4e180a0701375205235c21321c3314593631$X25030f014430.class, "get", String.class, (Object)null, new Object[]{5b624b6856bba76fc4a1adacaa7aa9b0a16ec551acadafb0b0aca86dc656aeb6af7bafb8a2bfc6a6ac80afa9afb0a86ac4a7aeb6af7fba5e6a604b7cbeae7ca979a9a4bcc5a2b0b0af.CMPLX$464d365341a68da6b09297659b9e95688da4af8f9765956a94948cb2b3869699986a95688857ae4197649a6b9a948c5ab33d9699((String)Main.basicObfuscatorService.invokeMethodFromObfuscatedClass(X240d120e4e180a0701375205235c21321c3314593631$X25030f014430.class, 5b624b6856bba76fc4a1adacaa7aa9b0a16ec551acadafb0b0aca86dc656aeb6af7bafb8a2bfc6a6ac80afa9afb0a86ac4a7aeb6af7fba5e6a604b7cbeae7ca979a9a4bcc5a2b0b0af.CMPLX$464d365341a68da6b09297659b9e95688da4af8f9765956a94948cb2b3869699986a95688857ae4197649a6b9a948c5ab33d9699((String)Main.basicObfuscatorService.invokeMethodFromObfuscatedClass(X240d120e4e180a0701375205235c21321c3314593631$X25030f014430.class, "get", String.class, (Object)null, new Object[]{"c"})), String.class, (Object)null, new Object[]{5b624b6856bba76fc4a1adacaa7aa9b0a16ec551acadafb0b0aca86dc656aeb6af7bafb8a2bfc6a6ac80afa9afb0a86ac4a7aeb6af7fba5e6a604b7cbeae7ca979a9a4bcc5a2b0b0af.CMPLX$464d365341a68da6b09297659b9e95688da4af8f9765956a94948cb2b3869699986a95688857ae4197649a6b9a948c5ab33d9699((String)Main.basicObfuscatorService.invokeMethodFromObfuscatedClass(X240d120e4e180a0701375205235c21321c3314593631$X25030f014430.class, "get", String.class, (Object)null, new Object[]{"d"}))}))})));
    encFlag = encFlag.substring(0, encFlag.length() - 1);
    System.out.println(5b624b6856bba76fc4a1adacaa7aa9b0a16ec551acadafb0b0aca86dc656aeb6af7bafb8a2bfc6a6ac80afa9afb0a86ac4a7aeb6af7fba5e6a604b7cbeae7ca979a9a4bcc5a2b0b0af.CMPLX$464d365341a68da6b09297659b9e95688da4af8f9765956a94948cb2b3869699986a95688857ae4197649a6b9a948c5ab33d9699(encFlag));
}
```

Comme on ne peux pas retrouver les noms de classes et fonctions original du à l'obfuscation, il est difficile de comprendre ce qu'il se passe. 


```java
//Pseudocode de la Ligne 1:
//Main.complexObfuscatorService.invokeMethodFromObfuscatedClass(CMPLX$2a53573b514b2c2044253c3f494a3951362c43313f55494e$CMPLX$363d26433196829aa02e875a848b8b588198a17f878b87568a858198a382875987898858.class, "CMPLX$6d745d7a68cdb981d6b3bfbebc8cbbc2b380d763bebfc1c2c2beba7fd868c0c8c18dc1cab4d1d8b8be92c1bbc1c2ba7cd6b9c0c8c191cc707c725d8ed0c0c2bcc0bfb7d1d6b5c2c092bfc0bf64d08ab4c4c18ebcbcbfb3d0d6b5c2", Boolean.class, (Object)null, new Object[0]);
SecurityManager.confirmSecurity()
```
Le SecurityManager.confirmSecurity() permet de s'assurer que le code qui roule n'a pas été modifié. 

Cette fonction permet de s'assurer que la fonction roule uniqument dans le logiciel, que la signature de la fonction est identique à l'originale et que la classe n'a pas été modifiée.

Cette fonction est là pour compliquer l'obtention du flag et est utilisé un peu partout dans le logiciel. De plus, elle est des fois appellée par la fonction `ComplexObfuscatorService.invokeMethodFromObfuscatedClass()` afin d'amener plus de confusion.

Cela enlève l'option d'appeller la fonction a partir d'une autre classe et nous laisse quelques options:

- Trouver une façon de bypass le SecurityManager
  - Peut etre fait en modifiant la fonction pour toujours retourner true
- Essayer de comprendre comment le flag est encrypté manuellement
- Trouver une façon d'appeller la méthode même si elle est private

```java
//Pseudocode de la ligne 2:
//String encFlag = 264f413e245b462e2d192c.CMPLX$4a1f2862464f3333452339(5b624b6856bba76fc4a1adacaa7aa9b0a16ec551acadafb0b0aca86dc656aeb6af7bafb8a2bfc6a6ac80afa9afb0a86ac4a7aeb6af7fba5e6a604b7cbeae7ca979a9a4bcc5a2b0b0af.CMPLX$464d365341a68da6b09297659b9e95688da4af8f9765956a94948cb2b3869699986a95688857ae4197649a6b9a948c5ab33d9699((String)Main.basicObfuscatorService.invokeMethodFromObfuscatedClass(X240d120e4e180a0701375205235c21321c3314593631$X25030f014430.class, "get", String.class, (Object)null, new Object[]{5b624b6856bba76fc4a1adacaa7aa9b0a16ec551acadafb0b0aca86dc656aeb6af7bafb8a2bfc6a6ac80afa9afb0a86ac4a7aeb6af7fba5e6a604b7cbeae7ca979a9a4bcc5a2b0b0af.CMPLX$464d365341a68da6b09297659b9e95688da4af8f9765956a94948cb2b3869699986a95688857ae4197649a6b9a948c5ab33d9699((String)Main.basicObfuscatorService.invokeMethodFromObfuscatedClass(X240d120e4e180a0701375205235c21321c3314593631$X25030f014430.class, 5b624b6856bba76fc4a1adacaa7aa9b0a16ec551acadafb0b0aca86dc656aeb6af7bafb8a2bfc6a6ac80afa9afb0a86ac4a7aeb6af7fba5e6a604b7cbeae7ca979a9a4bcc5a2b0b0af.CMPLX$464d365341a68da6b09297659b9e95688da4af8f9765956a94948cb2b3869699986a95688857ae4197649a6b9a948c5ab33d9699((String)Main.basicObfuscatorService.invokeMethodFromObfuscatedClass(X240d120e4e180a0701375205235c21321c3314593631$X25030f014430.class, "get", String.class, (Object)null, new Object[]{"c"})), String.class, (Object)null, new Object[]{5b624b6856bba76fc4a1adacaa7aa9b0a16ec551acadafb0b0aca86dc656aeb6af7bafb8a2bfc6a6ac80afa9afb0a86ac4a7aeb6af7fba5e6a604b7cbeae7ca979a9a4bcc5a2b0b0af.CMPLX$464d365341a68da6b09297659b9e95688da4af8f9765956a94948cb2b3869699986a95688857ae4197649a6b9a948c5ab33d9699((String)Main.basicObfuscatorService.invokeMethodFromObfuscatedClass(X240d120e4e180a0701375205235c21321c3314593631$X25030f014430.class, "get", String.class, (Object)null, new Object[]{"d"}))}))})));
encFlag = HTTPRequests.post("/thisisandendpointithink")
```

`HTTPRequest` est la classe `CMPLX$2a53573b514b2c2044253c3f494a3951362c43313f55494e$CMPLX$264f413e245b462e2d192c` et elle permet de communiquer avec le serveur HTTP qui est lancé avec nôtre application (`CMPLX$2a53573b514b2c2044253c3f494a3951362c43313f55494e$CMPLX$234c3e3b0a5c2f39.CMPLX$1513160a15()` permet de start le serveur). 

La majorité du code dans cette ligne permet simplement d'obtenir `"/thisisandendpointithink"` en récupérant des strings du fichier `config.conf` et en les décryptant.

La réponse du post va être notre string encrypté.

```java
encFlag = encFlag.substring(0, encFlag.length() - 1);
```
Cette ligne enlève le `\r` ajoutée par le serveur HTTP

```java
//Pseudocode pour la ligne 4
//System.out.println(CMPLX$2a53573b514b2c2044253c3f494a3951362c43313f55494e$CMPLX$5b624b6856bba76fc4a1adacaa7aa9b0a16ec551acadafb0b0aca86dc656aeb6af7bafb8a2bfc6a6ac80afa9afb0a86ac4a7aeb6af7fba5e6a604b7cbeae7ca979a9a4bcc5a2b0b0af.CMPLX$464d365341a68da6b09297659b9e95688da4af8f9765956a94948cb2b3869699986a95688857ae4197649a6b9a948c5ab33d9699(encFlag));
println(HomemadeEncryption.decrypt(encFlag))
```
Ici nous décryptons le flag et on le print. La partie la plus difficile ici est de comprendre l'encryption. Malheureusement le challenge à été designé dans le but de rendre ça aussi long et fastidieux que possible. 

Voici les étapes pour encrypter le flag:
- ToBase64
- ToBinary(No delimiter) pour chaque caractère
- XOR({0x1})
- ToBinary(No delimiter) pour chaque caractère
- Rot7 pour chaque caractère
- ToDecimal(; as a delimiter) pour chaque caractère
- XOR("rotatethat")
- ToBinary(NoDelimiter) pour chaque caractère
- ToDecimal(" " as a delimiter) pour chaque caractère
- ToBase64
- ToHex

Comme on peut voir avec la multitude d'étapes, cela va nous donner un string extremement long, et quasi impossible à restore manuellement.

Le flag est encrypté avant d'être mis dans le fichier de config. Comme le fichier de config est rempli d'autre strings quasiment similaire, incluant des faux flags, il est difficile d'identifier lequel est le bon.

Cela nous laisse avec 2 options pour print le flag:
- Modifier le SecurityManager pour retourner True, rendre la méthode pour print le flag publique et l'appeller dans Main
- Utiliser la reflection
  

### Solution (English)
