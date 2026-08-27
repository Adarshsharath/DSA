class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        def fun(preorder, inorder, i):

            if not inorder:
                return None, i

            root = TreeNode(preorder[i])

            mid = inorder.index(preorder[i])

            left_inorder = inorder[:mid]
            right_inorder = inorder[mid + 1:]

            root.left, i = fun(preorder, left_inorder, i + 1)

            root.right, i = fun(preorder, right_inorder, i)

            return root, i

        root, _ = fun(preorder, inorder, 0)

        return root