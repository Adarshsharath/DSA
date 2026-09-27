class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:

        # 1. Check reachability
        graph = defaultdict(list)

        for u, v, w in times:
            graph[u].append(v)

        visited = set()
        visited.add(k)

        def dfs(node):
            for neighbour in graph[node]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    dfs(neighbour)

        dfs(k)

        if len(visited) != n:
            return -1


        dist = [[float('inf')] * (n + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            dist[i][i] = 0

        for u, v, w in times:
            dist[u][v] = w

        for mid in range(1, n + 1):
            for i in range(1, n + 1):
                for j in range(1, n + 1):
                    dist[i][j] = min(
                        dist[i][j],
                        dist[i][mid] + dist[mid][j]
                    )

        return max(dist[k][1:])