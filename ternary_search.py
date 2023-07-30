l=[int(x) for x in input().split()]
x=int(input('Enter x:'))

l.sort()
low=0
high=len(l)-1
f=0
while low <= high:
    m1=low +(high-low)//3
    m2=high-(high-low)//3
    if x==l[m1]:
        print('x found at',m1)
        f=1
        break
    elif x==l[m2]:
        print('x found at',m1)
        f=1
        break
    elif x<l[m1]:
        high=m1-1
    elif x>l[m2]:
        low=m2+1
    
    else:   #  l[m1]<x<l[m2]
        low=m1+1
        high=m2-1
    
    

if f==0:
    print('NOt found')

    


  
    