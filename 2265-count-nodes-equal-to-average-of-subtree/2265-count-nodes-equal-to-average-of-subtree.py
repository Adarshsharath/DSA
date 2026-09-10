# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        def inorder(root, ls, sums, n):
            if not root:
                return ls, sums, n

            ls, sums, n = inorder(root.left, ls, sums, n)

            ls.append(root.val)
            sums += root.val
            n += 1

            ls, sums, n = inorder(root.right, ls, sums, n)

            return ls, sums, n
        count = [0]
        def fun(root):
            if not root:
                return
            
            ls,s,n = inorder(root,[],0,0)
            S = s//n
            if root.val == S:
                count[0] += 1
            print(root.val,S,count[0])

            fun(root.left)
            fun(root.right)

        fun(root)
        return count[0]




        