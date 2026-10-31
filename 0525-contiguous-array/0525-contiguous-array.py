class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        array = []
        for i in nums:
            if i == 0:
                array.append(-1)
            else:
                array.append(1)

        hashmap = defaultdict(list)
        hashmap[0].append(-1)        

        ans = 0
        right = 0
        prefix_sum = 0
        for i in array:
            prefix_sum += i
            needed = prefix_sum      
            if needed in hashmap:
                left = min(hashmap[needed])
                x = right - left     
                ans = max(ans, x)

            hashmap[prefix_sum].append(right)
            right += 1

        return ans