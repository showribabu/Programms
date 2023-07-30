#pop the top one and check with input one..

s=input('ENTER STRING :')
l=[]
f=0
for i in s:
    if i=='(' or i=='[' or i=='{' :
        l.append(i)
    elif i==')' or i==']' or i=='}':
        if l!=[]:
            l.pop()
        else:
            f=1
            # print('Invalid')
            break
    # print(l)

if l==[] and f==0:
    print('Equal paranthesis')
else:
    print('Not balance')
    