class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        even = []
        odd = []

        for i in nums:
            if i%2 == 0:
                even.append(i)
            else:
                odd.append(i)

        e = len(even)
        i = 0
        while i < e:
            nums[i] = even[i]
            i+=1

        k = len(nums)
        j = 0
        while(i<k):
            nums[i] = odd[j]
            i+=1
            j+=1

        return nums
        