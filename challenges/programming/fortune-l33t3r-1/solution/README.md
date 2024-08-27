# Fortune L33t3r

## Write-up

L'objectif de ce challenge est de décoder une phrase reçue en [Leet speak](https://fr.wikipedia.org/wiki/Leet_speak) et de la renvoyer au serveur.

Pour automatiser la communication avec le serveur et répondre dans le temps imparti, on utilise le langage Python et la bibliothèque [pwntools](https://github.com/Gallopsled/pwntools) mais il existe de nombreuses autres alternatives.

### Difficulté 0

Dans ce premier niveau de difficulté, le texte original est encore facilement lisible et avec quelques essais on arrive à trouver la correspondance complète:

```python
{
    '4': 'a',
    '3': 'e',
    '9': 'g',
    '1': 'l',
    '0': 'o',
    '5': 's',
    '7': 't'
}
```

### Difficulté 1

Même chose que précédemment avec plus de lettre codés et moins de lisibilité. La différence majeure avec la difficulté précédente est qu'on a plus "1 caractère leet speak = 1 caractère en clair". La correspondance complète:

```python
{
    '/-\': 'a',
    '/3': 'b',
    '/-/': 'h',
    '/<': 'k',
    '/\/\': 'm',
    '/V': 'n',
    '\/': 'v',
    '\X/': 'w',
    '\|/': 'y',
    '-/_': 'z'
}
```

### Difficulté 2

Dans ce dernier niveau de difficulté toutes les lettres de l'alphabet sont changés, ce qui rend le texte difficilement lisible mais la correspondance complète est trouvable avec plusieurs citations:

```python
{
    '@': 'a',
    '|3': 'b',
    '[': 'c',
    '|)': 'd',
    '€': 'e',
    '/=': 'f',
    '9': 'g',
    ')-(': 'h',
    '1': 'i',
    '_]': 'j',
    '|<': 'k',
    '£': 'l',
    '|V|': 'm',
    '//': 'n',
    '()': 'o',
    '|>': 'p',
    '<|': 'q',
    '/2': 'r',
    '$': 's',
    '"|"': 't',
    '(_)': 'u',
    '/': 'v',
    '\\'': 'w',
    '><': 'x',
    '¥': 'y',
    '7_': 'z'
}
```

Comme on a affaire à un [code préfixe](https://fr.wikipedia.org/wiki/Code_pr%C3%A9fixe), il n'y a pas d'ambiguité lorsqu'on décode le Leet Speak.

Une fois qu'on a les 3 correspondances, on utilise la bibliothèque Python pwntools pour communiquer avec le serveur:

```python
for level in range(3):
	io = remote(HOST,PORT) # Connexion au serveur
	io.sendafter(b") : ",f"{level}\n".encode('utf-8')) # Envoi du niveau de difficulté
	for _ in range(5):
		received = io.recvuntilS(b">> ") # Attente de la phrase leet speakée
		leetQuote = re.search(r"(Leet Quote: )(.+)", received).group(2) # Lecture de la phrase leet speakée
		originalQuote = leetQuote
		for leetChar in allDicts[level]:
			originalQuote = originalQuote.replace(leetChar,allDicts[level][leetChar]) # Traduction de la phrase leet speakée
		io.sendline(originalQuote.encode('utf-8')) # Envoi de la phrase traduite
```

## Flag

`flag-7h3Fu7ur31sY0ur5`
