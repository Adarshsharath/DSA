class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:

        nums.sort()

        ans = float("inf")

        for left in range(len(nums) - k + 1):

            difference = nums[left + k - 1] - nums[left]

            ans = min(ans, difference)

        return ans