class Solution(object):
    def triangularSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=[]
        l.append(nums)
        for i in range(len(nums)):
            d=[]
            for j in range(len(nums)-i-1):
                r=l[i][j]+l[i][j+1]
                if r>=10:
                    d.append(r%10)
                else:
                    d.append(r)
            if d!=[]:
                l.append(d)
        print(l)
        v=l[-1]
        for i in v:
            return i
s=Solution()
print(s.triangularSum([1,2,3,4,5]))