class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        op = ["+","-","/","*"]
        for i in tokens:
            if i in op:
                right = stack.pop()
                left = stack.pop()

                if i == "+":
                    result = (int(left))+(int(right))
                elif i == "-":
                    result = (int(left))-(int(right))
                elif i == "*":
                    result = (int(left))*(int(right))
                elif i == "/":
                    result = int((int(left))/(int(right)))
                stack.append(result)
            else:
                stack.append(i)
        return int((stack[-1]))