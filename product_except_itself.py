class Solution(object):
    def mul(self,l):
        if len(l)==0:
            return 1
        else:
            p=1
            for k in l:
                p=p*k
            return p
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answer=[]
        n=len(nums)
        for i in range(n):
            pre=self.mul(nums[:i])
            suf=self.mul(nums[i+1:n])
            print(pre*suf)
        # return pre*suf
    
s=Solution()
print(s.productExceptSelf([1,2,3,4]))
