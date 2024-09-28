#
# @lc app=leetcode id=2497 lang=python3
#
# [2497] Maximum Star Sum of a Graph
#

# @lc code=start
import heapq
from typing import List


class Solution:
    '''
    # of edge is limited below 10 ^ 5
    So for each node, keep a k min heap of val[neighbour]
    Then for each node, pop from the heap until:
    1. heap is empty
    2. sum will be negative if further pop
    '''
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        graph = [[] for i in range(len(vals))]
        for a, b in edges:
            heapq.heappush(graph[a], vals[b])
            heapq.heappush(graph[b], vals[a])
            while len(graph[a]) > k: heapq.heappop(graph[a])
            while len(graph[b]) > k: heapq.heappop(graph[b])
        result = - float("inf")
        for i in range(len(vals)):
            S = 0
            graph[i].sort(reverse = True)
            for j in range(len(graph[i])):
                if graph[i][j] <= 0: break
                S += graph[i][j]
            result = max(result, S + vals[i])
        return result

# @lc code=end
