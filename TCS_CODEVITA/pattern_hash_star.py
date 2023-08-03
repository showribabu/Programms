'''
The given program represent that :

{#,*,.} --> are 3 chars avilabele

#-> represents galaxy

*,. --> used to represents vowels in 3X3 matrix. 

now print the #for galaxy and character for the vowel from the given data 

N->Number of columns.

'''
n=int(input('Enter no.of columns'))

#here rows are fixed because the vowels represented in 3X3 matrix...in the part of the n columns

l=[]
for i in range(3):
    d=[]
    for j in range(n):
        d.append(input('Enter for '+str(i)+' row and '+str(j)+' column ::'))
    l.append(d)
    
print(l)

#now check that galaxy and the vowels ...
i=0
while i<n:
    #check the columns is galaxy or not
    if l[0][i]=='#' and l[1][i]=='#' and l[2][i]=='#':
        print('#',end=' ')
        i=i+1
    
    #now check the 3X3 matrix..
    else:
        #for 3X3 =9 elements.... a,b,c,a1,b1,c1,a2,b2,c2 
        a=l[0][i];b=l[0][i+1];c=l[0][i+2]
        a1=l[1][i];b1=l[1][i+1];c1=l[1][i+2]
        a2=l[2][i];b2=l[2][i+1];c2=l[2][i+2]
        
        #now check for vowels...
        
        #A
        if a=='.' and b=='*' and c=='.' and a1=='*' and b1=='*' and c1=='*' and a2=='*' and b2=='.' and c2=='*':
            print('A',end=' ')
            i=i+3
        elif a=='*' and b=='*' and c=='*' and a1=='.' and b1=='*' and c1=='.' and a2=='*' and b2=='*' and c2=='*':
            print('I', end=' ')
            i=i+3
        elif a=='*' and b=='*' and c=='*' and a1=='*' and b1=='*' and c1=='*' and a2=='*' and b2=='*' and c2=='*':
            print('E',end=' ')
            i=i+3
        elif a=='*' and b=='*' and c=='*' and a1=='*' and b1=='.' and c1=='*' and a2=='*' and b2=='*' and c2=='*':
            print('O',end=' ')
            i=i+3
        elif a=='*' and b=='.' and c=='*' and a1=='*' and b1=='.' and c1=='*' and a2=='*' and b2=='*' and c2=='*':
            print('U',end=' ')
            i=i+3
        else:
            i=i+1
            continue
        
        

        
        

