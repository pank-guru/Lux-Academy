import math

def square(number):
	sqr = int(math.sqrt(number))
	return sqr*sqr == number

def fibonacci(num):

	return square(5*num*num + 4) or square(5*num*num - 4)

for i in range(int(input("Enter starting range:")),int(input("Enter ending  range:"))):
	if (square(i) == True):
		print (i,"is a Fibonacci Number")
	else:
		print (i,"is not a Fibonacci Number")

