class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)

        ls = []
        for x in nums:
            s = sum(map(int, str(x)))
            ls.append((s, x))

        sorted_ls = sorted(ls)

        pos = {val: i for i, val in enumerate(sorted_ls)}

        visited = [False] * n
        swaps = 0

        for i in range(n):
            if visited[i] or pos[ls[i]] == i:
                continue

            cycle = 0
            j = i

            while not visited[j]:
                visited[j] = True
                j = pos[ls[j]]
                cycle += 1

            swaps += cycle - 1

        return swaps