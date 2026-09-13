class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        ans = 0

        def height(root):
            nonlocal ans

            if not root:
                return -1

            left = height(root.left)
            right = height(root.right)

            ans = max(ans, left + right + 2)

            return 1 + max(left, right)

        height(root)

        return ans