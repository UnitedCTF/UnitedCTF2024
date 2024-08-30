# Shellcode Obfuscation 1
## Write-up
### Solution (Français)
On peut facilement créer du shellcode avec la librairie pwntools de python:

```python
from pwnlib.shellcraft import amd64

code = ""
code += amd64.pushstr("Barbe à papa\n")
code += amd64.linux.write(1,'rsp',13)

print(code)
```

Ce qui nous genere:
```assembly
mov rax, 0x101010101010101
push rax
mov rax, 0x101010101010101 ^ 0xa6170617020
xor [rsp], rax
mov rax, -0x5f3cdf9a9d8d9ebe
push rax
push 1
pop rdi
push 0xe
pop rdx
mov rsi, rsp
push SYS_write
pop rax
syscall
```

En utilisant la fonction `asm()` de pwnlib, on obtient les bytes suivants:
`\x48\xb8\x01\x01\x01\x01\x01\x01\x01\x01\x50\x48\xb8\x21\x71\x60\x71\x60\x0b\x01\x01\x48\x31\x04\x24\x48\xb8\x42\x61\x72\x62\x65\x20\xc3\xa0\x50\x6a\x01\x5f\x6a\x0e\x5a\x48\x89\xe6\x6a\x01\x58\x0f\x05` 

Si on les execute on obtient le flag.

Flag: `flag-X9F3K7ZQ2JPXLMN4V5QW8TYC6DZ8JR6A`

### Solution (English)
You can easily create shellcode with python's pwntools library:

```python
from pwnlib.shellcraft import amd64

code = “”
code += amd64.pushstr("Barbe à papa\n")
code += amd64.linux.write(1,'rsp',13)

print(code)
```

Which generates us:
```assembly
mov rax, 0x101010101010101
push rax
mov rax, 0x101010101010101 ^ 0xa6170617020
xor [rsp], rax
mov rax, -0x5f3cdf9a9d8d9ebe
push rax
push 1
pop rdi
push 0xe
pop rdx
mov rsi, rsp
push SYS_write
pop rax
syscall
```

Using pwnlib's `asm()` function, we obtain the following bytes:
`\x48\xb8\x01\x01\x01\x01\x01\x01\x01\x01\x50\x48\xb8\x21\x71\x60\x71\x60\x0b\x01\x01\x48\x31\x04\x24\x48\xb8\x42\x61\x72\x62\x65\x20\xc3\xa0\x50\x6a\x01\x5f\x6a\x0e\x5a\x48\x89\xe6\x6a\x01\x58\x0f\x05` 

If you execute them, you get the flag.

Flag: `flag-X9F3K7ZQ2JPXLMN4V5QW8TYC6DZ8JR6A`