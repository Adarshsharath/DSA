class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        sums = nums[0]
        ans = []
        ans.append(nums[0])
        for i in range(1,len(nums)):
            sums+=nums[i]
            ans.append(sums)
        return ans
