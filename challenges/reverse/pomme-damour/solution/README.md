# Pomme d'amour 🍭🍎❤️

## Write-up

Here is a line by line explanation of the v8 bytecode:

```sh
## NOTES:
##  - The last argument of an instruction can be mostly ignored, it is only for optimization
##  - Named properties are referenced from the constant pool table below (ex: 0:"process",1:"argv",etc.)
##  - There are 9 registers ranging from r0 to r8

### Put into the stack the property "process" of the object global
   26 S> 0x28890d6ba6 @    0 : 21 00 00          LdaGlobal [0], [0]
### Store stack value into r5
         0x28890d6ba9 @    3 : bf                Star5
### Put into the stack the property "argv" of r5 (process)
   38 E> 0x28890d6baa @    4 : 2d f5 01 02       GetNamedProperty r5, [1], [2]
### Store stack value into r5
         0x28890d6bae @    8 : bf                Star5
### Put into the stack the property "length" of r5 (process.argv)
   43 E> 0x28890d6baf @    9 : 2d f5 02 04       GetNamedProperty r5, [2], [4]
### Store stack value into r5
         0x28890d6bb3 @   13 : bf                Star5
### Put into the stack the value 3
         0x28890d6bb4 @   14 : 0d 03             LdaSmi [3]
### Check if r5 is equal to the stack (process.argv.length === 3)
   50 E> 0x28890d6bb6 @   16 : 6c f5 06          TestEqualStrict r5, [6]
### Jump to 0x28890d6bcc@38 if true
         0x28890d6bb9 @   19 : 98 13             JumpIfTrue [19] (0x28890d6bcc @ 38)
### Put into the stack the property "process" of the object global
   57 S> 0x28890d6bbb @   21 : 21 00 00          LdaGlobal [0], [0]
### Store stack value into r6
         0x28890d6bbe @   24 : be                Star6
### Put into the stack the property "exit" of r6 (process)
   65 E> 0x28890d6bbf @   25 : 2d f4 03 07       GetNamedProperty r6, [3], [7]
### Store stack value into r5
         0x28890d6bc3 @   29 : bf                Star5
### Put into the stack the value 1
         0x28890d6bc4 @   30 : 0d 01             LdaSmi [1]
### Store stack value into r7
         0x28890d6bc6 @   32 : bd                Star7
### Call the function at r5 (process.exit) with context r6 (process) and value r7 (1) => process.exit(1)
   65 E> 0x28890d6bc7 @   33 : 5e f5 f4 f3 09    CallProperty1 r5, r6, r7, [9]
### Put into the stack the array ("<FixedArray[28]>")
   91 S> 0x28890d6bcc @   38 : 79 04 0b 25       CreateArrayLiteral [4], [11], #37
### Store stack value into r0
         0x28890d6bd0 @   42 : c4                Star0
### Put into the stack the property "TextEncoder" of the object global
  244 S> 0x28890d6bd1 @   43 : 21 05 0c          LdaGlobal [5], [12]
### Store stack value into r6
         0x28890d6bd4 @   46 : be                Star6
### Put a new object on the stack from r6 (new TextEncoder())
  244 E> 0x28890d6bd5 @   47 : 69 f4 fa 00 0e    Construct r6, r0-r0, [14]
### Store stack value into r6
         0x28890d6bda @   52 : be                Star6
### Put into the stack the property "encode" of r6 (new TextEncoder().encode)
  262 E> 0x28890d6bdb @   53 : 2d f4 06 10       GetNamedProperty r6, [6], [16]
### Store stack value into r5
         0x28890d6bdf @   57 : bf                Star5
### Put into the stack the property "process" of the object global
  269 E> 0x28890d6be0 @   58 : 21 00 00          LdaGlobal [0], [0]
### Store stack value into r7
         0x28890d6be3 @   61 : bd                Star7
### Put into the stack the property "length" of r7 (process.argv)
  277 E> 0x28890d6be4 @   62 : 2d f3 01 02       GetNamedProperty r7, [1], [2]
### Store stack value into r7
         0x28890d6be8 @   66 : bd                Star7
### Put into the stack the value 2
         0x28890d6be9 @   67 : 0d 02             LdaSmi [2]
### Put into the stack the property on the stack (2) of r7 (process.argv)
  281 E> 0x28890d6beb @   69 : 2f f3 12          GetKeyedProperty r7, [18]
### Store stack value into r7
         0x28890d6bee @   72 : bd                Star7
### Call the function at r5 (new TextEncoder().encode) with context r6 (new TextEncoder()) and value r7 (process.argv[2]) => (new TextEncoder().encode(process.argv[2]))
  262 E> 0x28890d6bef @   73 : 5e f5 f4 f3 14    CallProperty1 r5, r6, r7, [20]
### Store stack value into r1
         0x28890d6bf4 @   78 : c3                Star1
### Put into the stack the property "length" of the r1 (new TextEncoder().encode(process.argv[2]))
  299 S> 0x28890d6bf5 @   79 : 2d f9 02 16       GetNamedProperty r1, [2], [22]
### Store stack value into r5
         0x28890d6bf9 @   83 : bf                Star5
### Put into the stack the property "length" of the r0 ("<FixedArray[28]>")
  317 E> 0x28890d6bfa @   84 : 2d fa 02 18       GetNamedProperty r0, [2], [24]
### Check if r5 is equal to the stack (new TextEncoder().encode(process.argv[2]).length === "<FixedArray[28]>".length)
  306 E> 0x28890d6bfe @   88 : 6c f5 1a          TestEqualStrict r5, [26]
### Jump to 0x28890d6c14@110 if true
         0x28890d6c01 @   91 : 98 13             JumpIfTrue [19] (0x28890d6c14 @ 110)
### Put into the stack the property "process" of the object global
  325 S> 0x28890d6c03 @   93 : 21 00 00          LdaGlobal [0], [0]
### Store stack value into r6
         0x28890d6c06 @   96 : be                Star6
### Put into the stack the property "exit" of the r6 (process)
  333 E> 0x28890d6c07 @   97 : 2d f4 03 07       GetNamedProperty r6, [3], [7]
### Store stack value into r5
         0x28890d6c0b @  101 : bf                Star5
### Put into the stack the value 1
         0x28890d6c0c @  102 : 0d 01             LdaSmi [1]
### Store stack value into r7
         0x28890d6c0e @  104 : bd                Star7
### Call the function at r5 (process.exit) with context r6 (process) and value r7 (1)
  333 E> 0x28890d6c0f @  105 : 5e f5 f4 f3 1b    CallProperty1 r5, r6, r7, [27]
### Put into the stack the value 0
  357 S> 0x28890d6c14 @  110 : 0c                LdaZero
### Store stack value into r2 (NOTE: this is a loop index, we will call it "i")
         0x28890d6c15 @  111 : c2                Star2
### Put into the stack the property "length" of the r1 (new TextEncoder().encode(process.argv[2]))
  370 S> 0x28890d6c16 @  112 : 2d f9 02 16       GetNamedProperty r1, [2], [22]
### Check if r2 is less than the stack (i < new TextEncoder().encode(process.argv[2]).length)
  362 E> 0x28890d6c1a @  116 : 6d f8 1d          TestLessThan r2, [29]
### Jump to 0x28890d6c66@192 if false
         0x28890d6c1d @  119 : 99 49             JumpIfFalse [73] (0x28890d6c66 @ 192)
### Put into the stack the value of r2
  404 S> 0x28890d6c1f @  121 : 0b f8             Ldar r2
### Put into the stack the property on the stack (i) of r1 (new TextEncoder().encode(process.argv[2])) => new TextEncoder().encode(process.argv[2])[i]
  409 E> 0x28890d6c21 @  123 : 2f f9 1e          GetKeyedProperty r1, [30]
### Store stack value into r3
         0x28890d6c24 @  126 : c1                Star3
### Put into the stack the value 0
  431 S> 0x28890d6c25 @  127 : 0c                LdaZero
### Store stack value into r4 (NOTE: this is another loop index, we will call it "j")
         0x28890d6c26 @  128 : c0                Star4
### Put into the stack the value of r2 (i)
  436 S> 0x28890d6c27 @  129 : 0b f8             Ldar r2
### Add 1 to the value on the stack (i+1)
  440 E> 0x28890d6c29 @  131 : 44 01 20          AddSmi [1], [32]
### Check if r4 is less than the stack (j < i+1)
  436 E> 0x28890d6c2c @  134 : 6d f6 21          TestLessThan r4, [33]
### Jump to 0x28890d6c49@163 if false
         0x28890d6c2f @  137 : 99 1a             JumpIfFalse [26] (0x28890d6c49 @ 163)
### Put into the stack the value of r4 (j)
  458 S> 0x28890d6c31 @  139 : 0b f6             Ldar r4
### Put into the stack the property on the stack (j) of r0 ("<FixedArray[28]>") => ("<FixedArray[28]>"[j])
  487 E> 0x28890d6c33 @  141 : 2f fa 24          GetKeyedProperty r0, [36]
### Add r3 (new TextEncoder().encode(process.argv[2])[i]) to the value on the stack => ("<FixedArray[28]>"[j]+(new TextEncoder().encode(process.argv[2])[i]))
  479 E> 0x28890d6c36 @  144 : 38 f7 23          Add r3, [35]
### Modulo 255 the value on the stack
  492 E> 0x28890d6c39 @  147 : 00 48 ff 00 22 00 ModSmi.Wide [255], [34]
### Store stack value into r3
         0x28890d6c3f @  153 : c1                Star3
### Put into the stack the value of r4 (j)
  447 S> 0x28890d6c40 @  154 : 0b f6             Ldar r4
### Increase the value on the stack by 1 (j+1)
         0x28890d6c42 @  156 : 50 26             Inc [38]
### Store stack value into r4
         0x28890d6c44 @  158 : c0                Star4
### Loop back to 0x28890d6c27@129
  418 E> 0x28890d6c45 @  159 : 89 1e 01 27       JumpLoop [30], [1], [39] (0x28890d6c27 @ 129)
### Put into the stack the value 0
  509 S> 0x28890d6c49 @  163 : 0c                LdaZero
### Check if r3 is equal to the stack (loop j value === 0)
  522 E> 0x28890d6c4a @  164 : 6c f7 28          TestEqualStrict r3, [40]
### Jump to 0x28890d6c5d@183 if true
         0x28890d6c4d @  167 : 98 10             JumpIfTrue [16] (0x28890d6c5d @ 183)
### Put into the stack the property "process" of the object global
  529 S> 0x28890d6c4f @  169 : 21 00 00          LdaGlobal [0], [0]
### Store stack value into r6
         0x28890d6c52 @  172 : be                Star6
### Put into the stack the property "exit" of r6 (process)
  537 E> 0x28890d6c53 @  173 : 2d f4 03 07       GetNamedProperty r6, [3], [7]
### Store stack value into r5
         0x28890d6c57 @  177 : bf                Star5
### Call the function at r5 (process.exit) with context r6 (process) and value r3 (loop j value)
  537 E> 0x28890d6c58 @  178 : 5e f5 f4 f7 29    CallProperty1 r5, r6, r3, [41]
### Put into the stack the value of r2 (i)
  380 S> 0x28890d6c5d @  183 : 0b f8             Ldar r2
### Increase the value on the stack by 1 (i+1)
         0x28890d6c5f @  185 : 50 2b             Inc [43]
### Store stack value into r2
         0x28890d6c61 @  187 : c2                Star2
### Loop back to 0x28890d6c16@112
  344 E> 0x28890d6c62 @  188 : 89 4c 00 2c       JumpLoop [76], [0], [44] (0x28890d6c16 @ 112)
### Put into the stack the property "process" of the object global
  559 S> 0x28890d6c66 @  192 : 21 00 00          LdaGlobal [0], [0]
### Store stack value into r6
         0x28890d6c69 @  195 : be                Star6
### Put into the stack the property "exit" of r6 (process)
  567 E> 0x28890d6c6a @  196 : 2d f4 03 07       GetNamedProperty r6, [3], [7]
### Store stack value into r5
         0x28890d6c6e @  200 : bf                Star5
### Put into the stack the value 0
         0x28890d6c6f @  201 : 0c                LdaZero
### Store stack value into r7
         0x28890d6c70 @  202 : bd                Star7
### Call the function at r5 (process.exit) with context r6 (process) and value r7 (0)
  567 E> 0x28890d6c71 @  203 : 5e f5 f4 f3 2d    CallProperty1 r5, r6, r7, [45]
### Put into the stack the value undefined
         0x28890d6c76 @  208 : 0e                LdaUndefined
### Return the value on the stack
  576 S> 0x28890d6c77 @  209 : a9                Return
Constant pool (size = 7)
0x28890d6b29: [FixedArray] in OldSpace
 - map: 0x3d45b4980211 <Map(FIXED_ARRAY_TYPE)>
 - length: 7
           0: 0x3055918421f1 <String[7]: #process>
           1: 0x35c757e7f8f9 <String[4]: #argv>
           2: 0x3d45b4984791 <String[6]: #length>
           3: 0x30559184a071 <String[4]: #exit>
           4: 0x0028890d6b11 <ArrayBoilerplateDescription PACKED_SMI_ELEMENTS, 0x0028890d6a21 <FixedArray[28]>>
           5: 0x305591850a91 <String[11]: #TextEncoder>
           6: 0x305591850ab1 <String[6]: #encode>
```

