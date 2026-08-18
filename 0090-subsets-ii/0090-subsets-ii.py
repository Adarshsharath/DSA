class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        result = []

        def fun(idx, sub):

            if idx == len(nums):
                result.append(sub[:])
                return

            sub.append(nums[idx])
            fun(idx + 1, sub)
            sub.pop()

            while idx + 1 < len(nums) and nums[idx] == nums[idx + 1]:
                idx += 1

            fun(idx + 1, sub)

        fun(0, [])

        return result