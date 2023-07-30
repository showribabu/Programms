# knuth moris is the one of the of the best algorithm for pattern matching in a given string

#naive approack
#knuth moris
#rabin karp

#knuth moris is having  : Stirng , pattern(string which used to search) 

#we need to find the *** LPS table ****  for the pattern .

'''

def compute_lps(pattern):
    m = len(pattern)
    lps = [0] * m  # Initialize the LPS table with all zeros

    j = 0  # Length of the previous longest prefix suffix

    for i in range(1, m):
        while j > 0 and pattern[i] != pattern[j]:
            j = lps[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
        lps[i] = j

    return lps

def kmp_search(text, pattern):
    n = len(text)
    m = len(pattern)
    lps = compute_lps(pattern)
    j = 0  # Index for pattern[]

    for i in range(n):
        while j > 0 and text[i] != pattern[j]:  #if not match at j=0 then i++  .... 
            j = lps[j - 1]

        if text[i] == pattern[j]:
            j += 1
            #i =i+1 in loop...

        if j == m:
            print("Pattern found at index", i - m + 1)
            j = lps[j - 1]


text = input("Enter the text: ")
pattern = input("Enter the pattern to be searched: ")
kmp_search(text, pattern)

'''


#now cose it..
def lps_tab(pattern):
    m=len(pattern)
    lps=[0]*m
    
    
    j=0
    for i in range(1,m):
    #cond 1
        while j>0 and pattern[i]!=pattern[j]:
            j=lps[j-1]
    #cond2..
        if pattern[i]==pattern[j]:
            j+=1
        
    #update lps..
        lps[i]=j
    print(lps)
    return lps

def search(s,pattern):
    n=len(s)
    m=len(pattern)
    lps=lps_tab(pattern)
    j=0
    for i in range(n):
        
        #cond 1
        while j>0 and s[i]!=pattern[j]:
            j=lps[j-1]
        #cond2..
        if s[i]==pattern[j]:
            j+=1
        
        if j==m:
            print('The index :',i-j+1)
            j=lps[j-1]
    
            
        


s=input('Enter String:')
p=input('Enter Pattern:')
search(s,p)