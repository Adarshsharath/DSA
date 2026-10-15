
import math

class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:

        def nextPermutation(nums):
            n = len(nums)

            i = n - 2
            while i >= 0 and nums[i] >= nums[i + 1]:
                i -= 1

            if i >= 0:
                j = n - 1
                while nums[j] <= nums[i]:
                    j -= 1

                nums[i], nums[j] = nums[j], nums[i]

            left = i + 1
            right = n - 1

            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

            return nums

        nums.sort()
        ans = [nums.copy()]

        for i in range(math.factorial(len(nums)) - 1):
            nextPermutation(nums)
            ans.append(nums.copy())

        return ans


