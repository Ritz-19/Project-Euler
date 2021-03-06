#Even Fibonacci Number

'''
Each new term in the Fibonacci
sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million,
find the sum of the even-valued terms.
'''

num1 = 1
num2 = 2
fib, s = 0, 0
while num2<4000000:
    fib = num2 + num1
    num1 = num2
    num2 = fib
    if num2%2 == 0:
        s += fib
print(s+2)




