#Odd even numbers seperativley

n=int(input('Enter size:'))
l=[]
for x in range(n):
    l.append(int(input()))
print(l)

odd=[]
even=[]
for i in l:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
l.clear()

min_len = min(len(odd), len(even))

for i in range(min_len):
    l.append(odd[i])
    l.append(even[i])

# Append any remaining elements from the longer list
if len(odd) > min_len:
    l.extend(odd[min_len:])
elif len(even) > min_len:
    l.extend(even[min_len:])

print("Alternating list:", l)

        
        
        
        
        