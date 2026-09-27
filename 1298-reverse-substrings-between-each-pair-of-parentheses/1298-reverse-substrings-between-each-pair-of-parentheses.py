from collections import deque
class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        Q = deque()
        for i in s:
            if stack and i==")":
                while(stack[-1]!="("):
                    Q.append(stack.pop())
                stack.pop()
                while Q:
                    stack.append(Q.popleft())
            stack.append(i)

        s = ""
        for i in stack:
            if i not in ["(",")"]:
                s+=i
        return s
        
