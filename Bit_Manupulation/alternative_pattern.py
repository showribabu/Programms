#check the given number has alternative patterns or not...

'''
ex : 10101010 .....  (Because we have only 2 digits here....)

ex2 : 010101010101....


'''

'''

for that :
step 1: make the right shift by 1 ()>>1)  the we can like

n=101010
>>1
010101 
now we can check with the exor(^) operator
If all are 11111 then it is the alternative pattern ...
 
 (How to check that all are sets.....1111)
 
 now we can **** & with next number ******

'''

n=int(input('Enter n for check alternative pattern:'))

t=n ^ (n>>1)

# may be alll sets ...111111...

if ( t & t+1 ) ==0:
    print('Alternative pattern')
else:
    print('nOt a Alternative pattern')

