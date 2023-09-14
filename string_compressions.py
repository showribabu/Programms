class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """

        s=[]
        n=len(chars)
        if n==1:
            return 1
        i=0
        while i<n:
            c=1
            j=min(i+1,n-1)
            while j<n and chars[i]==chars[j]:
                c+=1
                j+=1
            
            if c==1:
                s.append(chars[i])
            elif c>1:
                s.append(chars[i])
                s.append(str(c))
                i=j
                continue
            
            i+=1
        chars=str(''.join(s))
        print(chars)
        return len(chars)
    



s=Solution()
print(s.compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]))

    



            


        