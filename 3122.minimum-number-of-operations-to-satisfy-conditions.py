#
# @lc app=leetcode id=3122 lang=python3
#
# [3122] Minimum Number of Operations to Satisfy Conditions
#

# @lc code=start
from typing import List


class Solution:
    '''
    dp for each column, assuming the final state is i
    '''
    def minimumOperations(self, grid: List[List[int]]) -> int:
        dp = [0] * 10
        m, n = len(grid), len(grid[0])
        for j in range(n):
            dpNew = [0] * 10
            for i in range(m):
                for k in range(10):
                    if grid[i][j] != k:
                        dpNew[k] += 1
            for k in range(10):
                minCost = float('inf')
                for k1 in range(10):
                    if k1 != k:
                        minCost = min(minCost, dp[k1])
                dpNew[k] += minCost
            dp = dpNew
        return min(dp)
# @lc code=end

