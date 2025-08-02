#
# @lc app=leetcode id=3603 lang=python3
#
# [3603] Minimum Cost Path with Alternating Directions II
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    def minCost(self, m: int, n: int, waitCost: List[List[int]]) -> int:
        dp = [[float("inf") for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0: dp[i][j] = 1
                if i > 0: dp[i][j] = min(dp[i][j], dp[i - 1][j] + waitCost[i][j] + (i + 1) * (j + 1))
                if j > 0: dp[i][j] = min(dp[i][j], dp[i][j - 1] + waitCost[i][j] + (i + 1) * (j + 1))
        return dp[m - 1][n - 1] - waitCost[m - 1][n - 1]
# @lc code=end
