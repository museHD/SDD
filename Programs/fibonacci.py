def fibonacci(n):
	prevnum = 0
	nextnum = 1
	final = 0
	finalList = [0,1]
	for x in range(n):
		final=prevnum+nextnum
		finalList.append(final)
		prevnum=nextnum
		nextnum=final
		print()
	print(finalList[n-1])
fibonacci(4)

# initlist = [0,1]
# tries = 995
# def fib_rec(n1):
# 	if n1 == 1:
# 		return 0
# 	else:
# 		return (n1 + fib_rec(n1))

# print(fib_rec(2))