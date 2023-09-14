
class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        j=0 #next zero...
        left=0 #previous zero..
        maxx=0
        tmax=0
        i=0

        n=len(nums)
        while i<n:
            if nums[i]==1:
                tmax+=1
            
            if nums[i]==0:
                j=i+1
                while  j<n and nums[j]!=0:
                    #find the next zero index
                    tmax=j-left+1
                    j+=1
                #now window with maxsize at tmax..
                #update...
                left=i+1
                i=j-1
                
                
            #changed pointers for next window..
            maxx=max(maxx,tmax)
            print(i,'--''maximum--',maxx)
            i+=1
        
        return max(maxx-1,0)


s=Solution()
print(s.longestSubarray([1,0,0,0,0]))


        