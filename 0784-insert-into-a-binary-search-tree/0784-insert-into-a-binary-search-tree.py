# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        count = [1]
        if not root:
            root =TreeNode(val)
            return root
        def fun(root,val):
            print("Fun",count[0],root.val)
            count[0] += 1
            if val < root.val and not root.left:
                print("hi")
                root.left = TreeNode(val)
                return
            if val > root.val and not root.right:
                print("hi2")
                root.right = TreeNode(val)
                return

            
            if val < root.val:
                fun(root.left,val)

            if val > root.val:
                fun(root.right,val)

            return

        cur = root
        fun(cur,val)
        return root


