import random

# Player Bot
class Player(object):

	def __init__(self, range):
		self.min = range-range
		self.max = range
		self.myGuess = 0
		self.tries=1

	# Function to print messages with a prefix
	def sendMessage(self, message):
		print("Player: {0}".format(message))

	# Binary Search (finds the average of the boundaries of the range)
	def guessNum(self):
		return(int((self.min+self.max)/2))

	def firstGuess(self,):
		self.myGuess = self.guessNum()
		self.sendMessage("I know that the range is {0} so I will guess {1}".format(self.max,self.myGuess))
		
	# Checks whether result is higher or lower and guesses accordingly
	def guess(self, result):

		if result == "HIGHER":
			self.min = self.myGuess
			self.myGuess = self.guessNum()
			self.sendMessage("Is it {0}?".format(self.myGuess))
		elif result == "LOWER":
			self.max = self.myGuess
			self.myGuess = self.guessNum()
			self.sendMessage("Is it {0}?".format(self.myGuess))

# Host Bot
class Host(object):

	def __init__(self, range):
		self.range = range
		self.tries = 0
		self.result = "A"
		self.secret = 0
		self.endgame = False

	# Function to print message with a prefix
	def sendMessage(self, message):
		print("Host: {0}".format(message))

	# Generate random number
	def randomGen(self):
		self.secret = random.randint(0, self.range)
		self.sendMessage(("Shhh! The secret number is {0}".format(self.secret)))

	# Checks player input and returns HIGHER or LOWER or ends the game for correct answer
	def check(self, guess):
		if guess == self.secret:
			self.sendMessage("Good Job! You got it right. Only took you {0} tries".format(self.tries))
			self.endgame = True

		elif guess < self.secret:
			self.sendMessage("Sorry! My number is HIGHER than {0}".format(guess))
			self.tries += 1
			self.result = "HIGHER"

		elif guess > self.secret:
			self.sendMessage("Sorry! My number is LOWER than {0}".format(guess))
			self.tries += 1
			self.result = "LOWER"

try:
	#theRange = int(input("Hey Spectator, Input the range for our game: "))
	theRange = 100000
except:
	print("Thats not a proper number!")

# Instantiate classes and call their basic functions
myHost = Host(theRange)
myHost.randomGen()

myPlayer = Player(theRange)
myPlayer.firstGuess()
myHost.check(myPlayer.myGuess)

# Until myHost declares game to have ended, keeps guessing and checking
while myHost.endgame == False:
	myPlayer.guess(myHost.result)
	myHost.check(myPlayer.myGuess)
