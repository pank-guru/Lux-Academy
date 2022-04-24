number=int(input("Enter a number:"))
if number>1:
    for i in range(2,number//2):
        if(number%i)==0:
            print(number,"is not a prime number")
            break
    else:
        print(number,"is a prime number")
else:
    print(number,"is neither prime nor composite")