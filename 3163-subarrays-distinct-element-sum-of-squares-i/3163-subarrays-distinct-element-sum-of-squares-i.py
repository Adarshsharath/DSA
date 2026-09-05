class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        ss = 0
        for i in range(len(nums)):
            s = set()
            s.add(nums[i])
            print(s)
            for j in range(i,len(nums)):
                s.add(nums[j])
                ss += len(s)**2
        return ss
