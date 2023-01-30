#
# @lc app=leetcode id=1368 lang=python3
#
# [1368] Minimum Cost to Make at Least One Valid Path in a Grid
#

# @lc code=start
import heapq
from typing import List


class Solution:
    # Typical Dijkstra graph search problem
    # We can modify the grid as we go
    def minCost(self, grid: List[List[int]]) -> int:
        heap, m, n = [], len(grid), len(grid[0])
        heapq.heappush(heap, [0, 0, 0])
        while heap:
            w, x, y = heapq.heappop(heap)
            if x == m-1 and y == n-1:
                return w
            neigs = [[x,y+1],[x,y-1],[x+1,y],[x-1,y]]
            arrow = grid[x][y] - 1
            for i, neig in enumerate(neigs):
                xn, yn = neig
                if m > xn >= 0 <= yn < n and 1 <= grid[xn][yn] <= 4:
                    if i == arrow:
                        heapq.heappush(heap, [w, xn, yn])
                    else:
                        heapq.heappush(heap, [w+1, xn, yn])
            grid[x][y] = 5
# @lc code=end

