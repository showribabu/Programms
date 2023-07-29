#take all possible permutations and find the larger one...

def perm(s):
    if len(s)=='':
        return []
    if len(s)==1:
        return [s]
    
    perms=[]
    for i in range(len(s)):
        curr=s[i]
        remain=s[i+1:]+s[:i]
        for xy in perm(remain):
            perms.append(curr+xy)
    return perms
s=input()
print(perm(s))

#the all possible permutatu=ions are ....n! 
# ex: len(s) =4...--> 24 posssibilites. 
