#4. Write a program that takes a string as input and outputs the number of vowels in the string.
str=input('Enter string:')

v=['a','e','i','o','u']

#convert string to lower case
str=str.lower()
c=0
for i in str:
    if i in v:
        c+=1
print('The vowels in the string is:%d'%c)
        