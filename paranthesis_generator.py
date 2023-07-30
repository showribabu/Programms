'''
n=3
-- 3 * 2 =6 total...

generate all possible paranthesis combinations..

.....'((()))','(())()','()()())'....}

'''

def paranthesis(n,l,op,cp,s):
    #op-->open paranthesis
    #cp-->closing paranthesis
    #n-->number for op and closing paranthesis
    #s-->string for the permutation..
    #l->fianl result..
    
    if (op==n and cp==n):
        l.append(s)
        return l
    
    if op<n:
        paranthesis(n,l,op+1,cp,s+'(')
    if cp<n:
        paranthesis(n,l,op,cp+1,s+')')
    
    return l 
        
    

n=int(input())

print(paranthesis(n,[],0,0,''))



