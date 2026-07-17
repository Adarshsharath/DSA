class Solution:
    def reverseWords(self, s: str) -> str:
        arr = s.split(" ")
        new = []
        l = len(arr)
        i = l-1
        while(i>=0):
            new.append(arr[i])
            i-=1
        s = " ".join(new)
        stack = []
        for ch in s:
            if ch == " " and (not stack or stack[-1]==" "):
                continue
            else:
                stack.append(ch)
        if stack and stack[-1]==" ":
            stack.pop()
        return "".join(stack)
       

            

        