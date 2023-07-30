# decimal to base  k,
d=int(input())
k=int(input())
result=''

temp=d


while d>0:
    result=str(d%k)+result
    d=d//k
print(result)