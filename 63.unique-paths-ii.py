#
# @lc app=leetcode id=63 lang=python3
#
# [63] Unique Paths II
#

# @lc code=start
from typing import List


class Solution:
    '''
    Like in Leetcode 62. Unique Paths we first set up the dp values along the first row and first column
    The dp relation is the same as in Leetcode 62, but only hold for grids without obstacles    
    '''
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for i in range(n)] for j in range(m)]
        if obstacleGrid[0][0] == 1:
            return 0
        dp[0][0] = 1
        i = 0
        while i < m - 1 and obstacleGrid[i + 1][0] == 0:
            i += 1
            dp[i][0] = 1
        j = 0
        while j < n-1 and obstacleGrid[0][j + 1] == 0:
            j += 1
            dp[0][j] = 1
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i][j-1] + dp[i-1][j]
        return dp[m-1][n-1]
# @lc code=end

