class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None
        for num in nums:
            if count == 0:
                candidate = num
                count+=1
            else:
                if candidate == num:
                    count+=1

                elif candidate != num:
                    count -=1
        return candidate

            

