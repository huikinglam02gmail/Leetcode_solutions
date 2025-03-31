#
# @lc app=leetcode id=2959 lang=python3
#
# [2959] Number of Possible Sets of Closing Branches
#

# @lc code=start
import heapq
from typing import List


class Solution:
    '''
    Use bitmask to represent whether a branch is closed, build the graph and Dijkstra 
    '''
    def numberOfSets(self, n: int, maxDistance: int, roads: List[List[int]]) -> int:
        result = 0
        for mask in range(1 << n):
            mapIndex = [-1 for i in range(n)]
            count = 0
            for j in range(n): 
                if mask & (1 << j) > 0: 
                    mapIndex[j] = count
                    count += 1
            graph = [{} for i in range(count)]
            for u, v, w in roads:
                if mapIndex[u] >= 0 and mapIndex[v] >= 0: 
                    graph[mapIndex[u]][mapIndex[v]] = min(graph[mapIndex[u]].get(mapIndex[v], float("inf")), w)
                    graph[mapIndex[v]][mapIndex[u]] = min(graph[mapIndex[v]].get(mapIndex[u], float("inf")), w)
            count1 = 0
            for i in range(count):
                if count <= 1: count1 += 1
                else:
                    Dijk = self.Dijkstra(graph, i)
                    if min(Dijk) >= 0 and max(Dijk) <= maxDistance: count1 += 1
            if count1 == count: result += 1
        return result


    def Dijkstra(self, graph, source):
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
                    heapq.heappush(heap, [weight + graph[node][nxt], nxt])
        return result 
# @lc code=end
