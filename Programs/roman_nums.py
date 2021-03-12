roman = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M": 1000}

# def convert_to_num(word):
# 	global roman
# 	nlist = word.split()
# 	print(nlist)
# 	n1 = nlist[0]
# 	factor = 1
# 	answer = 0
# 	for letter in reversed(list(n1)):
# 		answer += roman[letter]*factor
# 		factor = factor*10
# 	print(answer)


# expr = input("Input expression: ")
# convert_to_num(expr)

# 10 1 100 10 1000 100 1000 1000 1000
# num = "MMMCMXCIX"
# num = "MMXXII"
num = "DCCCXLV"
numbers = []
for letter in num:
	numbers.append(roman[letter])

numbers.append(0)
numbers.reverse()
numbers.append(0)
numbers.reverse()

print(numbers)


addnums = 0
newnums = []

for index in range(len(numbers)):
	thisnum = numbers[index]
	try:
		if thisnum < numbers[index+1]:
			newnums.append(-(thisnum))
			addnums -= thisnum
		else:
			newnums.append(thisnum)
			addnums += thisnum
	except:
		pass

	# if thisnum > numbers[index-1]:
	# 	addnums += (thisnum - numbers[index-1])
	# if thisnum < numbers[index-1]:
	# 	addnums += thisnum
	# if thisnum == numbers[index-1]:
	# 	addnums+=thisnum

	# print(thisnum, index)
print(addnums)