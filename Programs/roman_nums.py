roman = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M": 1000}

# num = "MMMCMXCIX"
# num = "MMXXII"
num = "DCCCXLV"

def roman_to_nums(word):

	numbers = []
	for letter in word:
		numbers.append(roman[letter])

	numbers.append(0)
	numbers.reverse()
	numbers.append(0)
	numbers.reverse()
	
	total = 0

	for index in range(len(numbers)):
		thisnum = numbers[index]
		try:
			if thisnum < numbers[index+1]:
				total -= thisnum
			else:
				total += thisnum
		except:
			pass

	print(total)

roman_to_nums(num)