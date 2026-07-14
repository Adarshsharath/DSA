class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        counts = {}

        for u, v in edges:
            if u in counts:
                counts[u] += 1
            else:
                counts[u] = 1

            if v in counts:
                counts[v] += 1
            else:
                counts[v] = 1

        x = 0

        for key, val in counts.items():
            if val > 1:
                x += 1

        if x == 1:
            for key, val in counts.items():
                if val > 1:
                    return key

        return -1