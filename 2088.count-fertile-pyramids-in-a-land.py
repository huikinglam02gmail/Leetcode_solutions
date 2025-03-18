#
# @lc app=leetcode id=2088 lang=python3
#
# [2088] Count Fertile Pyramids in a Land
#

# @lc code=start
from typing import List


class Solution:
    def countPyramids(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        pyramid = [[0 for j in range(n)] for i in range(m)]
        result = 0
        for i in range(m - 2, -1, -1):
            for j in range(1, n - 1):
                if grid[i][j] == 1 and grid[i + 1][j - 1] == 1 and grid[i + 1][j] == 1 and grid[i + 1][j + 1] == 1:
                    pyramid[i][j] = 1 + min(pyramid[i + 1][j - 1], pyramid[i + 1][j], pyramid[i + 1][j + 1])
                    result += pyramid[i][j]
        inversePyramid = [[0 for j in range(n)] for i in range(m)]
        for i in range(1, m):
            for j in range(1, n - 1):
                if grid[i][j] == 1 and grid[i - 1][j - 1] == 1 and grid[i - 1][j] == 1 and grid[i - 1][j + 1] == 1:
                    inversePyramid[i][j] = 1 + min(inversePyramid[i - 1][j - 1], inversePyramid[i - 1][j], inversePyramid[i - 1][j + 1])
                    result += inversePyramid[i][j]
        return result
        

# @lc code=end

