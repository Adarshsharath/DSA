class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        arr = []
        n = []
        for i in nums:
            if i % k == 0:
                arr.append(i)

        if not arr:
            return k

        # [2,4,6,8]
        for i in range(1,(len(arr)*k)+1):
            if i % k == 0:
                n.append(i)


        arr = sorted(list(set(arr)))
        for i in range(len(arr)):
            if arr[i] != n[i]:
                return n[i]
        return arr[-1] + k

        

            

