class Solution:
    def search(self, nums: list[int], target: int) -> int:

        def binsearch(nums, left, right, target):
            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    return mid

                elif nums[mid] < target:
                    left = mid + 1

                else:
                    right = mid - 1

            return -1
        pivot = 0

        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                pivot = i
                break

        if pivot == 0:
            return binsearch(nums, 0, len(nums) - 1, target)

       
        if nums[0] <= target <= nums[pivot - 1]:
            return binsearch(nums, 0, pivot - 1, target)

        return binsearch(nums, pivot, len(nums) - 1, target)