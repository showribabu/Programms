class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l=[]
        for i in s:
            if i not in l:
                l.append(i)
        x=[]
        for j in l:
            x.append(s.count(j))
        f=0
        for i in range(len(x)):
            for j in range(i+1,len(x)):
                if x[i]!=x[j]:
                    f=1
                    break
        if f==1:
            return 'false'
        else:
            return 'true'
        
        
        
      
     
s=Solution()
print(s.repeatedSubstringPattern("abcabcabcabc"))