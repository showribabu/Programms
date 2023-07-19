"""
3. Write a program that takes an list of integers as input and outputs the sum of all the even numbers in the list.
"""

#take list of integers as input
l=[int(x) for x  in input().split()]
# print(l)
sum=0
for i in l:
    if i%2==0:
        sum+=i 
print(sum)
