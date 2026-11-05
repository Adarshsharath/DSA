class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums = sorted(nums)

        x = nums[len(nums)//2]

        count = 0

        for i in nums:
            if x>i:
                count += (x-i)
            else:
                count += (i-x)
        return count