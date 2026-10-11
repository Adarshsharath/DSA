class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        idx = 1
        n = len(nums)
        sums = 0 
        for i in nums:
            if n%idx == 0:
                sums += i*i
            idx+=1
        return sums
