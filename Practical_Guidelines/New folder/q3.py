def Factorial(n) :

    prod = 1

    for i in range(1, n+1) :
        prod *= i

    return prod
'''
def Fibonacci(n):	#	RECURSIVE Version

	if n <= 0:
		print("Incorrect input")

	# First Fibonacci number is 0
	elif n == 1:
		return 0

	# Second Fibonacci number is 1
	elif n == 2:
		return 1

	# nth term = (n-1)th term - (n-2)th term
	else:
		return Fibonacci(n-1) + Fibonacci(n-2)
'''
def Fibonacci(n) :	  #	  ITERATIVE Version

	a = 0
	b = 1

	if n <= 0:
		print("Incorrect input")

	# First Fibonacci number is 0
	elif n == 1:
		return 0

	# Second Fibonacci number is 1
	elif n == 2:
		return 1

	else :

		for i in range(3, n+1) :
			c = a+b
			a = b
			b = c

		return c

def Result(n) :

    l = [Fibonacci(n), Factorial(Fibonacci(n))]
    return l

n = int(input("Enter value of 'n' : "))

res = Result(n)
print(f"Result = {res}")
