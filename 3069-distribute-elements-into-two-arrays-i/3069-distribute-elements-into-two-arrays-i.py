class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        if len(nums)<3:
            return nums
        arr1 = []
        arr2 = []

        arr1.append(nums[0])
        arr2.append(nums[1])

        for i in range(2,len(nums)):
            if (arr1[-1] > arr2[-1]):
                arr1.append(nums[i])
            else:
                arr2.append(nums[i])
        
        return arr1+arr2
            
        


        