# find sum of digits and make sum into single digit if sum>9 again finf the sum 


def sumofdigits(n):
    sum=0
    while n>0:
        sum=sum+(n%10)
        n=n//10
    return sum
        


n=int(input('Enter n:'))
r=sumofdigits(n)
while r>9:
    # print(r,'-->',end=' ')
    r=sumofdigits(r)
print(r)
    
    
    