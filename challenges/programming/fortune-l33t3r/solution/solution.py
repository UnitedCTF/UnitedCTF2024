from pwn import *
import re


HOST = "localhost"
PORT = 1337

dictLvl0 = {'4': 'a', '3': 'e', '9': 'g', '1': 'l', '0': 'o', '5': 's', '7': 't'}
dictLvl1 = {'/-\\': 'a', '/3': 'b', '/-/': 'h', '/<': 'k', '/\\/\\': 'm', '/V': 'n', '\\/': 'v', '\\X/': 'w', '\\|/': 'y', '-/_': 'z'}
dictLvl2 = {'@': 'a', '|3': 'b', '[': 'c', '|)': 'd', '€': 'e', '/=': 'f', '9': 'g', ')-(': 'h', '1': 'i', '_]': 'j', '|<': 'k', '£': 'l', '|V|': 'm', '/\\/': 'n', '()': 'o', '|>': 'p', '<|': 'q', '/2': 'r', '$': 's', '"|"': 't', '(_)': 'u', '\\/': 'v', "\\\\'": 'w', '><': 'x', '¥': 'y', '7_': 'z'}
allDicts = [dictLvl0, dictLvl1, dictLvl2]

flag = ""

for level in range(3):
	io = remote(HOST,PORT)
	io.sendafter(b") : ",f"{level}\n".encode('utf-8'))
	for _ in range(5):
		received = io.recvuntilS(b">> ")
		leetQuote = re.search(r"(Leet Quote: )(.+)", received).group(2)
		originalQuote = leetQuote
		for leetChar in allDicts[level]:
			originalQuote = originalQuote.replace(leetChar,allDicts[level][leetChar])
		print(leetQuote)
		print(originalQuote)
		io.sendline(originalQuote.encode('utf-8'))
	io.recvline()
	received = io.recvlineS()
	flag += re.search(r"(flag: )(.+)", received).group(2)
	io.close()

print(flag)