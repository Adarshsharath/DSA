class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        minval = min(nums)
        maxval = max(nums)
        minidx = -1
        maxidx = -1
        if len(nums) == 1:
            return 1
        if len(nums) == 2:
            return 2
        for i in range(len(nums)):
            if nums[i] == minval:
                minidx = i
            if nums[i] == maxval:
                maxidx = i
        n = len(nums)
        left = max(minidx, maxidx) + 1
        right = n - min(minidx, maxidx)

        one_each = min(
            minidx + 1 + n - maxidx,
            maxidx + 1 + n - minidx
        )

        return min(left, right, one_each)
