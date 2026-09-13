# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder[0])
        def fun(root,val):
            if not root.left and val<root.val:
                root.left = TreeNode(val)
                return

            if not root.right and val>root.val:
                root.right = TreeNode(val)
                return
            
            if val<root.val:
                fun(root.left,val)
            
            if val>root.val:
                fun(root.right,val)
            
        for i in range(1,len(preorder)):
            fun(root,preorder[i])

        return root
        