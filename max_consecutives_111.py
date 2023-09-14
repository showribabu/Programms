def longestOnes(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        n=len(nums)
        
        ones=0
        i=0
        x=0
        while i<k:
            if nums[x]==0:
                i+=1
                print('if condition')
            ones+=1
            x+=1
        
        
        max_ones=ones
        start=0
        end=ones+1
        print('Hiii',max_ones)

        while end<n:
            if nums[start]==1:
                ones-=1
                start+=1
            if nums[end]==1:
                ones+=1
                end+=1
            max_ones=max(ones,max_ones)
        return max_ones

print(longestOnes([1,1,1,0,0,0,1,1,1,1,0],2))