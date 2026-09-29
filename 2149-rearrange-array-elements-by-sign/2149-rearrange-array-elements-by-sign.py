class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        positive = []
        negative = []
        ans = []
        for i in nums:
            if i > 0:
                positive.append(i)
            elif i < 0:
                negative.append(i)

        p = True
        f = False
        positive.reverse()
        # print(positive)
        negative.reverse()
        # print(negative)
        for i in range(len(nums)):
            if p and not f:
                ans.append(positive.pop())
                p = False
                f = True
                continue
            if f and not p:
                ans.append(negative.pop())
                p = True
                f = False
                continue

        return ans