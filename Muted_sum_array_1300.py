class Solution(object):
    def findBestValue(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        s=0
        minn=max(arr)
        mini=arr[0]
        for i in range(len(arr)):
            l1=arr[:]
            for j in range(len(l1)):
                if arr[i]< l1[j]:
                    l1[j]=arr[i]
            s=sum(l1)
            print(s)
            diff=abs(target-s)
            if minn>=diff:
                minn=diff
                mini=arr[i]
        return mini
     
s=Solution()
print(s.findBestValue([60864,25176,27249,21296,20204],56803))       



                
