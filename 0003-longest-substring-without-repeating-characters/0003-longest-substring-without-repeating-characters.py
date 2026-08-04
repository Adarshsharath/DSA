from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        maxLen = 0
        mp = defaultdict(bool)

        for right in range(len(s)):
            while(mp[s[right]]):
                mp[s[left]] = False
                left += 1
                
            mp[s[right]] = True

            n = right - left + 1

            if n > maxLen:
                maxLen = n
        return maxLen


            