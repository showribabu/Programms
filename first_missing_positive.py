#first missing positive...

''''
+ve -> 1,2,3... 

Ex: [1,2,3] -->4

[2,4,5] --->1

'''

l=[int(x) for x in input().split()]

n=len(l)

i=1
l=set(l) #here set() because if there is any duplicate the i values...
while i<n+2:
    if i not in l:
        print(i)
        break
    i+=1

