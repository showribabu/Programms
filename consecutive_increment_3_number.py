#check the 3 continuous incrementing adjacent values existed or not
def check(l,n):
    for x in range(n-2):
        if(l[x+1]==l[x]+1 and l[x+2]==l[x]+2):
            return True
    return False
    

n=int(input())#array size
l=[]
for i in range(n):
    l.append(int(input()))
# print(l)
#calling the function check()
if n!=0 : 
    print(check(l,n))
else:
    print('Please enter correct value')
