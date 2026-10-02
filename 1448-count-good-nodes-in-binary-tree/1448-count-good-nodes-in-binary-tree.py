class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ls = []
        count = [0]

        def fun(root):
            if not root:
                return

            ls.append(root.val)

            if root.val == max(ls):
                count[0] += 1

            fun(root.left)
            fun(root.right)


            ls.pop()

        fun(root)
        return count[0]