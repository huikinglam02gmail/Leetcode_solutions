#
# @lc app=leetcode id=3128 lang=python3
#
# [3128] Right Triangles
#

# @lc code=start
from typing import List


class Solution:
    def numberOfRightTriangles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        rows = [0] * m
        cols = [0] * n
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    rows[i] += 1
                    cols[j] += 1
        result = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    result += (rows[i] - 1) * (cols[j] - 1)
        return result
# @lc code=end

