# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         p = 1
#         pre =[0]*len(nums)
#         pre[0] = 0
#         pre[1] = nums[0]
#         p = pre[1]
#         for i in range(2,len(nums)):
#             p = p * nums[i-1]
#             pre[i] = p
        

#         suf =[0]*len(nums)
#         suf[len(nums)-1] = 0
#         suf[len(nums)-2] = nums[-1]
#         p = nums[-1]
#         for i in range(len(nums)-3,-1,-1):
#             p = p*nums[i+1]
#             suf[i] = p
        
#         ans = []
#         for i in range(len(nums)):
#             if i == 0:
#                 ans.append(suf[i])
#                 continue
#             if i == len(nums)-1:
#                 ans.append(pre[i])
#                 continue
#             ans.append(pre[i]*suf[i])
#         return ans

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        pre = [1] * n
        suf = [1] * n

        for i in range(1, n):
            pre[i] = pre[i - 1] * nums[i - 1]

        for i in range(n - 2, -1, -1):
            suf[i] = suf[i + 1] * nums[i + 1]

        ans = []

        for i in range(n):
            ans.append(pre[i] * suf[i])

        return ans
            

