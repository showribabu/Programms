#first repeat element..

n=int(input('Enter size:'))
l=[]
for x in range(n):
    l.append(int(input()))
print(l)

check=[]
for i in l:
    if i not in check:
        check.append(i)
    else:
        print(i,'The element repeated first')
        break
