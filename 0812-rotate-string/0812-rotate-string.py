class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        ls = []
        for i in range(len(goal)):
            if goal[i] == s[0]:
                ls.append(i)
        while ls:
            idx = ls.pop()
            s1 = goal[idx:]
            s2 = goal[0:idx]
            
            rotated = s1+s2

            print(idx)

            print(rotated)

            if rotated == s:
                return True
        return False