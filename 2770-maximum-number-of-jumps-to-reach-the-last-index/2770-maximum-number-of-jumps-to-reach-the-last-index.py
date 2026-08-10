class Solution:    
    def maximumJumps(self, nums, target):
        dp = {}
        def fun(idx):
            if idx == len(nums) - 1:
                return 0
            if idx in dp:
                return dp[idx]
            ans = -1
            for j in range(idx + 1, len(nums)):
                diff = nums[j] - nums[idx]
                if -target <= diff <= target:
                    result = fun(j)
                    if result != -1:
                        ans = max(ans, 1 + result)
            dp[idx] = ans
            return ans
        return fun(0)