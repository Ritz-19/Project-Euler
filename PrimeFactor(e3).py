# Euler 3: Prime Factor of a number
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

import math

#Find Factors
def find_Factors(num):
   factors = []
   for i in range(1, int(math.sqrt(num)+1)):
      if num%i == 0:
         factors.append(i)
   return factors

#Check if prime
def check_Prime(num):
   return len(find_Factors(num)) == 1

 
#main
num = int(input("Enter a Number: "))
factors = find_Factors(num)
largest = 0
for n in factors:
   b = check_Prime(n)
   if b == True and n > largest:
      largest = n
 
print("The Largest Prime Factor is: ",largest)

'''
While checking for the Factors, you can use Sqrt because the
main factors of a number only occur till its srqt, after which they are
products of the previous.
Example num = 24,
factors = 1,2,3,4,6,8,12
sqrt ~ 4
and all factors after 4 are products of 4 and before, this way you ca shorten
runtime.
'''
