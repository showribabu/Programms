#8. Write a program that takes an array of integers as input and outputs the sum of all the numbers that are greater than or equal to 10.

#list of integers
l=list(map(int,input().split()))

#sum
sum=0

for i in l:
    if i>=10:
        sum+=i
print('The sum of integers which grater or equal to 10 is : ',sum)