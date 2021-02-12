import wave as w 
import struct
from scipy.io import wavfile
import matplotlib.pyplot as plt

file = w.open("Morse_test_file.wav","r")

samplerate, data = wavfile.read('Morse_test_file.wav')

x = []
y = []

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
prevOn = False
beeps = []
locations = []
endingLs = 0

for i, samp in enumerate(data):
	if samp == 247:
		x.append(i)
		y.append(samp)

# print(len(beeps))
morse = ""
for ind, dot in enumerate(x):

	try:
		if dot - x[ind-1] > 20000:
			# print("newWord",end="")
			morse += "newWord"
		elif dot - x[ind-1] == 16 and x[ind+1] - dot > 1500:
			# print(".",end="")
			morse += "."
		elif 45 < dot - x[ind-1] < 48:
			# print("-",end="")
			morse += "-"
		elif dot - x[ind-1] > 11000:
			# print(" ",end = "")
			morse += " "
	except:
		for r, rInd in reversed(list(enumerate(x))):
			endingLs += 1
			if rInd - x[r-1]> 1600:
				# print(endingLs)
				if endingLs > 5:
					morse += "-"
				else:
					morse += "."
				break

11,000
deciphered = ""
morse = morse.replace("---------------.", "-")
words = morse.split(sep="newWord")
for eachWord in words:
	letters = eachWord.split(" ")
	for eachLetter in letters:
		deciphered += mor[eachLetter]

	deciphered +=" "
print(words)
print(deciphered)
# print(morse)

# plt.figure(1)
# plt.plot(data)
plt.scatter(x,y)
plt.show()


47
# 30 < . < 50
# 0 < - < 20

# Function that reads picks each sequence and makes a list
# Function that reads the lists and converts them into letters/words

# go all the way from one to the next one and make sure that the interval is small enough and when it reaches the final value, append to list and count the numms of elements in list to determine dit and dah