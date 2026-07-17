from collections import defaultdict, Counter

class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        indegree = Counter()
        outdegree = Counter()

        # Build graph and count degrees
        for u, v in pairs:
            graph[u].append(v)
            outdegree[u] += 1
            indegree[v] += 1

        # Find the start node
        start = pairs[0][0]
        for node in graph:
            if outdegree[node] - indegree[node] == 1:
                start = node
                break

        path = []

        def dfs(node):
            while graph[node]:
                nxt = graph[node].pop()
                dfs(nxt)
            path.append(node)

        dfs(start)

        path.reverse()

        ans = []
        for i in range(len(path) - 1):
            ans.append([path[i], path[i + 1]])

        return ans