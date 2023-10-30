#
# @lc app=leetcode id=1976 lang=python3
#
# [1976] Number of Ways to Arrive at Destination
#

# @lc code=start
from collections import deque
import heapq
from typing import List


class Solution:
    '''
    We would spend a lot of time travelling unnecessary edges if we do not know the shortest path to reach from 0 to any node. Given 1 <= n <= 200, getting all the Dijkstra weight would amount to n^2 log(n) time, which is affordable.
    Then we search from 0 again and compare arrivalTime to the SSP arrivalTime. To prioritize order of search, we put nodes into a min heap with weight SSP[nxt] as the priority. Then we can make sure we process nodes with earlier arrival first
    '''
   
    '''
    graph is supposed to be [{} for i in range(n)], with graph[i][j] = weight[i][j]
    return the SSP weight for all nodes
    O(n^2 log(n)) time
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
    
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        graph = [{} for i in range(n)]
        for u, v, time in roads:
            graph[u][v] = time
            graph[v][u] = time
        SSP = self.Dijkstra(graph, 0)
        
        MOD = pow(10, 9) + 7
        dp = [0 for i in range(n)]
        heap = []
        heapq.heappush(heap, [0, 0, 1])
        nodesInHeap = [0] * n
        nodesInHeap[0] += 1
        while heap:
            arrivalTime, node, arrivalCount = heapq.heappop(heap)
            dp[node] += arrivalCount
            dp[node] %= MOD
            nodesInHeap[node] -= 1
            if node != n - 1 and nodesInHeap[node] == 0:
                for nxt, delta in graph[node].items():
                    if arrivalTime + delta == SSP[nxt]:
                        heapq.heappush(heap, [arrivalTime + delta, nxt, dp[node]])
                        nodesInHeap[nxt] += 1
        return dp[n - 1]

# @lc code=end

