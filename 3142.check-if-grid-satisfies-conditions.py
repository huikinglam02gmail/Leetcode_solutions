#
# @lc app=leetcode id=3142 lang=python3
#
# [3142] Check if Grid Satisfies Conditions
#

# @lc code=start
from typing import List


class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if i < m - 1 and grid[i][j] != grid[i + 1][j]: return False
                if j < n - 1 and grid[i][j] == grid[i][j + 1]: return False
        return True
# @lc code=end

