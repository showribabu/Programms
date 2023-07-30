#The strings have same set of characteres.../same frequency

s1=input()
s2=input()

#sort...
'''
s1=list(s1)
s1.sort()
s2=list(s2)
s2.sort()
print(s1,s2) '''


# frequency count. 

d1={}
for i in s1:
        d1[i]=s1.count(i)
d2={}
for i in s2:
        d2[i]=s2.count(i)


# if s1 == s2:
if d1==d2:
    print('Anagram')
else:
    print('Not anagram')

