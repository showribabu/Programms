# nth min value from the 

s=int(input('Enter array size:'))
n=int(input('Enter nth value:'))
l=[]
for x in range(s):
    l.append(int(input()))
print(l)

#here if array have duplicate values..if give wrong ...remove duplicates also...

m=list(set(l))  #data sorted and eliminates duplicates..

print(m)
if 1<= n <len(m):
    print(m[n-1] ,'is nth min value...')
    