#
# @lc app=leetcode id=1594 lang=python3
#
# [1594] Maximum Non Negative Product in a Matrix
#

# @lc code=start
from typing import List


class Solution:
    # dp[i][j][0] = maximum of product arriving at (i, j)
    # dp[i][j][1] = maximum of product arriving at (i, j)
    def maxProductPath(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dpMax =  [[- float('inf') for j in range(n)] for i in range(m)]
        dpMin =  [[float('inf') for j in range(n)] for i in range(m)]
        dpMax[0][0] = grid[0][0]
        dpMin[0][0] = grid[0][0]
        MOD = pow(10,9) + 7
        for i in range(m):
            for j in range(n):
                if i > 0:
                    if grid[i][j] >= 0:
                        dpMax[i][j] = max(dpMax[i][j], dpMax[i-1][j]*grid[i][j])
                        dpMin[i][j] = min(dpMin[i][j], dpMin[i-1][j]*grid[i][j])
                    if grid[i][j] <= 0:
                        dpMax[i][j] = max(dpMax[i][j], dpMin[i-1][j]*grid[i][j])
                        dpMin[i][j] = min(dpMin[i][j], dpMax[i-1][j]*grid[i][j])
                if j > 0:
                    if grid[i][j] >= 0:
                        dpMax[i][j] = max(dpMax[i][j], dpMax[i][j-1]*grid[i][j])
                        dpMin[i][j] = min(dpMin[i][j], dpMin[i][j-1]*grid[i][j])
                    if grid[i][j] <= 0:
                        dpMax[i][j] = max(dpMax[i][j], dpMin[i][j-1]*grid[i][j])
                        dpMin[i][j] = min(dpMin[i][j], dpMax[i][j-1]*grid[i][j])
        if dpMax[-1][-1] < 0:
            return -1
        else:
            return dpMax[-1][-1] % MOD

# @lc code=end
