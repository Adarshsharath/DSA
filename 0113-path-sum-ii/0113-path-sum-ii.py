# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.arr=[]
        self.path = []
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []

        self.path.append(root.val)

        if not root.left and not root.right:
            if(sum(self.path)==targetSum):
                self.arr.append(self.path.copy())

        else:
            self.pathSum(root.left,targetSum)
            self.pathSum(root.right,targetSum)
        self.path.pop()

        return self.arr 


