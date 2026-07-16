class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        k = len(nums)/3
        arr = []
        count = {}
        for i in nums:
            if i not in count:
                count[i] = 1
            else:
                count[i] += 1
        for key,value in count.items():
            if value>k:
                arr.append(key)
        return arr

        