class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        mid = 0
        right = len(nums)-1
        while mid <= right:
            if nums[mid] == 0:
                temp = nums[left]
                nums[left] = nums[mid]
                nums[mid] = temp
                left += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            elif nums[mid] == 2:
                temp = nums[right]
                nums[right] = nums[mid]
                nums[mid] = temp
                right -= 1

            

                