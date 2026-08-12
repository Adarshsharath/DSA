class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        ans = 0
        while(left<right):
            base = right - left

            height_L = min(height[left],height[right])

            water = base * height_L
            ans = max(ans,water)

            if height[left] < height[right]:
                left+=1
            else:
                right-=1
        return ans

        