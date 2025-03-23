#
# @lc app=leetcode id=2318 lang=python3
#
# [2318] Number of Distinct Roll Sequences
#

# @lc code=start
class Solution:
    '''
    dp[i][j][k] = total number of distinct sequences of length i + 1 and last roll is j and second last roll is k
    '''
    def distinctSequences(self, n: int) -> int:
        if n == 1: return 6
        MOD = 1000000007
        dpOld = [[0 for k in range(6)] for j in range(6)]
        dp = [[0, 1, 1, 1, 1, 1], 
              [1, 0, 1, 0, 1, 0],
              [1, 1, 0, 1, 1, 0],
              [1, 0, 1, 0, 1, 0],
              [1, 1, 1, 1, 0, 1],
              [1, 0, 0, 0, 1, 0]]
        allowed = [[1, 2, 3, 4, 5], [0, 2, 4], [0, 1, 3, 4], [0, 2, 4], [0, 1, 2, 3, 5], [0, 4]]
        for i in range(2, n):
            for j in range(6):
                for k in range(6):
                    dpOld[j][k] = dp[j][k]
                    dp[j][k] = 0
            for j in range(6):
                for k in allowed[j]:
                    for l in range(6):
                        if l != k:
                            dp[j][k] += dpOld[l][j]
                            dp[j][k] %= MOD
        S = 0
        for j in range(6):
            for k in range(6):
                S += dp[j][k]
                S %= MOD
        return S

        
# @lc code=end

