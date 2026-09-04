class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        instability = 0
        minS = 2**31-1
        mini = -1

        for i in range(len(nums)):
            if i == 0:
                instability = nums[i] -min(nums)
            elif i == len(nums):
                instability = max(nums) - nums[i]

            else:
                instability = max(nums[0:i+1]) - min(nums[i:])

            if instability<=k and instability<minS:
                minS = instability
                mini = i
                return mini

        
        return -1