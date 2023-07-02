#
# @lc app=leetcode id=743 lang=python3
#
# [743] Network Delay Time
#

# @lc code=start
import heapq
from typing import List


class Solution:
    '''
    Dijkstra's algorithm    
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
            result[node] = weight
            if not visited[node]:
                visited[node] = True
                visitedCount += 1
                for nxt in graph[node].keys():
                    heapq.heappush(heap, [weight + graph[node][nxt], nxt])
        
        return result


    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = [{} for i in range(n)]
        for time in times:
            graph[time[0] - 1][time[1] - 1] = time[2]
        
        result = self.Dijkstra(graph, k - 1)
        result.sort()

        return -1 if result[0] == -1 else result[-1] 
            
# @lc code=end
