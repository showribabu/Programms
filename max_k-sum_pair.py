class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        #0step  :sort the given code and perform operarations..
        #1 step :i =0 and j=n-1 
        #2 step :if nums[i]+nums[j]>k: then j-=1
        #3 step :if nums[i]+nums[j]<k: then i+=1
        #4 else : equlal then update both..
        
        i=0
        c=0
        j=len(nums)-1
        nums.sort()
        while i<j:
            if nums[i]+nums[j]>k:
                j-=1
            elif nums[i]+nums[j]<k:
                i+=1
            elif nums[i]+nums[j]==k:
                c+=1
                i+=1
                j-=1
        return c
                
                
                
         
        
s=Solution()
print(s.maxOperations([3,1,3,4,3],6))


                
'''
        c=0
        i=0
        n=len(nums)
        while i<n:
            j=i+1
            while j<n:
                if nums[i]+nums[j]==k:
                    c+=1
                    nums.remove(nums[i])
                    nums.remove(nums[j-1])
                    i=0
                    j=1
                    n=len(nums)
                    continue
                
                j+=1
            i+=1
        return c
'''
        # while i<n and i<j:
        #     f=0
        #     j=n-1
        #     if nums[i]+nums[j]==k:
        #         c+=1
        #         f=1
        #         nums.remove(nums[i])
        #         nums.remove(nums[j])
        #         n=len(nums)


'''
        while i<n-1:
            j=n-1
            while i<j:
                if nums[i]+nums[j]==k:
                    c+=1
                    nums.remove(nums[i])
                    n=len(nums)
                    j=n-1
                    nums.remove(nums[j])
                    n=len(nums)
                j-=1            
            i+=1
        
        return c
'''
        

           

                



        