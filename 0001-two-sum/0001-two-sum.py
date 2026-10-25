class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # left = 0
        # nums = sorted(nums)
        # right = len(nums)-1
        # while left < right:
        #     sums = nums[left] + nums[right]
        #     if sums == target:
        #         return [left,right]
        #     elif sums < target:
        #         left+=1
        #     else:
        #         right-=1
        hashmap = {}
        for i in range(len(nums)):
            val = target-nums[i]
            if val in hashmap:
                return [hashmap[val],i]
            hashmap[nums[i]] = i 
            # print(hashmap)