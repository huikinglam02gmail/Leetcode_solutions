#
# @lc app=leetcode id=2787 lang=python3
#
# [2787] Ways to Express an Integer as Sum of Powers
#

# @lc code=start
class Solution:
    '''
    dp[i][j] = number of ways to express j as a sum of unique integers^x using first i integers
    '''
    def numberOfWays(self, n: int, x: int) -> int:
        dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
        dp[0][0] = 1
        MOD = pow(10, 9) + 7
        for i in range(1, n + 1):
            for j in range(n + 1):
                dp[i][j] = dp[i - 1][j]
                if j >= pow(i, x): 
                    dp[i][j] += dp[i - 1][j - pow(i, x)]
                    dp[i][j] %= MOD
        return dp[n][n]
# @lc code=end