Which gives the following decompiled code:

```javascript
r5 = process.argv.length;
if (r5 !== 3) {
  r6 = process;
  r5 = process.exit;
  r7 = 1;
  r5.call(r6, r7);
}
r0 = Array(28); // Contains something we do not know yet
r6 = new TextEncoder();
r5 = r6.encode;
r7 = process.argv[2];
r1 = r5.call(r6, r7);
r5 = r1.length;
if (r5 !== r0.length) {
  r6 = process;
  r5 = process.exit;
  r7 = 1;
  r5.call(r6, r7);
}
r2 = 0;
do {
  if (r2 < r1.length) {
    r3 = r1[r2];
    r4 = 0;
    do {
      if (r4 < r2 + 1) {
        r3 += r0[r4];
        r3 %= 255;
        r4 += 1;
      } else {
        break;
      }
    } while (true);
    if (r3 !== 0) {
      r6 = process;
      r5 = process.exit;
      r5.call(r6, r3);
    }
    r2 += 1;
  } else {
    break;
  }
} while (true);
r6 = process;
r5 = process.exit;
r7 = 0;
r5.call(r6, r7);
```

The compiled code can be simplified to the following javascript code:

```javascript
if (process.argv.length !== 3) {
  process.exit(1);
}
const secret = Array(28); // Contains something we do not know yet
const input = new TextEncoder().encode(process.argv[2]);
if (secret.length !== input.length) {
  process.exit(1);
}
for (let i = 0; i < secret.length; ++i) {
  let check = secret[i];
  for (let j = 0; j < i + 1; ++j) {
    check = (check + secret[j]) % 255;
  }
  if (check !== 0) {
    process.exit(check);
  }
}
process.exit(0);
```

