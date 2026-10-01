# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def constructMaximumBinaryTree(self, nums: list[int]) -> TreeNode | None:
        def fun(current_nums):
            if not current_nums:
                return None
                
            max_val = max(current_nums)
            pivot_idx = current_nums.index(max_val)

            root = TreeNode(max_val)

            left_arr = current_nums[:pivot_idx]
            right_arr = current_nums[pivot_idx + 1:]

            
            root.left = fun(left_arr)
            root.right = fun(right_arr)

            return root
            
        return fun(nums)