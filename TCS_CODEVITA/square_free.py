import math
def perfect_square(x):
    #check perfecr suare or not.....
    r=math.sqrt(x)
    
    return (r*r)==x
    
    

def square_free(y):
    #the number can't devided with the perfect squares.
    for z in range(2,y):
        if y%z==0 and perfect_square(z):
            return False
    return True


n=int(input('Enter N:'))
count=0

for i in range(2,n):
    if n%i==0 and square_free(i):
        count+=1

print('Count is:',count)
    
    