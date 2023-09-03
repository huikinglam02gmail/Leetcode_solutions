#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#

# @lc code=start
class Solution:
    '''
    Simple DP question    
    '''
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for i in range(n)] for j in range(m)]
        dp[0][0] = 0
        for i in range(m):
            dp[i][0] = 1
        for i in range(n):
            dp[0][i] = 1
        for i in range(1,m,1):
            for j in range(1,n,1):
                dp[i][j] = dp[i][j-1] + dp[i-1][j]
        return dp[m-1][n-1]
# @lc code=end

