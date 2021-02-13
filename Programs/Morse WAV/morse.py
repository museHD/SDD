import wave, struct
import matplotlib.pyplot as plt

wavefile = wave.open('Morse_test_file.wav', 'r')

full = []

length = wavefile.getnframes()
for i in range(0, length):
	try:
	    wavedata = wavefile.readframes(2)
	    data = struct.unpack("H", wavedata)
	    full.append(int(data[0]))

	except:
		pass
# print(full)
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

# prevOn = False

endingLs = 0

# Picking data points equal to 247 to make it easier to plot
for j, samp in enumerate(full):
	if samp > 63400:
		x.append(j)
		y.append(10)

plt.scatter(x = x, y = y)
plt.show()
