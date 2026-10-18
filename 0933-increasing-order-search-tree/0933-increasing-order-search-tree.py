# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode | None) -> TreeNode | None:
        ls = []
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            ls.append(root.val)
            inorder(root.right)

        inorder(root)
        root = None
        prev = None
        for node in ls:
            Node = TreeNode(node)
            if not root:
                root = Node
                prev = root
            else:
                prev.right = Node
                prev = prev.right
            


        return root
