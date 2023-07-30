class Solution(object):
    @classmethod
    def rev(cls,nums,s,e):
        while s<=e:
            nums[s],nums[e]=nums[e],nums[s]
            s+=1
            e-=1

    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums)>1 and k>0:
            Solution.rev(nums,0,len(nums)-1)
            Solution.rev(nums,0,(k-1)%len(nums))
            Solution.rev(nums,k%len(nums),len(nums)-1)


se=Solution()
nums=[int(x) for x in input().split()]
k=int(input())
se.rotate(nums,k)
print(nums)