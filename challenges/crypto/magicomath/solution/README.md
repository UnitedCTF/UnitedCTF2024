# MagicoMath

## Write-up (français)

### Part 1

Dans ce challenge on doit "décrypter" un message avec seulement une fonction d'encryption. Spécifiquement, une fonction d'encryption qui nous laisse ajouter des octets arbitraires après chaque charactère du flag.

Puisque cette fonction fonctionne en ECB, elle traite le message en blocks de 16 octets. On doit donc simplement faire deux choses.

Premimèrement, on ajoute 15 octets bidons entre les charactères du flag. Ceci va mettre un charactère du flag en première position dans chaque block du plaintext, où l'on connais les autres charactères. Il ne nous restera qu'à "brute force" les charactères ASCII (~96 options).

À noter: il faut enlever le dernier block, c'est le padding PKCS7.

```python
remote.sendline(b"00"*15)
message = bytes.fromhex(remote.readline().decode())

blocks = [message[i:i+16] for i in range(0, len(message)-16, 16)]
```

Deuxièment donc, on essaie pour tous les charactères de répliquer le format qu'on connais, jusqu'à ce qu'on aie des blocks qui encryptent à la même chose que tous les blocks du flag. On fait ceci en mettant 15 octets bidons, le charactère qu'on essaie, puis 15 octets bidons encore. Ceci va transformer la moitié de blocks. On peut alors simplement prendre le deuxième block de la réponse et vérifier si le ciphertext est le même qu'un des blocks du flag.

```python
zeros = [0]*15
for i in range(127,0,-1):
	joiner = bytes(zeros+[i]+zeros)
	remote.sendline(joiner.hex().encode())
	response = bytes.fromhex(remote.readline().decode())
	chrblock = response[16:32]

	if chrblock in missing:
		missing.remove(chrblock)
		solutions[chrblock] = chr(i)
		if len(missing) == 0:
			break

print("".join([solutions[block] for block in blocks]))
```

Et voilà le premier flag!

### Part 2

Le challenge a pas vraiment changé: la solution à la deuxième partie est aussi applicable à la première. Cependant, la deuxième partie nous force d'être un peu plus sophistiqué.

On a le droit à une seule encryption ici. Il faut alors combiner tout nos encryptions en une seule.

Additionnellement, on a pas seulement du texte cette fois, alors on doit envoyer 256 blocks de valeurs qu'on connais, toujours en utilisant les même 15 octets bidons pour chaque octet qu'on connait ou veut déchiffrer.

```python
zeros = [0]*15
known_blocks = chain.from_iterable([i]+zeros for i in range(256))
remote.sendline((bytes(zeros) + bytes(known_blocks)).hex().encode())

message = bytes.fromhex(remote.readline().decode())
blocks = [message[i:i+16] for i in range(0, len(message)-16, 16)]
```

Maintenant qu'on a les blocks, on associe les blocks qu'on connait à leur octet de plaintext.

```python
solutions = {blocks[i+1]: i for i in range(256)}
```

Finalement, on utilise nos associations pour faire le processus inverse sur les blocks qu'on voulait connaître, se rappelant de sauter au-dessus de 256 blocks à chaque fois puisque notre plaintext choisi est entre chaque octet du plaintext inconnu.

```python
solved = bytes([solutions[block] for block in blocks[:-256:257]])

remote.sendline(solved.hex().encode())
print(remote.recv().decode())
```

Et on reçoit le flag!

## Write-up (english)

### Part 1

In this challenge, we need to "decrypt" a message with only an encryption function. Specifically, the function lets us add arbritrary characters after every byte of the message.

Because this encrpytion function is a block cipher in ECB mode, we only need to obtain pairs of known plaintext-ciphertext blocks.

So first, we simply add 15 bytes (any that we know, though 15 nulls is the most obvious) after every character, giving us one ciphertext block for every character of plaintext we want to obtain. We will then only need to "brute force" the printable ASCII characters (~96).

N.B. the last block is discarded because it is PKCS7 padding.

```python
remote.sendline(b"00"*15)
message = bytes.fromhex(remote.readline().decode())

blocks = [message[i:i+16] for i in range(0, len(message)-16, 16)]
```

Then, we try each possible characters, replicating the format we put the flag characters in, until we've figured out the plaintext for every ciphertext block in the flag we obtained in the above step. We do this by putting any 15 bytes, our character, then our 15 known bytes again. This will make half of the blocks into our known plaintext block. We can simply take the second block of the response and check if it's part of the flag ciphertext blocks.

```python
zeros = [0]*15
for i in range(127,0,-1):
	joiner = bytes(zeros+[i]+zeros)
	remote.sendline(joiner.hex().encode())
	response = bytes.fromhex(remote.readline().decode())
	chrblock = response[16:32]

	if chrblock in missing:
		missing.remove(chrblock)
		solutions[chrblock] = chr(i)
		if len(missing) == 0:
			break

print("".join([solutions[block] for block in blocks]))
```

And that's the first flag!

### Part 2

The second part of the challenge is actually the same: we can apply the technique we'll use here to the first part too. The only important change is that only one encryption is allowed this time, so we need to be a little more sophisticated.

All we really do now is stuff all of our encryptions into one. Because we aren't dealing only with text anymore, we need to get a full 256 blocks with known plaintext.

```python
zeros = [0]*15
known_blocks = chain.from_iterable([i]+zeros for i in range(256))
remote.sendline((bytes(zeros) + bytes(known_blocks)).hex().encode())

message = bytes.fromhex(remote.readline().decode())
blocks = [message[i:i+16] for i in range(0, len(message)-16, 16)]
```

We then associate the blocks in the ciphertext we've received with the byte values we know:

```python
solutions = {blocks[i+1]: i for i in range(256)}
``` 

And finally, use those associations to get the plaintext for the blocks we aren't supposed to know. Just remember to skip over 256 blocks every time since our chosen plaintext went between every byte of unknown plaintext.

```python
solved = bytes([solutions[block] for block in blocks[:-256:257]])

remote.sendline(solved.hex().encode())
print(remote.recv().decode())
```

Congrats, you've got the second flag!

## Flags

Part 1: `flag-th3ecbp3ngu1nsaysh3ll0`

Part 2: `flag-d0ntl1m1ty0urs3lf`
