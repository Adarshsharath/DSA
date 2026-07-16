# from collections import Counter
# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         count = Counter(nums)
#         s = count.most_common(2)
#         arr = []
#         for i in s:
#             arr.append(i[0])
#         return arr


from collections import defaultdict

class Solution:
    def topKFrequent(self, nums, k):

        count = defaultdict(int)

        for num in nums:
            count[num] += 1

        bucket = [[] for _ in range(len(nums)+1)]

        for num, freq in count.items():
            bucket[freq].append(num)

        ans = []

        for freq in range(len(bucket)-1,0,-1):

            for num in bucket[freq]:

                ans.append(num)

                if len(ans)==k:
                    return ans            