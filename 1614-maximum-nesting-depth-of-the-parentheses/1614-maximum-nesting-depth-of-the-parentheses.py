class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        count = 0
        ans = []
        flag = True
        for i in s:
            if i == "(":
                flag=False
                stack.append("(")
            elif i == ")":
                count = len(stack)
                ans.append(count)
                stack.pop()
        if not flag:
            return max(ans)
        return 0