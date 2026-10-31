class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        first = {0: -1}          
        prefix_sum = 0
        ans = 0

        for right, num in enumerate(nums):
            prefix_sum += 1 if num == 1 else -1

            if prefix_sum in first:                  
                ans = max(ans, right - first[prefix_sum])
            else:
                first[prefix_sum] = right            

        return ans