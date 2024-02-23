#
# @lc app=leetcode id=787 lang=python3
#
# [787] Cheapest Flights Within K Stops
#

# @lc code=start
# Dijkstra variant
import heapq
from typing import List


class Solution:
    '''
    To use Dijkstra's algorithm, one point to keep in mind is what to minimize in the heap.
    We still prefer popping the lowest cost paths, but we kick out any above k stops before return the result
    The visited array tracks the minimal number of steps to reach a certain node    
    '''
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = [{} for i in range(n)]
        for flight in flights:
            graph[flight[0]][flight[1]] = flight[2]
        visited = [float('inf')] * n
        heap = []
        heapq.heappush(heap, [0, src, 0])
        while heap:
            node = heapq.heappop(heap)
            if node[1] == dst:
                return node[0]
            if node[2] < k + 1:
                visited[node[1]] = node[2] 
                for neig in graph[node[1]].keys():
                    if node[2] + 1 < visited[neig]:
                        heapq.heappush(heap, [node[0] + graph[node[1]][neig], neig, node[2] + 1])
        return -1
# @lc code=end

