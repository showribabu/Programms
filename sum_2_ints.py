#1. Write a program that takes two integers as input and outputs their sum.

#method1 
a,b=list(map(int,input('Enter 2 integers with space:').split())) #unpack 
print(f'The sum of {a} and {b} is : %d '%(a+b))

#method 2

print(int(input('enter first value:'))+int(input('Enter second value:')))

