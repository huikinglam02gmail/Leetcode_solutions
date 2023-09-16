#
# @lc app=leetcode id=1631 lang=python3
#
# [1631] Path With Minimum Effort
#

# @lc code=start
import heapq
from typing import List


class Solution:
    '''
    Dijkstra
    '''
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        heap, m, n = [], len(heights), len(heights[0])
        heapq.heappush(heap, [0, 0, 0])
        while heap:
            w, x, y = heapq.heappop(heap)
            if x == m - 1 and y == n - 1:
                return w
            elif heights[x][y] >= 1:
                neigs = [[x, y + 1],[x, y - 1],[x + 1, y],[x - 1, y]]
                for xn, yn in neigs:
                    if m > xn >= 0 <= yn < n and heights[xn][yn] >= 1:
                        heapq.heappush(heap, [max(w, abs(heights[xn][yn] - heights[x][y])), xn, yn])
                heights[x][y] = -1

# @lc code=end