Now, all we need to resolve the challenge is the value of the `secret` array. To obtain it, we will create full string dump with the command `strings` of the challenge. While there is a lot of data, one of the hints given is that it was packed using `Node SEA`. To find the start of the packed code, all we have to do is search for the last instance of the string `NODE_SEA_BLOB`.

```javascript
// NODE_SEA_BLOB
// challenge.jsc.js
require("node:v8").setFlagsFromString("--no-lazy");
require("node:v8").setFlagsFromString("--no-flush-bytecode");
new (require("vm").Script)(`"${" ".repeat(565)}"`, {
  cachedData: Buffer.from(
    [
      251, 50, 233, 247, 60, 245, 211, 55, 0, 53, 55, 55, 210, 22, 25, 157, 151,
      51, 55, 55, 55, 55, 55, 55, 54, 43, 99, 54, 23, 49, 159, 87, 55, 55, 55,
      55, 61, 55, 55, 55, 54, 59, 123, 87, 55, 55, 55, 55, 54, 55, 55, 55, 54,
      43, 99, 54, 179, 167, 87, 55, 55, 55, 55, 229, 55, 55, 55, 54, 19, 123,
      87, 55, 55, 55, 55, 48, 55, 55, 55, 54, 59, 101, 86, 65, 95, 110, 120, 48,
      55, 55, 55, 71, 69, 88, 84, 82, 68, 68, 55, 54, 59, 101, 86, 33, 201, 225,
      172, 51, 55, 55, 55, 86, 69, 80, 65, 55, 55, 55, 55, 49, 90, 53, 54, 59,
      101, 86, 213, 44, 97, 21, 51, 55, 55, 55, 82, 79, 94, 67, 55, 55, 55, 55,
      54, 59, 49, 102, 61, 87, 55, 55, 55, 55, 55, 55, 55, 55, 54, 79, 122, 75,
      55, 55, 55, 55, 43, 55, 55, 55, 55, 55, 55, 55, 174, 55, 55, 55, 55, 55,
      55, 55, 206, 55, 55, 55, 55, 55, 55, 55, 60, 55, 55, 55, 55, 55, 55, 55,
      206, 55, 55, 55, 55, 55, 55, 55, 13, 55, 55, 55, 55, 55, 55, 55, 245, 55,
      55, 55, 55, 55, 55, 55, 62, 55, 55, 55, 55, 55, 55, 55, 221, 55, 55, 55,
      55, 55, 55, 55, 34, 55, 55, 55, 55, 55, 55, 55, 218, 55, 55, 55, 55, 55,
      55, 55, 39, 55, 55, 55, 55, 55, 55, 55, 199, 55, 55, 55, 55, 55, 55, 55,
      62, 55, 55, 55, 55, 55, 55, 55, 207, 55, 55, 55, 55, 55, 55, 55, 204, 55,
      55, 55, 55, 55, 55, 55, 37, 55, 55, 55, 55, 55, 55, 55, 223, 55, 55, 55,
      55, 55, 55, 55, 50, 55, 55, 55, 55, 55, 55, 55, 56, 55, 55, 55, 55, 55,
      55, 55, 53, 55, 55, 55, 55, 55, 55, 55, 196, 55, 55, 55, 55, 55, 55, 55,
      60, 55, 55, 55, 55, 55, 55, 55, 201, 55, 55, 55, 55, 55, 55, 55, 204, 55,
      55, 55, 55, 55, 55, 55, 194, 55, 55, 55, 55, 55, 55, 55, 58, 55, 55, 55,
      55, 55, 55, 55, 199, 55, 55, 55, 55, 55, 55, 55, 48, 55, 55, 55, 54, 39,
      101, 85, 225, 103, 33, 128, 60, 55, 55, 55, 99, 82, 79, 67, 114, 89, 84,
      88, 83, 82, 69, 55, 55, 55, 55, 55, 54, 59, 101, 86, 81, 48, 207, 32, 49,
      55, 55, 55, 82, 89, 84, 88, 83, 82, 55, 55, 49, 214, 54, 54, 11, 124, 90,
      55, 55, 55, 55, 95, 55, 55, 55, 54, 103, 53, 43, 62, 7, 60, 35, 56, 43,
      61, 43, 62, 23, 38, 55, 61, 95, 61, 211, 51, 62, 55, 58, 127, 60, 43, 62,
      23, 56, 39, 62, 124, 59, 163, 54, 60, 127, 62, 28, 61, 123, 62, 23, 38,
      55, 61, 87, 51, 3, 62, 40, 61, 171, 54, 50, 35, 63, 111, 51, 35, 50, 39,
      48, 56, 61, 111, 50, 107, 48, 40, 48, 3, 57, 172, 54, 60, 68, 63, 227, 53,
      52, 31, 61, 43, 62, 23, 60, 55, 61, 244, 51, 60, 184, 54, 63, 151, 49, 62,
      23, 56, 55, 59, 19, 76, 119, 55, 55, 55, 63, 55, 55, 55, 55, 55, 55, 55,
      55, 55, 22, 55, 55, 136, 26, 194, 54, 53, 136, 26, 194, 53, 51, 136, 58,
      52, 91, 194, 49, 175, 36, 22, 55, 55, 137, 26, 195, 52, 48, 136, 58, 54,
      138, 105, 194, 195, 196, 62, 78, 51, 60, 18, 243, 22, 50, 59, 137, 94,
      195, 205, 55, 57, 137, 26, 195, 49, 39, 136, 22, 55, 55, 138, 26, 196, 54,
      53, 138, 58, 53, 24, 196, 37, 138, 105, 194, 195, 196, 35, 244, 26, 206,
      53, 33, 136, 26, 205, 53, 47, 91, 194, 45, 175, 36, 22, 55, 55, 137, 26,
      195, 52, 48, 136, 58, 54, 138, 105, 194, 195, 196, 44, 59, 245, 26, 206,
      53, 33, 90, 207, 42, 174, 126, 60, 207, 24, 206, 41, 246, 59, 247, 60,
      207, 115, 54, 23, 90, 193, 22, 174, 45, 60, 193, 24, 205, 19, 15, 192, 20,
      55, 127, 200, 55, 21, 55, 246, 60, 193, 103, 17, 247, 190, 41, 54, 16, 59,
      91, 192, 31, 175, 39, 22, 55, 55, 137, 26, 195, 52, 48, 136, 105, 194,
      195, 192, 30, 60, 207, 103, 28, 245, 190, 123, 55, 27, 22, 55, 55, 137,
      26, 195, 52, 48, 136, 59, 138, 105, 194, 195, 196, 26, 57, 158, 54, 19,
      100, 85, 55, 55, 55, 55, 245, 70, 54, 55, 55, 55, 55, 55, 55, 55, 55, 55,
      55, 55, 55, 55, 55, 55, 55, 55, 54, 39, 101, 85, 149, 9, 100, 100, 62, 55,
      55, 55, 84, 95, 86, 91, 91, 82, 89, 80, 82, 55, 55, 55, 55, 55, 55, 55,
      87, 55, 55, 55, 55, 200, 200, 200, 200, 115, 86, 55, 55, 55, 55, 36, 55,
      55, 55, 55, 55, 55, 55, 5, 53, 55, 55, 54, 47, 49, 175, 83, 24, 55, 55,
      55, 55, 55, 55, 55, 49, 35, 103, 55, 134, 55, 53, 17, 49, 39, 103, 55, 63,
      39, 103, 55, 50, 115, 53, 21, 63, 247, 63, 22, 63, 247, 44, 62, 55, 105,
      53, 55, 54, 127, 49, 150, 61, 48, 55, 54, 35, 101, 84, 45, 213, 121, 23,
      32, 55, 55, 55, 82, 65, 86, 91, 90, 86, 84, 95, 94, 89, 82, 25, 11, 86,
      89, 88, 89, 78, 90, 88, 66, 68, 9, 55, 86, 55, 55, 55, 55, 55, 55, 55, 55,
      55, 55, 55, 55, 55, 55, 55, 55, 115, 87, 55, 55, 55, 55, 53, 55, 55, 55,
      115, 87, 55, 55, 55, 55, 69, 55, 55, 55, 115, 87, 55, 55, 55, 55, 55, 55,
      55, 55, 54, 39, 49, 118, 54, 87, 55, 55, 55, 55, 53, 55, 55, 55, 46, 52,
      55, 46, 52, 59, 115, 87, 55, 55, 55, 55, 61, 55, 55, 55, 183, 115, 106,
      115, 86, 55, 55, 54, 55, 37, 55, 53, 55, 183, 39, 55, 55, 54, 55, 55, 55,
      164, 54, 39, 124, 85, 55, 55, 55, 55, 62, 55, 55, 55, 54, 51, 53, 55, 60,
      251, 38, 63, 39, 55, 55, 55, 55, 55, 55, 55, 85, 39, 55, 55, 55, 63, 55,
      55, 55, 55, 55, 55, 55, 55, 55, 183, 55, 55, 55, 244, 86, 206, 55, 243,
      158, 54, 23, 100, 85, 55, 55, 55, 55, 115, 7, 55, 55, 55, 55, 55, 55, 55,
      55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 126, 85, 55, 55, 55, 55, 200,
      200, 200, 200, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 0, 53, 55,
      55, 54, 59, 163, 86, 53, 55, 55, 55, 54, 55, 55, 55, 51, 55, 55, 55, 55,
      55, 55, 55, 52, 115, 86, 55, 55, 54, 55, 55, 55, 53, 55, 55, 39, 55, 63,
      55, 55, 55, 55, 60, 61, 61, 61, 61, 61, 61, 61,
    ].map((b) => b ^ 0x137)
  ),
}).runInThisContext();
```

