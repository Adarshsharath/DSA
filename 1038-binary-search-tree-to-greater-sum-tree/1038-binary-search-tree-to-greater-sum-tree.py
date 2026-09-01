# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        ls = []
        def inorder(root):
            if not root:
                return

            inorder(root.right)
            ls.append(root.val)
            inorder(root.left)
            
        inorder(root)
        mp = defaultdict(int)

        total = 0

        for i in ls:
            total+=i
            mp[i] = total

        def modTree(root):
            if not root:
                return
            
            root.val = mp[root.val]
            modTree(root.left)
            modTree(root.right)

        modTree(root)
        return root

        
            