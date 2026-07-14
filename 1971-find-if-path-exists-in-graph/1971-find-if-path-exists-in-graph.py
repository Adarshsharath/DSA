class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        adj = [[] for _ in range(n)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        queue = [0] * n
        front = 0
        rear = 0

        queue[rear] = source

        visited = [False] * n
        visited[source] = True

        while front <= rear:

            start = queue[front]
            front += 1

            if start == destination:
                return True

            for neighbour in adj[start]:
                if not visited[neighbour]:
                    visited[neighbour] = True
                    rear += 1
                    queue[rear] = neighbour

        return False
                



        # adj = [[0] * n for _ in range(n)]

        # for u, v in edges:
        #     adj[u][v] = 1
        #     adj[v][u] = 1

        # R = [row[:] for row in adj]

        # for i in range(n):
        #     R[i][i] = 1

        # for k in range(n):
        #     for i in range(n):
        #         for j in range(n):
        #             R[i][j] = R[i][j] or (R[i][k] and R[k][j])

        # return R[source][destination] == 1