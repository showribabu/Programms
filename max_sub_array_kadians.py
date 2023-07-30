l=[int(x) for x in input().split()]

# max value of array...



"""

''' Without any specific K'''

max_so_far=l[0]
max_end=0

for i in range(len(l)):
    max_end+=l[i] 
    if max_end <0:
        max_end=0
    if max_so_far<max_end:
        max_so_far=max_end
        
print('The max_so_far is:',max_so_far)


"""

""" With specific K """

#max subarray 
k=int(input())

""" Slinding window protocol"""

ind=0
max_so_far=0

for i in range(len(l)-k+1):
    sum=0
    for j in range(i,i+k):
        sum+=l[j]
    if max_so_far <sum:
        max_so_far=sum
        ind=i 

print('The max value from the array is: ',max_so_far,'Due to elements:')
for j in range(ind,ind+k):
    print(l[j],end=' ')
        
        
            
        
