def perm(l):
    if len(l)==0:
        return []
    if len(l)==1:
        return [l]
    
    #if more than 1 then n! ....
    perms=[]
    for i in range(len(l)):
        curr=l[i]
        # print('Current :--->',curr ,end=' ')
        remain=[x for x in l[i+1:]]
        remain.extend([x for x in l[:i]])
        # print(' --- --  Remain :--->',remain)
        for xy in perm(remain):
            dd=[]
            dd.append(curr)
            dd.extend(xy)
            # print('dd ---> ',dd)
            perms.append(dd)
        # print('list : perms---->',perms)
    return perms

l=[int(x) for x in input().split()]
print(perm(l))
    