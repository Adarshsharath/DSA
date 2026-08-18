class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        mp = defaultdict(int)

        left = 0

        right = k-1

        while(right<len(nums)):
            for i in range(left,right+1):
                mp[nums[i]] += 1
            
            right+=1
            left+=1
        if k == len(nums):
            return max(nums)
        maxnum = -1
        for key,val in mp.items():
            if val == 1 and key > maxnum:
                maxnum = key


        return maxnum
