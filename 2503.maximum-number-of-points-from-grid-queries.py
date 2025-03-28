#
# @lc app=leetcode id=2503 lang=python3
#
# [2503] Maximum Number of Points From Grid Queries
#

# @lc code=start
import bisect
import heapq
from typing import List


class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        m, n = len(grid), len(grid[0])
        threshold = [[0 for j in range(n)] for i in range(m)]
        heap = []
        elements = []
        heapq.heappush(heap, [grid[0][0], 0, 0])
        while heap:
            while heap and threshold[heap[0][1]][heap[0][2]] > 0: heapq.heappop(heap)
            if heap:
                cost, x, y = heapq.heappop(heap)
                threshold[x][y] = cost
                elements.append(threshold[x][y])
                for nx, ny in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                    if 0 <= nx < m and 0 <= ny < n: heapq.heappush(heap, [max(grid[nx][ny], threshold[x][y]), nx, ny])
        elements.sort()
        
        result = []
        for query in queries: result.append(bisect.bisect_left(elements, query))
        return result
        
# @lc code=end

