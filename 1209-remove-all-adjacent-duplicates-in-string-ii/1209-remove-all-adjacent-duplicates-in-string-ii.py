class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for ch in s:
            if stack and stack[-1][0] == ch:
                if stack[-1][1] + 1 == k:
                    for _ in range(k-1):
                        
                        stack.pop()
                else:
                    stack.append((ch,stack[-1][1]+1))
            else:
                stack.append((ch,1))
        ls = []
        for item in stack:
            ls.append(item[0])

        return "".join(ls)