#take list and element to search 

l=[int(x) for x in input().split()]
print(l)
x=int(input())
f=0
for i in range(len(l)):
    if l[i]==x:
        print('Elememt Found at',i)
        f=1
        break

if f==0:
    print('Element Not found')
