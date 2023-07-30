#finding the one missng element within the range 0 to n: 

#by use [n =(n*(n+1))/2]

'''
Ex: [0,2,3]

l->length
l=(l*(l+1))/2

now subtract each one from it and thenfnally we can have result with us....


'''

l=[int(x) for x in input().split()]
sum=(len(l)*(len(l)+1))//2
for i in l:
    sum-=i 
print(sum) 
