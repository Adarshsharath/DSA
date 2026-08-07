class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ls = []
        def dfs(index,subsets):
            if index == len(nums):
                ls.append(subsets[:])
                return

            subsets.append(nums[index])
            dfs(index+1,subsets)

            subsets.pop()

            dfs(index+1,subsets)

        dfs(0,[])

        return ls