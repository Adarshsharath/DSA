from collections import defaultdict
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        maps = defaultdict(int)
        mp = defaultdict(int)
        for i in range(len(s)):
            if not maps[s[i]] and not mp[t[i]]:
                maps[s[i]] = t[i]
                mp[t[i]] = s[i]
            else:
                if maps[s[i]] != t[i] or mp[t[i]] != s[i]:
                    return False
        return True
