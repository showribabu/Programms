#Bubble sort concept is used...
#or  2 pointers  concepts is used

l=[int(x) for x in input().split()] 
print(l)
ll=0
r=0
n=len(l)
while r<n:
    # if l[r]==0:
    #     r+=1      #something...
    
    if l[r]!=0:  
        l[ll],l[r]=l[r],l[ll]
        ll+=1
    r+=1

print(l)
        
    
      