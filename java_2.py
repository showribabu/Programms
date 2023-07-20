# find out the missing  of  a num 

n=int(input())
l=[]
for i in range(n):
    l.append(int(input()))
print(l)

#finding the miss value

nn=int(input('Enter n:'))

l2=l[:nn]

l2.sort()

first=l2[0]

for i in range(1,len(l2)):
    next=l[first]+1 
    if next!=l[i]:
        print(next)
        break
    else:
        next +=1 
        
    
    
    
    

