class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left = 0
        sums = 0
        ans = float('inf')

        for right in range(len(nums)):
            sums += nums[right]

            while sums >= target:
                ans = min(ans, right - left + 1)

                sums -= nums[left]
                left += 1

        return 0 if ans == float('inf') else ans