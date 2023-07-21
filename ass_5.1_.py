n=int(input())

l=[]
for i in range(n):
    l.append(int(input()))

#not smaller than its neighbour   2 '4' 3

#if test cases there then we need to change more conditions..

f=0
start=1
if len(l)==1:
    print(l[i])
    
if len(l)==2:
    start=2
    print(l[i]) if l[i]>l[i+1] else print(l[i+1])

for i in range(start,n-1):
    if l[i]>l[i+1] and l[i]>l[i-1]:
        print(l[i])
        f=1
        break
if f==0:
    print('No neighbours found')
    