class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        ans =nums[0]
        maxans = nums[0]

        for i in range(1,len(nums)):
            ans = max(nums[i],ans+nums[i])
            maxans = max(maxans,ans)
        
        ans = nums[0]
        minans = nums[0]

        for i in range(1,len(nums)):
            ans = min(nums[i],ans+nums[i])
            minans = min(minans,ans)

        if maxans<0:
            return maxans

        s = sum(nums)-minans

        return max(s,maxans)
            
            