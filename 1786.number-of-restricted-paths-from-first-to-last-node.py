#
# @lc app=leetcode id=1786 lang=python3
#
# [1786] Number of Restricted Paths From First to Last Node
#

# @lc code=start
from collections import deque
import heapq
from typing import List


class Solution:
    '''
    First build the graph
    Dijkstra from n to every point, record the distanceToLastNode(x) in an array
    Then we calculate number of paths starting from node 0 and reaching each node [i]
    '''
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
    
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        MOD = pow(10, 9) + 7

        graph = [{} for i in range(n)]
        for a, b, w in edges:
            graph[a - 1][b - 1] = w
            graph[b - 1][a - 1] = w
        
        distanceToLastNode = self.Dijkstra(graph, n - 1)
        distanceToLastNodeSorted = sorted(list(enumerate(distanceToLastNode)), key = lambda x: - x[1])
        result = [0] * n
        result[0] = 1
        i = 0
        while distanceToLastNodeSorted[i][0] != 0:
            i += 1
        
        for j in range(i, n):
            for nxt in graph[distanceToLastNodeSorted[j][0]]:
                if distanceToLastNode[nxt] < distanceToLastNodeSorted[j][1]:
                    result[nxt] += result[distanceToLastNodeSorted[j][0]]
                    result[nxt] %= MOD
        return result[-1]
        
        
        
        
# @lc code=end