By XOR'ing each byte of the array by `0x137` and putting it in a file, we get the following hexdump of the bytecode:

```sh
00000000: cc05 dec0 0bc2 e400 3702 0000 e521 2eaa  ........7....!..
00000010: a004 0000 0000 0000 011c 5401 2006 a860  ..........T. ..`
00000020: 0000 0000 0a00 0000 010c 4c60 0000 0000  ..........L`....
00000030: 0100 0000 011c 5401 8490 6000 0000 00d2  ......T...`.....
00000040: 0000 0001 244c 6000 0000 0007 0000 0001  ....$L`.........
00000050: 0c52 61ea a7b7 2b07 0000 0070 726f 6365  .Ra...+....proce
00000060: 7373 0001 0c52 61d6 2f6e 5504 0000 0061  ss...Ra./nU....a
00000070: 7267 7600 0000 0006 6d02 010c 5261 5a1d  rgv.....m...RaZ.
00000080: 0ec9 0400 0000 6578 6974 0000 0000 010c  ......exit......
00000090: 0651 0a60 0000 0000 0000 0000 0178 4d7c  .Q.`.........xM|
000000a0: 0000 0000 1c00 0000 0000 0000 9900 0000  ................
000000b0: 0000 0000 f900 0000 0000 0000 0b00 0000  ................
000000c0: 0000 0000 f900 0000 0000 0000 3a00 0000  ............:...
000000d0: 0000 0000 c200 0000 0000 0000 0900 0000  ................
000000e0: 0000 0000 ea00 0000 0000 0000 1500 0000  ................
000000f0: 0000 0000 ed00 0000 0000 0000 1000 0000  ................
00000100: 0000 0000 f000 0000 0000 0000 0900 0000  ................
00000110: 0000 0000 f800 0000 0000 0000 fb00 0000  ................
00000120: 0000 0000 1200 0000 0000 0000 e800 0000  ................
00000130: 0000 0000 0500 0000 0000 0000 0f00 0000  ................
00000140: 0000 0000 0200 0000 0000 0000 f300 0000  ................
00000150: 0000 0000 0b00 0000 0000 0000 fe00 0000  ................
00000160: 0000 0000 fb00 0000 0000 0000 f500 0000  ................
00000170: 0000 0000 0d00 0000 0000 0000 f000 0000  ................
00000180: 0000 0000 0700 0000 0110 5262 8ae7 2791  ..........Rb..'.
00000190: 0b00 0000 5465 7874 456e 636f 6465 7200  ....TextEncoder.
000001a0: 0000 0000 010c 5261 5e30 0056 0600 0000  ......Ra^0.V....
000001b0: 656e 636f 6465 0000 06e1 0101 3c4b 6d00  encode......<Km.
000001c0: 0000 0068 0000 0001 5002 1c09 300b 140f  ...h....P...0...
000001d0: 1c0a 1c09 2011 000a 680a e404 0900 0d48  .... ...h......H
000001e0: 0b1c 0920 0f10 094b 0c94 010b 4809 2b0a  ... ...K....H.+.
000001f0: 4c09 2011 000a 6004 3409 1f0a 9c01 0514  L. ...`.4.......
00000200: 0858 0414 0510 070f 0a58 055c 071f 0734  .X.......X.\...4
00000210: 0e9b 010b 7308 d402 0328 0a1c 0920 0b00  ....s....(... ..
00000220: 0ac3 040b 8f01 08a0 0609 200f 000c 247b  .......... ...${
00000230: 4000 0000 0800 0000 0000 0000 0000 2100  @.............!.
00000240: 00bf 2df5 0102 bf2d f502 04bf 0d03 6cf5  ..-....-......l.
00000250: 0698 1321 0000 be2d f403 07bf 0d01 bd5e  ...!...-.......^
00000260: f5f4 f309 7904 0b25 c421 050c be69 f4fa  ....y..%.!...i..
00000270: 000e be2d f406 10bf 2100 00bd 2df3 0102  ...-....!...-...
00000280: bd0d 022f f312 bd5e f5f4 f314 c32d f902  .../...^.....-..
00000290: 16bf 2dfa 0218 6cf5 1a98 1321 0000 be2d  ..-...l....!...-
000002a0: f403 07bf 0d01 bd5e f5f4 f31b 0cc2 2df9  .......^......-.
000002b0: 0216 6df8 1d99 490b f82f f91e c10c c00b  ..m...I../......
000002c0: f844 0120 6df6 2199 1a0b f62f fa24 38f7  .D. m.!..../.$8.
000002d0: 2300 48ff 0022 00c1 0bf6 5026 c089 1e01  #.H.."....P&....
000002e0: 270c 6cf7 2898 1021 0000 be2d f403 07bf  '.l.(..!...-....
000002f0: 5ef5 f4f7 290b f850 2bc2 894c 002c 2100  ^...)..P+..L.,!.
00000300: 00be 2df4 0307 bf0c bd5e f5f4 f32d 0ea9  ..-......^...-..
00000310: 0124 5362 0000 0000 c271 0100 0000 0000  .$Sb.....q......
00000320: 0000 0000 0000 0000 0000 0000 0110 5262  ..............Rb
00000330: eeec 0a1a 0900 0000 6368 616c 6c65 6e67  ........challeng
00000340: 6500 0000 0000 0000 6000 0000 00ff ffff  e.......`.......
00000350: ff44 6100 0000 0013 0000 0000 0000 0032  .Da............2
00000360: 0200 0001 1806 9864 2f00 0000 0000 0000  .......d/.......
00000370: 0614 5000 b100 0226 0610 5000 0810 5000  ..P....&..P...P.
00000380: 0544 0222 08c0 0821 08c0 1b09 005e 0200  .D."...!.....^..
00000390: 0148 06a1 0a07 0001 1452 63fa 9faa 1417  .H.......Rc.....
000003a0: 0000 0065 7661 6c6d 6163 6869 6e65 2e3c  ...evalmachine.<
000003b0: 616e 6f6e 796d 6f75 733e 0061 0000 0000  anonymous>.a....
000003c0: 0000 0000 0000 0000 0000 0000 4460 0000  ............D`..
000003d0: 0000 0200 0000 4460 0000 0000 7200 0000  ......D`....r...
000003e0: 4460 0000 0000 0000 0000 0110 0641 0160  D`...........A.`
000003f0: 0000 0000 0200 0000 1903 0019 030c 4460  ..............D`
00000400: 0000 0000 0a00 0000 8044 5d44 6100 0001  .........D]Da...
00000410: 0012 0002 0080 1000 0001 0000 0093 0110  ................
00000420: 4b62 0000 0000 0900 0000 0104 0200 0bcc  Kb..............
00000430: 1108 1000 0000 0000 0000 6210 0000 0008  ..........b.....
00000440: 0000 0000 0000 0000 0080 0000 00c3 61f9  ..............a.
00000450: 00c4 a901 2053 6200 0000 0044 3000 0000  .... Sb....D0...
00000460: 0000 0000 0000 0000 0000 0000 0000 0049  ...............I
00000470: 6200 0000 00ff ffff ff00 0000 0000 0000  b...............
00000480: 0000 0000 0037 0200 0001 0c94 6102 0000  .....7......a...
00000490: 0001 0000 0004 0000 0000 0000 0003 4461  ..............Da
000004a0: 0000 0100 0000 0200 0010 0008 0000 0000  ................
000004b0: 0b0a 0a0a 0a0a 0a0a                      ........
```

