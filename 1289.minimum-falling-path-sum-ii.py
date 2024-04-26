#
# @lc app=leetcode id=1289 lang=python3
#
# [1289] Minimum Falling Path Sum II
#

# @lc code=start
from typing import List


class Solution:
    '''
    dp[i][j] = minimum of all falling path which ends at row i and column j
    Then we can just iterate through the rows from top to bottom    
    '''
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if n == 1:
            return grid[0][0]
        for i in range(n):
            dp_new = []
            if i == 0:
                for j in range(n):
                    dp_new.append([grid[i][j], j])
            else:
                for j in range(n):
                    if j != dp[0][1]:
                        dp_new.append([grid[i][j] + dp[0][0], j])
                    else:
                        dp_new.append([grid[i][j] + dp[1][0], j])
            dp = dp_new[:]
            dp.sort()
        return dp[0][0]
                    
# @lc code=end

