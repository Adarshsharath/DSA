class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even = []
        odd = []

        for i in nums:
            if i%2==0:
                even.append(i)
            else:
                odd.append(i)

        n = len(nums)
        i = 0
        e = True
        o = False
        while i<n:
            if e and not o:
                nums[i] = even.pop()
                e = False
                o = True
            elif o and not e:
                nums[i] = odd.pop()
                e = True
                o = False
            i += 1
        return nums
            