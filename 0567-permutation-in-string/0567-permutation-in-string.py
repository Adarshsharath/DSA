class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        left = 0
        right = k
        ls = list(sorted(s1))
        while(right<=len(s2)):
            word = list(sorted(s2[left:right]))
            if ls == word:
                return True
            left+=1
            right+=1
        return False

