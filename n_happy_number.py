'''
Challenge Question: Nth Happy Number

A happy number is a number defined by the following process: Starting with any positive integer

replace the number by the sum of the squares of its digits, and repeat the process until the number becomes 1 or 
enters a cycle that includes 4, 16, 37, 58, 89, 145, 42, or 20. If the number becomes 1, it is a happy number.

Write a function nth_happy_number(n) that takes an integer n as input and returns the nth happy number.


'''

''' 
#happy number ir not....
def happy_number(nn):
    v=set()
    
    #n not equal to 1 or not visited ---then only iterate and find sum of square
    while nn!=1 and nn not in v:
        v.add(nn)
        nn=sum(int(num)**2 for num in str(nn))
    return nn==1 


#nth happy number
def nth_happy_number(n):
    count=1
    number=1
    while count<=n:
        if happy_number(number):
            # print(number)
            count+=1
        number+=1
    return number-1

n=int(input('Enter n th number you want:'))

print(nth_happy_number(n))
        
        
    
    

        '''
        
def is_happy(num):
    visited = set()

    while num != 1 and num not in visited:
        visited.add(num)
        num = sum(int(digit) ** 2 for digit in str(num))

    return num == 1


def nth_happy_number(n):
    count = 0
    number = 1

    while True:
        if is_happy(number):
            count += 1

        if count == n:
            return number

        number += 1


n = int(input('Enter the n-th number you want: '))
print(f"The {n}th happy number is: {nth_happy_number(n)}")
