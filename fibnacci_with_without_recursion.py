#fibnacci with and without recursion....

#fibnacci without recursion
n1=0
n2=1 
n=int(input())

if n==0:
    print(n1)
if n==1:
    print(n1,n2)
if n>=2:
    print(n1,n2,end=' ')
    for i in range(2,n):
        temp=n1+n2
        print(temp,end=' ')
        n1=n2
        n2=temp


#fibnacci with recursion  
def fib(x):
    if x==0:
        return 0
    elif x==1 or x==2:
        return 1
    else:
        return fib(x-1)+fib(x-2)
print()
for i in range(n):
    print(fib(i),end=' ')


    
    
    