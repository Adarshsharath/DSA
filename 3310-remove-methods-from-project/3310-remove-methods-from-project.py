from collections import defaultdict

class Solution:
    def __init__(self):
        self.ls = set()          
        self.vis = set()         
        self.a = 0
        self.graph = defaultdict(list)

    def dfs(self, node):
        if node in self.ls:
            return

        self.ls.add(node)

        for neighbour in self.graph[node]:
            self.dfs(neighbour)

    def dfs1(self, node):
        if node in self.vis:
            return

        self.vis.add(node)

        for neighbour in self.graph[node]:
            if neighbour in self.ls:
                self.a = 1
                return

            self.dfs1(neighbour)

    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:

        for u, v in invocations:
            self.graph[u].append(v)

        self.dfs(k)

        for i in range(n):
            if i not in self.ls:
                self.dfs1(i)

        if self.a:
            return list(range(n))

        ans = []
        for i in range(n):
            if i not in self.ls:
                ans.append(i)

        return ans