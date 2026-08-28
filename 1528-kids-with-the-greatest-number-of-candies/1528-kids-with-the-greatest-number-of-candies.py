class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxs = max(candies)
        ans = []
        for i in candies:
            if i + extraCandies >= maxs:
                ans.append(True)
            else:
                ans.append(False)

        return ans