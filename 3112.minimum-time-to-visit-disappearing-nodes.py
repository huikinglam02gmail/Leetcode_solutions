#
# @lc app=leetcode id=3112 lang=python3
#
# [3112] Minimum Time to Visit Disappearing Nodes
#

# @lc code=start
import heapq
from typing import List

class Solution:
    '''
    Modified Dijkstra's algorithm to account for disappearing nodes.
    '''
    def minimumTime(self, n: int, edges: List[List[int]], disappear: List[int]) -> List[int]:
        graph = [{} for _ in range(n)]
        for u, v, l in edges:
            if v not in graph[u]: graph[u][v] = float('inf')
            if u not in graph[v]: graph[v][u] = float('inf')
            graph[u][v] = min(graph[u][v], l)
            graph[v][u] = min(graph[v][u], l)
        
        return self.DijkstraWithDisappear(graph, 0, disappear)

    '''
    graph is supposed to be [{} for i in range(n)], with graph[i][j] = weight[i][j]
    return the SSP weight for all nodes
    O(n^2 log(n)) time
    '''
    def DijkstraWithDisappear(self, graph, source, disappear):
        n = len(graph)
        result = [-1] * n
        heap = []
        visited = [False]*n
        visitedCount = 0
        heapq.heappush(heap, [0, source])

        while heap and visitedCount < n:
            weight, node = heapq.heappop(heap)
            if result[node] < 0:
                result[node] = weight
                visited[node] = True
                visitedCount += 1
                for nxt in graph[node].keys():
                    if weight + graph[node][nxt] < disappear[nxt]:
                        heapq.heappush(heap, [weight + graph[node][nxt], nxt])        
        return result
# @lc code=end
