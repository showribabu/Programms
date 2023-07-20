#reverse of an array 


n=int(input())
l=[]
for i in range(n):
    l.append(int(input()))

print(l)


#reverse by use 2 pointer approach...
left=0
right=len(l)-1

while left<right:
    l[left],l[right]=l[right],l[right]
print(l)

