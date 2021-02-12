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
# fibonacci(4)

runs = 0
n1 = 0
n2 = 1


def fib_rec(n):
	global runs, n1, n2
	runs += 1

	if runs == n+1:
		return n2
	elif n == 0:
		return None
	elif n == 1:
		return 0

	temp = n1
	n1 = n2
	n2 = temp + n2
	print(runs,n2)
	fib_rec(n)

# print(fib_rec(5))
fib_rec(10)




'''
nth num in fib
fib returns 0+1 = 1
fib runs

Code found on the internet 
# Function for nth Fibonacci number
 
def Fibonacci(n):
    if n<0:
        print("Incorrect input")
    # First Fibonacci number is 0
    elif n==0:
        return 0
    # Second Fibonacci number is 1
    elif n==1:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)
 
# Driver Program
 
print(Fibonacci(9))
 
#This code is contributed by Saket Modi

'''