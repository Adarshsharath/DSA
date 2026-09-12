class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ["a","e","i","o","u"]
        ls = []
        s = list(s)
        for i in range(len(s)):
            if s[i].lower() in vowels:
                ls.append(s[i])
                s[i] = "*"
        for i in range(len(s)):
            if s[i] == "*":
                s[i] = ls.pop()
        return "".join(s)

