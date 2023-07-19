#armstrong number or not with in the range
def arm(n):
    l=len(str(n))
    temp=n
    sum=0
    while n>0:
        sum=sum+((n%10)**l)
        n//=10
    print("armstrong:%d"%temp) if sum==temp else print("Not armstrong:%d"%temp)



a=int(input('Enter start range:'))
b=int(input('Enter the final range:'))


for x in range(a,b+1):
    arm(x)