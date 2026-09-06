class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        ans = 0

        def inorder(root):
            nonlocal count, ans

            if not root:
                return

            inorder(root.left)

            count += 1
            if count == k:
                ans = root.val
                return

            inorder(root.right)

        inorder(root)
        return ans