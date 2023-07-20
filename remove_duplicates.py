# remove the duplicate elements

n=int(input())
l=[]
for x in range(n):
    l.append(int(input()))
print(l)
l=list(set(l))
print(l)