#Check to see if its a prime number

num = int(input("Enter a Number: "))

if num > 1:
	for x in range(2,num):
		if num%x==0 :
			print("Not a Prime Number!")
			break
	else:
		print("Prime Numer!")



