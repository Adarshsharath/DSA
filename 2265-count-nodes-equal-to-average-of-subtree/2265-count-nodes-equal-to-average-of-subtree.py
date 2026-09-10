# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        def inorder(root,ls):
            if not root:
                return
            inorder(root.left,ls)
            ls.append(root.val)
            inorder(root.right,ls)
            return ls
        count = [0]
        def fun(root):
            if not root:
                return
            
            ls = inorder(root,[])
            S = sum(ls)//len(ls)
            if root.val == S:
                count[0] += 1
            fun(root.left)
            fun(root.right)

        fun(root)
        return count[0]




        