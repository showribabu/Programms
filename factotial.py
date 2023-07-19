#6. Write a program that takes a number as input and outputs its factorial.
#using linear recursion...
import time
def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
        
print('Using the Linear recursion')    
t1=time.time()
n=int(input('Enter number:'))
print(fact(n))
t2=time.time()
print('%.2f'%(t2-t1))

#using loop
print('Using Loop')
t3=time.time()
n=int(input())
f=1
for i in range(1,n+1):
    f=f*i
print(f)
t4=time.time()
print('%.2f'%(t4-t3))
