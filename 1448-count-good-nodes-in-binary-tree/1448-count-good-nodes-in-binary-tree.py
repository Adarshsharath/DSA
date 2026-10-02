# class Solution:
#     def goodNodes(self, root: TreeNode) -> int:
#         ls = []
#         count = [0]

#         def fun(root):
#             if not root:
#                 return

#             ls.append(root.val)

#             if root.val == max(ls):
#                 count[0] += 1

#             fun(root.left)
#             fun(root.right)


#             ls.pop()

#         fun(root)
#         return count[0]
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def fun(root, mx):
            if not root:
                return 0

            count = 0

            if root.val >= mx:
                count = 1
                mx = root.val

            count += fun(root.left, mx)
            count += fun(root.right, mx)

            return count

        return fun(root, root.val)