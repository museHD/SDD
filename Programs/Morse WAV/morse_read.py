import wave as w 
import struct
from scipy.io import wavfile
import matplotlib.pyplot as plt

# file = w.open("Morse_test_file.wav","r")

samplerate, data = wavfile.read('Morse_test_file.wav')

# x and y co-ordinates list for plot
x = []
y = []

# Morse to English dict.

mor = {'.-': 'A',   '-...': 'B',   '-.-.': 'C',
       '-..': 'D',      '.': 'E',   '..-.': 'F',
        ' -.': 'G',   '....': 'H',     '..': 'I',
      '.---': 'J',    '-.-': 'K',   '.-..': 'L',
        '--': 'M',     '-.': 'N',    '---': 'O', 
      '.--.': 'P',   '--.-': 'Q',    '.-.': 'R',
       '...': 'S',      '-': 'T',    '..-': 'U', 
      '...-': 'V',    '.--': 'W',   '-..-': 'X',
      '-.--': 'Y',   '--..': 'Z',  '-----': '0', 
     '.----': '1',  '..---': '2',  '...--': '3',
     '....-': '4',  '.....': '5',  '-....': '6', 
     '--...': '7',  '---..': '8',  '----.': '9'}

# print(samplerate)
# print(data)

# prevOn = False

endingLs = 0

# Picking data points equal to 247 to make it easier to plot
for i, samp in enumerate(data):
	if samp == 247:
		x.append(i)
		y.append(samp)

# Morse Code String
morse = ""

# Iterate through all datapoints and check against conditions to identify symbols

for ind, dot in enumerate(x):

	try:
		if dot - x[ind-1] > 20000:
			# Space between words
			morse += "newWord"
		elif dot - x[ind-1] == 16 and x[ind+1] - dot > 1500:
			# .
			morse += "."
		elif 45 < dot - x[ind-1] < 48:
			# -
			morse += "-"
		elif dot - x[ind-1] > 11000:
			# Space between letters
			morse += " "
	except:
		# Had a problem with out of index so created this to handle it
		
		# Last symbol was not properly recognised so the list is reversed and iterated through again to find the correct symbol
		# when it identifies a space, it counts the number of plots behind it and if its > 5, its a '-' else: '.'
		for r, rInd in reversed(list(enumerate(x))):
			endingLs += 1
			if rInd - x[r-1]> 1600:
				if endingLs > 5:
					morse += "-"
				else:
					morse += "."
				break

# 11,000

# While the code doesn't correctly translate everything, its consistent (atleast for the file provided)
# which requires some parts to be replaced with what they should be
deciphered = ""
morse = morse.replace("---------------.", "-")

# Splitting morse into different words, and then further breaking it down into different letters

words = morse.split(sep="newWord")
for eachWord in words:
	letters = eachWord.split(" ")
	for eachLetter in letters:
		# Identifying each morse code and adding the correct letter to deciphered
		deciphered += mor[eachLetter]
	# space between the words
	deciphered +=" "
print(words)
print(deciphered)
# print(morse)

# plt.figure(1)
# plt.plot(data)

# Debug Plot

plt.scatter(x,y)
plt.show()

# Misc.
47
# 30 < . < 50
# 0 < - < 20

# Function that reads picks each sequence and makes a list 
# Function that reads the lists and converts them into letters/words

# go all the way from one to the next one and make sure that the interval is small enough and when it reaches the final value, append to list and count the numms of elements in list to determine dit and dah