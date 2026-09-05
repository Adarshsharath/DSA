class Solution:
    def longestSubstring(self, s: str, k: int) -> int:

        def fun(s, k):

            if len(s) < k:
                return 0

            mp = defaultdict(int)

            for i in s:
                mp[i] += 1

            bad = False

            for i in s:
                if mp[i] < k:
                    bad = True

            if not bad:
                return len(s)

            for i in range(len(s)):
                if mp[s[i]] < k:

                    left = fun(s[0:i], k)
                    right = fun(s[i+1:], k)

                    return max(left, right)

        return fun(s, k)