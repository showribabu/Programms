#5. Write a program that takes a list of strings as input and outputs the longest string in the list .

#list of stsrings

l=list(input().split())
x=[]
for i in l:
    x.append(len(i))
print(l)
print(max(x))