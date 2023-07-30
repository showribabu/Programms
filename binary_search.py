l=[int(x) for x in input().split()]
x=int(input('Enter x:'))

l.sort()
low=0
high=len(l)-1
f=0
while low <= high:
    mid=low +(high-low)//2
    if l[mid]==x:
        f=1
        print('x found at',mid)
        break
    elif x>l[mid]:
      low=mid+1
    elif l[mid]>x:
        high=mid-1

if f==0:
    print('NOt found')

    


  
    