#rotation of array..

def rev(l,s,e):
    # print(s,e)
    start=s
    end=e
    # print(start,s)
    while start<end:
        l[start],l[end]=l[end],l[start]
        start+=1 
        end-=1 
def rotate(l,n,i):
    rev(l,0,n-1)
    rev(l,0,i-1)
    rev(l,i,n-1)
    print(l,'---->For iteration :')
    

n=int(input('Enter size:'))
l=[]
for x in range(n):
    l.append(int(input()))
print(l)

temp=l.copy()
for z in range(n):
    rotate(temp,n,1)
    
# rotation of the array..


