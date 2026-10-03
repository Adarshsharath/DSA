class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        left = 0
        ans = 0
        current_k = k
        for right in range(len(nums)):
            print(left,right)
            if nums[right]==0:
                current_k-=1
                
            while(current_k < 0):
                if nums[left] == 0:
                    current_k+= 1
                left += 1
            
            ans = max(ans,right-left+1)
        return ans