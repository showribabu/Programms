class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        l=s.split(' ')
        # print(l)
        l1=[]
        for i in l:
            if i!='':
                l1.append(i)
        # print(l1)
        
        l1.reverse()
        # return ' '.join(l1)
        return l1

s=Solution()
print(s.reverseWords(" HELLO WORLD  "))