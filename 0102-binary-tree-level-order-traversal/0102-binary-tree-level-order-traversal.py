# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        stack = []
        if not root:
            return []
        if not root.left and not root.right:
            return [[root.val]]

        ans.append([root.val])
        stack.append([root])
        new = []
        new2 = []
        while stack:
            prev = stack.pop()
            new = []
            new2 = []
            for node in prev:
                if node.left:
                    new.append(node.left.val)
                    new2.append(node.left)


                if node.right:
                    new.append(node.right.val)
                    new2.append(node.right)
                
            if not new:
                return ans

            ans.append(new)
            stack.append(new2)
        



            
        