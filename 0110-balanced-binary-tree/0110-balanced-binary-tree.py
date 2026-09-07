# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def node(root):
            def height(root):
                if not root:
                    return -1
                left = height(root.left)
                right = height(root.right)
                return 1 + max(left,right)
            
            leftL = height(root.left)
            rightL = height(root.right)

            if abs(leftL-rightL) >1:
                return False
            return True
        if not root:
            return True

        if not root.left and not root.right:
            return True

        if node(root):
            l = self.isBalanced(root.left)
            r = self.isBalanced(root.right)
            if l and r:
                return True
        return False
