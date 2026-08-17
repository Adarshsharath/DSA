class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        mp = defaultdict(int)

        for i in nums:
            mp[i]+=1

        ans = []

        for key,val in mp.items():
            if val == 1:
                ans.append(key)
        return ans