from collections import defaultdict

class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        mp = defaultdict(int)

        for i in s:
            mp[i] += 1

        ans = []
        seen = set()
        ch = ""

        for right in range(len(s)):

            seen.add(s[right])

            
            mp[s[right]] -= 1

            ch += s[right]


            finished = True

            for c in seen:
                if mp[c] != 0:
                    finished = False
                    break

            if finished:
                ans.append(len(ch))
                ch = ""
                seen = set()

        return ans