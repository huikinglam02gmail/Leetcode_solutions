#
# @lc app=leetcode id=1155 lang=python3
#
# [1155] Number of Dice Rolls With Target Sum
#

# @lc code=start
class Solution:
    '''
    DP problem
    1 <= n, k <= 30
    1 <= target <= 1000
    dp[i][j] = number of ways to roll k-faced dice i + 1 times to get sum of j
    dp relation: dp[i][j] += dp[i-1][j-l] for l = 1 to k    
    '''
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = pow(10, 9) + 7
        dp = [[0 for j in range(target + 1)] for i in range(n)]
        for j in range(1, min(k, target) + 1):
            dp[0][j] += 1
        for i in range(n - 1):
            for j in range(target + 1):
                for l in range(1, k + 1):
                    if j + l < target + 1:
                        dp[i + 1][j + l] += dp[i][j]
                        dp[i + 1][j + 1] %= MOD
        return dp[n - 1][target]
# @lc code=end

