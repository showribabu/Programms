s1=input()
s2=input()

s1=list(s1)
s2=list(s2) 

#by sort the 2 strings we can check the s1  in s2 or not.....

#find permutations of s1 and then find that are aviilable in s2 or not... 

s1.sort()
s2.sort()

s1="".join(x for x in s1)
s2="".join(x for x in s2)
if s1 in s2:
    print('Permutation of s1 is present in s2')
    