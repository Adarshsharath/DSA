class Solution:
    def GCD(self, a, b):
        while(b!=0):
            a,b=b,a%b
        return a

         
    def findGCD(self, nums: List[int]) -> int:
        minnum = nums[0]
        maxnum = nums[0]
        for i in nums:
            if i<minnum:
                minnum = i
            if i>maxnum:
                maxnum = i
        return self.GCD(minnum,maxnum)
         