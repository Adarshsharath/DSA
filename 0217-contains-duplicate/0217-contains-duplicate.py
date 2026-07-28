from collections import defaultdict
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        mp = defaultdict(int)
        for i in nums:
            mp[i] +=1
            if mp[i] > 1:
                return True
        return False