class Solution:
    def maxSubArray(self,nums):
        curr = nums[0]
        max_sum = nums[0]

        for i in range(1, len(nums)):
            curr = max(nums[i], curr + nums[i])
            max_sum = max(max_sum, curr)

        return max_sum
        