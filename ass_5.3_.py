n=int(input())
l1=[]
for i in range(n):
    l1.append(int(input()))

l1.sort()

l2=[]
for i in range(n):
    l2.append(int(input()))
l2.sort()


#union

l3=[]
l3=l1[::]
for i in l2:
    if i not in l3:
        l3.append(i)

print('union of 2 sets : ',l3)

#intersection
l4=[]
for i in l1:
    if i in l3:
        l4.append(i)

print('intersectio of 2 processort',l4)




