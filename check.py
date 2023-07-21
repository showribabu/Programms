n,m=[int(x) for x in input().split()]

l=[0]*n
print(l)

for i in range(m):
    a,b,v= [int(x) for x in input().split()]
    print(i,'--->',a,b,v)
    if 0<=a-1 <=n and 0<=b-1<=n :
        for j in range(a-1,b):
            l[j]=l[j+1] + v 
            print('Good :',j)
            print(l[j])
            

print(max(l))

# n, m = map(int, input().split())
# l = [0] * n

# for i in range(m):
#     a, b, v = map(int, input().split())
#     if 1 <= a <= n and 1 <= b <= n:
#         for j in range(a - 1, b):
#             l[j] += v

# print(max(l))
