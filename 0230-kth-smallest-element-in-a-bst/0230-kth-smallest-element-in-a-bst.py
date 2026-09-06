class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ls = []
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            ls.append(root.val)
            inorder(root.right)

        inorder(root)

        return ls[k-1]