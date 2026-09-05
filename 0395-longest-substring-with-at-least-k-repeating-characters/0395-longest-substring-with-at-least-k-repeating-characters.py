class Solution:
    def longestSubstring(self, s: str, k: int) -> int:

        def fun(s):
            if len(s) < k:
                return 0

            mp = defaultdict(int)

            for ch in s:
                mp[ch] += 1

            for i in range(len(s)):
                if mp[s[i]] < k:
                    return max(
                        fun(s[:i]),
                        fun(s[i+1:])
                    )

            return len(s)

        return fun(s)