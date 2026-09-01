class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        ls = []

        def inorder(root):
            if not root:
                return

            inorder(root.left)
            ls.append(root.val)
            inorder(root.right)

        inorder(root)

        mp = defaultdict(int)

        total = 0

        
        for i in range(len(ls) - 1, -1, -1):
            total += ls[i]
            mp[ls[i]] = total

        def constructTree(root):
            if not root:
                return None

            node = TreeNode(mp[root.val])

            node.left = constructTree(root.left)
            node.right = constructTree(root.right)

            return node

        final = constructTree(root)

        return final