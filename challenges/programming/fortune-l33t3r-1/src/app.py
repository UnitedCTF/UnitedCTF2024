# Quotes from https://github.com/reggi/fortune-cookie

import signal
import string
import random

class LeetServer():
	"""Leet Server for CTF"""
	dictLvl0 = {"a":"4","e":"3","g":"9","l":"1","o":"0","s":"5","t":"7"}
	dictLvl1 = {"a":"/-\\","b":"/3","h":"/-/","k":"/<","m":"/\\/\\","n":"/V","v":"\\/","w":"\\X/","y":"\\|/","z":"-/_"}
	dictLvl2 = {"a":"@","b":"|3","c":"[","d":"|)","e":"€","f":"/=","g":"9","h":")-(","i":"1","j":"_]","k":"|<","l":"£","m":"|V|","n":"/\\/","o":"()","p":"|>","q":"<|","r":"/2","s":"$","t":'"|"',"u":"(_)","v":"\\/","w":"\\\\'","x":"><","y":"¥","z":"7_"}
	allDicts = [dictLvl0, dictLvl1, dictLvl2]
	quoteFilename = "fortune-cookies.txt"
	bannerFilename = "banner.txt"
	timeout = 10 # seconds
	flag = ["flag-7h3","Fu7ur3","1sY0ur5"] # "flag-7h3Fu7ur31sY0ur5"


	def __init__(self) -> None:
		with open(self.quoteFilename) as f:
			quotes = f.readlines()
		self.cleanQuotes(quotes)

	def cleanQuotes(self, quotes: str) -> None:
		forbiddenChars = string.digits
		i = 0
		self.allQuotes = [[], [], []]
		for quote in quotes:
			if set(quote).isdisjoint(set(forbiddenChars)):
				quote = quote.strip().lower()
				if i < 20: # 20 quotes for level 1
					self.allQuotes[0].append(quote)
				elif i < 60: # 40 quotes for level 2
					self.allQuotes[1].append(quote)
				else: # 65 quotes for level 3 (without counting forbidden quotes)
					self.allQuotes[2].append(quote)
				i += 1


	### I/O functions ###

	def welcome(self) -> None:
		with open(self.bannerFilename,'r') as f:
			print(f.read())
		print("Peux tu me renvoyer la phrase encodé en clair ? Toutes les lettres sont en minuscule.")
		print("Can you send me the sentence back in plain text ? All letters are lowercase.")
		print()

	def gameOver(self) -> None:
		print("7h3 myst3ri3s 0f 7h3 univ3rs3 4r3 unf4th0m4bl3 f0r y0u...")

	def badResponse(self) -> None:
		print("B4d r3sp0ns3 !")

	def goodResponse(self) -> None:
		print("G00d r3sp0ns3 !")

	def win(self, difficultyLevel: int) -> None:
		nTh = {0:"1st",1:"2nd",2:"3rd"}
		print(f"\\X/311 |)0/V3 ! This is the {nTh[difficultyLevel]} part of the flag: {self.flag[difficultyLevel]}")

	def chooseDifficultyLevel(self) -> int:
		retry = True
		while retry:
			difficultyLevel = input(f"Choose your level of difficulty (from 0 to {len(self.allDicts)-1}) : ").strip()
			if difficultyLevel.isdigit() and 0 <= int(difficultyLevel) <= len(self.allDicts)-1:
				retry = False
		return int(difficultyLevel)

	def sendLeetSpeak(self, chain: str, level: int) -> None:
		assert level < len(self.allDicts)
		dictLvl = self.allDicts[level]
		leetSpeaked = ""
		for char in chain:
			if char in dictLvl:
				leetSpeaked += dictLvl[char]
			else:
				leetSpeaked += char
		print(f"Leet Quote: {leetSpeaked}")

	def recvResponse(self) -> str:
		signal.alarm(self.timeout)
		response = input(">> ")
		signal.alarm(0)
		return response

	#####################


	def chall(self) -> None:
		self.welcome()
		defeat = False
		n = 5

		difficultyLevel = self.chooseDifficultyLevel()
		quotes = random.sample(self.allQuotes[difficultyLevel],n)

		for i in range(n):
			quote = quotes[i]
			self.sendLeetSpeak(quote,difficultyLevel)
			response = self.recvResponse()
			
			# print(f"Expected : {quote}")
			# print(f"Received : {response}")

			if response == quote:
				# Good response, continue
				self.goodResponse()
				continue
			else:
				# Bad response
				defeat = True
				self.badResponse()
				break
				
		if defeat:
			# Game Over
			self.gameOver()
			exit(0)
		else:
			self.win(difficultyLevel)


def timeout_handler(signum, frame):
    print("T00 5l0w !")
    exit(0)


if __name__ == '__main__':
	signal.signal(signal.SIGALRM, timeout_handler)
	server = LeetServer()
	server.chall()