The constant pool is situated at the start of the bytecode. We can see some known strings of the constant pool such as `process`, `argv` and `exit`. The array is located between the `exit` and the `TextEncoder` as defined by the constant pool. We can search for the pattern `00? 00 ?00 ?1c` (28) to identify the begining of the array:

```sh
00000080: 0ec9 0400 0000 6578 6974 0000 0000 010c  ......exit......
00000090: 0651 0a60 0000 0000 0000 0000 0178 4d7c  .Q.`.........xM|
#------array-length-vv------array-start-vv
000000a0: 0000 0000 1c00 0000 0000 0000 9900 0000  ................
000000b0: 0000 0000 f900 0000 0000 0000 0b00 0000  ................
000000c0: 0000 0000 f900 0000 0000 0000 3a00 0000  ............:...
000000d0: 0000 0000 c200 0000 0000 0000 0900 0000  ................
000000e0: 0000 0000 ea00 0000 0000 0000 1500 0000  ................
000000f0: 0000 0000 ed00 0000 0000 0000 1000 0000  ................
00000100: 0000 0000 f000 0000 0000 0000 0900 0000  ................
00000110: 0000 0000 f800 0000 0000 0000 fb00 0000  ................
00000120: 0000 0000 1200 0000 0000 0000 e800 0000  ................
00000130: 0000 0000 0500 0000 0000 0000 0f00 0000  ................
00000140: 0000 0000 0200 0000 0000 0000 f300 0000  ................
00000150: 0000 0000 0b00 0000 0000 0000 fe00 0000  ................
00000160: 0000 0000 fb00 0000 0000 0000 f500 0000  ................
00000170: 0000 0000 0d00 0000 0000 0000 f000 0000  ................
00000180: 0000 0000 0700 0000 0110 5262 8ae7 2791  ..........Rb..'.
#---------array-end-^^
00000190: 0b00 0000 5465 7874 456e 636f 6465 7200  ....TextEncoder.
```

The value of the `secret` array is:

```javascript
secret = [
  0x99, 0xf9, 0xb, 0xf9, 0x3a, 0xc2, 0x9, 0xea, 0x15, 0xed, 0x10, 0xf0, 0x9,
  0xf8, 0xfb, 0x12, 0xe8, 0x5, 0xf, 0x2, 0xf3, 0xb, 0xfe, 0xfb, 0xf5, 0xd, 0xf0,
  0x7,
];
```

We can then solve the challenge by running the following code:

```javascript
const secret = [
  0x99, 0xf9, 0xb, 0xf9, 0x3a, 0xc2, 0x9, 0xea, 0x15, 0xed, 0x10, 0xf0, 0x9,
  0xf8, 0xfb, 0x12, 0xe8, 0x5, 0xf, 0x2, 0xf3, 0xb, 0xfe, 0xfb, 0xf5, 0xd, 0xf0,
  0x7,
];
const flag = new Array(28);
for (let i = 0; i < flag.length; ++i) {
  for (let charCode = 0, value = -1; value !== 0; ++charCode) {
    value = flag[i] = charCode;
    for (let j = 0; j < i + 1; ++j) {
      value = (value + secret[j]) % 255;
    }
  }
}
console.log(String.fromCharCode(...flag));
```

## Flag

`flag-javascriptbytecodeisfun`
