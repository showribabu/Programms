l=[int(x) for x in input().split()]

#peak element ..
p_count=0

for i in range(len(l)):
    #check the  neighbours... 
    
    #at 0 index 
    if i==0 and l[i]>l[i+1]:
        p_count+=1
        print(l[i])
    
    #at n-1 index...
    if i==len(l)-1 and l[i]>l[i-1]:
        p_count+=1
        print(l[i])

    
    #remian ...
    if i>1 and i<len(l)-1 :
        if l[i-1] < l[i] > l[i+1]:
            p_count+=1
            print(l[i])

    
    
print('The count of peak elemnts is:',p_count)

            
    