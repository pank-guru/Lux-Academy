def isprime():
	number = int(input("Enter a number"))
	if number == 2 or number == 3:
		return True
	if number%2 == 0 or number<2:
		return False
	for i in range (2,int(number**0.5)+1,2):
		if number%i == 0:
			return False
		return True
print(isprime())