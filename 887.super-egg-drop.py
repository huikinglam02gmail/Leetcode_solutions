#
# @lc app=leetcode id=887 lang=python3
#
# [887] Super Egg Drop
#

# @lc code=start
class Solution:
    '''
    Famous egg drop problem
    Solving by DP:
    dp[m][k] = maximum number of floors I can check, given I have m moves and k eggs
    Then we have this recurrence relation:
    dp[m][k] = 1 + dp[m-1][k-1] + dp[m-1][k]    
    '''

    def superEggDrop(self, k: int, n: int) -> int:
        dp = [[0] * (k + 1) for i in range(n + 1)]
        for m in range(1, n + 1):
            for K in range(1, k + 1):
                dp[m][K] = dp[m - 1][K - 1] + dp[m - 1][K] + 1
            if dp[m][k] >= n:
                return m
# @lc code=end

