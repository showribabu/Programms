n=int(input())

l=[]
for i in range(n):
    l.append(int(input()))
    
#duplicate by frequncy 
dict={}

for i in range(n):
    dict[l[i]]=l.count(l[i])
    #frequency....
    # if l.count(l[i])>1:
    #     print('duplicate:',l[i])
    
#values..
# print(dict.items())

for k,v in dict.items():
    # print(k,v)
    if v>1:
        print(k)

