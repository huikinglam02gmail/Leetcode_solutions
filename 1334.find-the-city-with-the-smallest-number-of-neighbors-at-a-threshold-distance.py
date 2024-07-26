#
# @lc app=leetcode id=1334 lang=python3
#
# [1334] Find the City With the Smallest Number of Neighbors at a Threshold Distance
#

# @lc code=start
import heapq
from typing import List


class Solution:
    '''
    2 <= n <= 100
    A brute forceish approach would be Dijkstra from every node and search until the heap top cost is higher than distanceThreshold or the heap is empty
    Record reachable city counts in a hash table    
    '''

    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # Build the graph first
        graph = [set() for i in range(n)]
        for node1, node2, w in edges:
            graph[node1].add((w, node2))
            graph[node2].add((w, node1))
        
        # Dijkstra * n
        result = [0]*n
        for i in range(n):
            cost, heap = [float('inf') for j in range(n)], []
            heap = []
            heapq.heappush(heap, [0, i])
            while heap and heap[0][0] <= distanceThreshold:
                while heap and cost[heap[0][1]] <= heap[0][0]:
                    heapq.heappop(heap)
                if heap and heap[0][0] <= distanceThreshold:
                    c, node = heapq.heappop(heap)
                    cost[node] = c
                    for w, nxt in graph[node]:
                        if c + w < cost[nxt]: heapq.heappush(heap, [c + w, nxt])
            for j in range(n):
                if cost[j] < float('Inf'):
                    result[j] += 1
        return sorted([[i, count] for i, count in enumerate(result)], key = lambda x: [x[1], -x[0]])[0][0]
# @lc code=end

