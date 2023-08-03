
'''

a=2 #010
b=5 #111

print(a & b)
print(a | b)
print(a ^ b)

'''


#Check power of 2 or not

def check_power2(n):
    #***********previous..number *********
    t=n & (n-1)
    
    if t==0:
        return True
    else:
        return False
        

n=int(input('enter n:'))
print(check_power2(n))



#swaping of 2 numbers ...

def swap(a,b):
    #1
    a=a+b
    b=a-b
    a=a-b
    print(a,b)
    a,b=b,a
    #2 --->Binary operator effective
    a=a^b
    b=a^b
    a=a^b
    print(a,b)
    #3
    a,b=b,a
    a=a*b
    b=a//b
    a=a//b
    print(a,b)

a,b=[int(x) for x in input('Enter a,b:').split()]
swap(a,b)
