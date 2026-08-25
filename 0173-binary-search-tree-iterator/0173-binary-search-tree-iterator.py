# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.i = -1
        self.k = -1
        self.ls = []
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            self.ls.append(root.val)
            self.k += 1
            dfs(root.right)
        dfs(root)
        # [3,7,9,15,20]

    def next(self) -> int:
        self.i+=1
        if self.i <= self.k:
            return self.ls[self.i]

    def hasNext(self) -> bool:
        if self.i < self.k:
            return True
        return False
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()