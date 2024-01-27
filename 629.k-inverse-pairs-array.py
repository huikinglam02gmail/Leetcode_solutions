#
# @lc app=leetcode id=629 lang=python3
#
# [629] K Inverse Pairs Array
#

# @lc code=start
class Solution:
    '''
     dp[i][j] = number of permutations of [1,...,i] with j inverses
    We can easily see that there is only one way for k = 0: 1,2,3,....,i + 1
    We also see that dp[i][j] must contain dp[i - 1][j] (just put i at the end of 1,..., i - 1 permutations with j inverses)
    We can also put i into the second last position of the 1,..., i - 1 permutations with j - 1 inverses to get at j inverses total dp[i][j] must contain dp[i - 1][j - 1]
    To conclude, dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1] + dp[i - 1][j - 2] + ... + dp[i - 1][j - i + 1]
    We should notice that dp[i][j - 1] = dp[i - 1][j - 1] + dp[i - 1][j - 2] + dp[i - 1][j - 3] + ... + dp[i - 1][j - i]
    Therefore dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - i]
    dp for n and k
    Recurrence: dp[0][j] = 1
    dp[i][j] =  dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - i]   

    '''

    def kInversePairs(self, n: int, k: int) -> int:
        MOD = pow(10, 9) + 7
        dp = [[0 for j in range(k + 1)] for i in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = 1
        for i in range(2, n + 1):
            for j in range(1, k + 1):
                if j >= i:
                    dp[i][j] = (dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - i]) % MOD
                else:
                    dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % MOD
        return dp[n][k]
# @lc code=end

