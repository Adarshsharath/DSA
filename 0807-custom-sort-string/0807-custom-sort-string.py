class Solution:
    def customSortString(self, order: str, s: str) -> str:
        st = ""
        mp = defaultdict(int)

        for i in s:
            mp[i] += 1

        for i in order:
            if i in s:
                if mp[i]:
                    for j in range(mp[i]):
                        st += i
                mp[i] = 0
        new = st
        for i in s:
            if i not in st:
                new += i
        return new