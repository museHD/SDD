roman = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M": 1000}

def convert_to_num(word):
	global roman
	nlist = word.split()
	print(nlist)
	n1 = nlist[0]
	factor = 1
	answer = 0
	for letter in reversed(list(n1)):
		answer += roman[letter]*factor
		factor = factor*10
	print(answer)


expr = input("Input expression: ")
convert_to_num(expr)

