class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        ans = []

        def dfs(idx, target, subset):

            if target == 0:
                ans.append(subset[:])
                return

            if target < 0:
                return

            if idx == len(candidates):
                return


            subset.append(candidates[idx])

            dfs(idx, target - candidates[idx], subset)

            subset.pop()
            dfs(idx + 1, target, subset)

        dfs(0, target, [])

        return ans
            


