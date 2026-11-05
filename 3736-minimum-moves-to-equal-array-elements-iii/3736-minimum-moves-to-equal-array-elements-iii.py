class Solution:
    def minMoves(self, nums: List[int]) -> int:
        x =  max(nums)
        count = 0
        for i in nums:
            count += (x-i)
        return count
