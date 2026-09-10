# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def averageOfSubtree(self, root: TreeNode) -> int:
#         def inorder(root,ls):
#             if not root:
#                 return
#             inorder(root.left,ls)
#             ls.append(root.val)
#             inorder(root.right,ls)
#             return ls
#         count = [0]
#         def fun(root):
#             if not root:
#                 return
            
#             ls = inorder(root,[])
#             S = sum(ls)//len(ls)
#             if root.val == S:
#                 count[0] += 1
#             fun(root.left)
#             fun(root.right)

#         fun(root)
#         return count[0]

class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:

        count = [0]

        def dfs(root):
            if not root:
                return 0, 0

            left_sum, left_count = dfs(root.left)
            right_sum, right_count = dfs(root.right)

            total_sum = left_sum + right_sum + root.val
            total_count = left_count + right_count + 1

            if root.val == total_sum // total_count:
                count[0] += 1

            return total_sum, total_count

        dfs(root)
        return count[0]



        