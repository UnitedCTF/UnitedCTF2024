# Quotes from https://github.com/reggi/fortune-cookie

import signal
import string
import random
import re


class LeetServer():
	"""Leet Server for CTF"""
	dictLeet = {"a":"4","d":"<|","e":"3","g":"9","i":"1","l":"1","o":"0","q":"<|","s":"5","t":"7","u":"\\/","v":"\\/","y":"7","z":"2"}
	quoteFilename = "fortune-cookies.txt"
	bannerFilename = "banner.txt"
	timeout = 5 # seconds
	flag = "flag-Th3F0r7un3C00ki3IsN07ALi3"


	def __init__(self) -> None:
		with open(self.quoteFilename) as f:
			quotes = f.readlines()
		self.cleanQuotes(quotes)

	def cleanQuotes(self, quotes: str) -> None:
		forbiddenChars = string.digits
		i = 0
		self.allQuotes = []
		for quote in quotes:
			if set(quote).isdisjoint(set(forbiddenChars)):
				quote = quote.strip().lower()
				self.allQuotes.append(quote)
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

	def win(self) -> None:
		print(f"\\X/311 |)0/V3 ! Here is your flag: {self.flag}")

	def sendLeetSpeak(self, chain: str) -> None:
		leetSpeaked = ""
		for char in chain:
			if char in self.dictLeet:
				leetSpeaked += self.dictLeet[char]
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
		n = 20

		quotes = random.sample(self.allQuotes,n)

		for i in range(n):
			quote = quotes[i]
			self.sendLeetSpeak(quote)
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
			self.win()


def timeout_handler(signum, frame):
    print("T00 5l0w !")
    exit(0)


if __name__ == '__main__':
	signal.signal(signal.SIGALRM, timeout_handler)
	server = LeetServer()
	server.chall()
