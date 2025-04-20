#
# @lc app=leetcode id=3148 lang=python3
#
# [3148] Maximum Difference Score in a Grid
#

# @lc code=start
from typing import List


class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        result = - float("inf")
        m, n = len(grid), len(grid[0])
        dp = [[- float("inf") for j in range(n)] for i in range(m)]
        dp[0][0] = 0
        for i in range(m):
            for j in range(n):
                if j > 0 or i > 0:
                    if j > 0:
                        dp[i][j] = max(dp[i][j], dp[i][j - 1] + grid[i][j] - grid[i][j - 1])
                        dp[i][j] = max(dp[i][j], grid[i][j] - grid[i][j - 1]) 
                    if i > 0:
                        dp[i][j] = max(dp[i][j], dp[i - 1][j] + grid[i][j] - grid[i - 1][j])
                        dp[i][j] = max(dp[i][j], grid[i][j] - grid[i - 1][j])
                    result = max(result, dp[i][j])
        return result

# @lc code=end

