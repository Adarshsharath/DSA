class Solution:
    def getPermutation(self, n: int, k: int) -> str:

        def nextPermutation(nums):
            length = len(nums)

            i = length - 2

            while i >= 0 and nums[i] >= nums[i + 1]:
                i -= 1

            if i >= 0:
                j = length - 1

                while nums[j] <= nums[i]:
                    j -= 1

                nums[i], nums[j] = nums[j], nums[i]

            nums[i + 1:] = reversed(nums[i + 1:])

        nums = list(range(1, n + 1))

        for _ in range(k - 1):
            nextPermutation(nums)

        return ''.join(map(str, nums))