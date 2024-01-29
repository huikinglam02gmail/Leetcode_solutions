#
# @lc app=leetcode id=2639 lang=python3
#
# [2639] Find the Width of Columns of a Grid
#

# @lc code=start
from typing import List


class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        result = [0] * n
        for i in range(m):
            for j in range(n):
                result[j] = max(result[j], len(str(grid[i][j])))
        return result
# @lc code=end

