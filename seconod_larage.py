#7. Write a program that takes a list of integers as input and outputs the second-largest number in the list.

#here second large possible on;y if the list having at least 2 elements

def bubb(l):
    for i in range(len(l)):
        for j in range(0,len(l)-i-1):
            if l[j]>l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]
    return l
    
    


l=list(map(int,input().split()))
if len(l)>=2:
    #sort
    print(bubb(l))
    
    #print second large -2 index
    print('The second large value:',l[-2])
else:
    print('Less values given !! not possible to print 2nd largest value!!!')