#9. Write a program that takes a string as input and outputs whether it is a palindrome.

#reverse function..
def rev(str):
    #reverse by use 2 pointer technique....
    f=0
    l=len(str)-1
    while f<l:
        str[f],str[l]=str[l],str[f]
        f+=1
        l-=1
    return str
        
str=input('Enter string:(case insensitive)')
str=str.lower()
# print(str)
temp=list(str)
print("Palindrome") if(temp==rev(list(str))) else print("Not Palindrome")
