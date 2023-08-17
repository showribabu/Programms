class Solution(object):
    def fact(self,f):
        if f==0 or f==1:
            return 1
        else:
            ff=f*self.fact(f-1)
            # print(ff)
            return ff
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        l=[]
        for i in range(numRows):
            d=[]
            for j in range(i+1):
                r=self.fact(i)//(self.fact(j)*(self.fact(i-j)))
                print(r)
                d.append(r)
            l.append(d)
        return l

s=Solution()
print(s.generate(5))