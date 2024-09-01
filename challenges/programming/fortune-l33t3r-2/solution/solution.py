from pwn import *
import re
import itertools
import string

HOST = "localhost"
PORT = 1337

dictSolo = {'4': 'a', '3': 'e', '9': 'g', '0': 'o', '5': 's', '2': 'z'}
dictMultiple = {'<|': ['d', 'q'], '1': ['i', 'l'], '7': ['t', 'y'], '\\/': ['u', 'v']}
englishWordlistFile = "words_alpha.txt"
littleEnglishWordlistFile = "google-10000-english-usa-no-swears.txt"

with open(englishWordlistFile,'r') as f:
	englishWordlist = f.read().splitlines()

with open(littleEnglishWordlistFile,'r') as f:
	littleEnglishWordlist = f.read().splitlines()

def main():
	io = remote(HOST,PORT) # Connexion au serveur
	for _ in range(20):
		received = io.recvuntilS(b">> ") # Attente de la phrase leet speakée
		leetQuote = re.search(r"(Leet Quote: )(.+)", received).group(2) # Lecture de la phrase leet speakée
		originalQuote = leetQuote


		for leetChar in dictSolo:
			originalQuote = originalQuote.replace(leetChar,dictSolo[leetChar]) # Traduction de la phrase leet speakée pour les lettres dont on est sûr
		
		wordsInQuote = re.findall(r"[a-z0-9<|\\\/]+",originalQuote) # Récupération d'une liste de tout les mots de la phrase en cours de traduction


		for word in wordsInQuote:
			if set(word).issubset(set(string.ascii_lowercase)): # Le mot est déjà entièrement traduit
				continue
			
			starWord = word
			possibleChars = []
			# print(starWord)
			while not set(starWord).issubset(set(string.ascii_lowercase+"*")): # On remplace le leet speak incertain par des '*' pour faciliter le traitement et on sauvegarde les lettres possibles dans l'ordre
				dictIndex = {k:starWord.find(k) for k in dictMultiple.keys()}
				dictIndex = {k:v for k,v in sorted(dictIndex.items(),key=lambda x: x[1])}
				for leetChar,index in dictIndex.items():
					if index != -1:
						starWord = starWord.replace(leetChar,"*",1)
						possibleChars.append(dictMultiple[leetChar])
						break

			# print(starWord)
			allLettersCombos = list(itertools.product(*possibleChars)) # Génération de toutes les combinaisons de lettres possibles

			notExistingWords = []
			existingWords = []
			for lettersCombo in allLettersCombos: # Génération de tout les mots possibles avec les combinaisons générées précédemment
				testWord = starWord
				i = 0
				for letter in lettersCombo:
					assert "*" in testWord
					testWord = testWord.replace("*",letter,1)
				assert not "*" in testWord

				if testWord in englishWordlist: # Séparation des mots générés en deux catégories: ceux qui existent et ceux qui n'existent pas
					existingWords.append(testWord)
				else:
					notExistingWords.append(testWord)

			# print(f"Existing words:", existingWords)

			if len(existingWords) == 0: # Faux négatif du test d'existence
				# Le mot n'a pas été trouvé, il faut que l'utilisateur choisisse
				print("Choisissez le mot le plus probable:")
				for i, testWord in enumerate(notExistingWords):
					print(f"{i}: {testWord}")
				number = int(input("Votre choix: "))
				assert 0 <= number < len(notExistingWords)
				newWord = notExistingWords[number]

			elif len(existingWords) == 1: # Il n'y a qu'un seul mot possible, pas besoin d'intervention
				newWord = existingWords[0]

			else: # Plusieurs mots sont possibles, on choisit le plus fréquent de ceux là dans la langue anglaise
				minIndex = len(littleEnglishWordlist)
				for existingWord in existingWords:
					try:
						minIndex = min(minIndex, littleEnglishWordlist.index(existingWord))
					except ValueError:
						pass

				if minIndex != len(littleEnglishWordlist):
					newWord = littleEnglishWordlist[minIndex]
				else: # Dans le cas où plusieurs mots sont possibles mais qu'aucun n'est fréquent, c'est à l'utilisateur de trancher
					print("Choisissez le mot le plus probable:")
					for i, testWord in enumerate(existingWords):
						print(f"{i}: {testWord}")
					number = int(input("Votre choix: "))
					assert 0 <= number < len(existingWords)
					newWord = existingWords[number]

			# print(f"Before replacement: {originalQuote}")
			originalQuote = originalQuote.replace(word, newWord, 1)
			# print(f"Word '{word}' is replaced by '{newWord}'")
			# print(f"After replacement: {originalQuote}")
			# print()
				

		print(f'Leet: "{leetQuote}"')
		print(f'Plaintext: "{originalQuote}"\n')
		io.sendline(originalQuote.encode('utf-8')) # Envoi de la phrase traduite
	io.recvline()
	received = io.recvlineS() # Réception d'une partie du flag
	flag = re.search(r"(flag: )(.+)", received).group(2)
	io.close()
	print(f"\nFlag: {flag}")


if __name__ == '__main__':
	main()
