class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        i = 0
        j = 0
        k = 0
        p = 0
        first = False
        second = False
        third = False

        while i + 1 < len(nums) and (nums[i] < nums[i+1]):
            i+=1
            j+=1
        if j > 0:
            first = True
        while i + 1 < len(nums) and (nums[i]>nums[i+1]):
            i+=1
            k+=1
        if k > 0:
            second = True
        while i + 1 < len(nums) and (nums[i]<nums[i+1]):
            i+=1
            p+=1
        if p > 0:
            third = True 
        return first and second and third and i == len(nums)-1