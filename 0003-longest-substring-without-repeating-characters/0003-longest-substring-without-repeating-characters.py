class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ls = []

        for i in range(len(s)):
            char = ""
            k = i
            while(s[k] not in char):
                char+=s[k]
                if k!=len(s)-1:
                    k+=1

            ls.append(char)
        maxVal = 0
        for ch in ls:
            if len(ch) > maxVal:
                maxVal = len(ch)
        return maxVal
            