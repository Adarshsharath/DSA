from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:

        graph = defaultdict(list)

        for u, v, w in times:
            graph[u].append((v, w))

        heap = [(0, k)]

        dist = [float('inf')] * (n + 1)
        dist[k] = 0

        while heap:

            current_time, node = heapq.heappop(heap)


            if current_time > dist[node]:
                continue

            for neighbour, weight in graph[node]:

                new_time = current_time + weight

                if new_time < dist[neighbour]:
                    dist[neighbour] = new_time
                    heapq.heappush(heap, (new_time, neighbour))

        answer = max(dist[1:])

        return -1 if answer == float('inf') else answer