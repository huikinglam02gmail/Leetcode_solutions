#
# @lc app=leetcode id=64 lang=python3
#
# [64] Minimum Path Sum
#

# @lc code=start
import heapq
from typing import List


class Solution:
    '''
    One can do DP to solve the problem, but we can also use Dijkstra
    '''
    def minPathSum(self, grid: List[List[int]]) -> int:
        heap = []
        heapq.heappush(heap, [grid[0][0], 0, 0])
        grid[0][0] = -1
        m = len(grid)
        n = len(grid[0])
        while heap:
            cost, x, y = heapq.heappop(heap)
            if x == m - 1 and y == n - 1:
                return cost
            if x < m - 1 and grid[x + 1][y] >= 0:
                heapq.heappush(heap, [cost + grid[x + 1][y], x + 1, y])
                grid[x + 1][y] = -1
            if y < n - 1 and grid[x][y + 1] >= 0:
                heapq.heappush(heap, [cost + grid[x][y + 1], x, y + 1])
                grid[x][y + 1] = -1
        return -1
        
# @lc code=end

