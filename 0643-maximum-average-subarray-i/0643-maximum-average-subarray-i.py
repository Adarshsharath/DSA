class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        left = 0
        maxA = float('-inf')
        sums = 0

        for right in range(len(nums)):
            sums += nums[right]

            if right - left + 1 == k:
                maxA = max(maxA, sums / k)

                sums -= nums[left]
                left += 1

        return maxA