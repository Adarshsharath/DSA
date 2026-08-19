# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def find(self,root,subRoot):
        if not root:
            return False

        if self.issame(root,subRoot):
            return True
            

        left = self.find(root.left,subRoot)
        right = self.find(root.right,subRoot)

        return left or right

    def issame(self,root,subRoot):
        if not root and not subRoot:
            return True

        if (root and not subRoot) or (not root and subRoot):
            return False

        if (root.val!=subRoot.val):
            return False
        
        
        left = self.issame(root.left,subRoot.left)

        right = self.issame(root.right,subRoot.right)

        return (left and right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return self.find(root,subRoot)


        
