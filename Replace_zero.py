#function return the required array 

def zeroReplace(l,n):
    #repalce zero ->largest odd to the right of each zero
    # if  no odd value to the right zero leave it as zero
    print('Function called')
    for i in range(n-1):
        if(l[i]==0):
            j=i+1
            print(l[j])
            max=0
            while(j<n and l[j]!=0):
                if(l[j]%2==1):
                    if max<l[j]:
                        max=l[j]
                j=j+1
            if max!=0:
                l[i]=max
    print(l)
    return l
                    

#read size of array and elements
n=int(input())
# print('heiii',n)
l=[]
for i in range(n):
    l.append(int(input()))
print(l)
#now pass array to the function...
print(zeroReplace(l,n))