#
# @lc app=leetcode id=3259 lang=python3
#
# [3259] Maximum Energy Boost From Two Drinks
#

# @lc code=start
from typing import List


class Solution:
    '''
    dp[3][n]:
    dp[0][i] = drink energyDrinkA at i
    dp[1][i] = drink energyDrinkB at i
    dp[2][i] = skip i
    '''
    def maxEnergyBoost(self, energyDrinkA: List[int], energyDrinkB: List[int]) -> int:
        n = len(energyDrinkA)
        dp = [[0 for j in range(n)] for i in range(3)]
        dp[0][0] = energyDrinkA[0]
        dp[1][0] = energyDrinkB[0]
        for j in range(1, n):
            dp[0][j] = energyDrinkA[j] + max(dp[0][j - 1], dp[2][j - 1])
            dp[1][j] = energyDrinkB[j] + max(dp[1][j - 1], dp[2][j - 1])
            dp[2][j] = max(dp[0][j - 1], dp[1][j - 1], dp[2][j - 1])
        return max(dp[0][j], dp[1][j], dp[2][j])

        
# @lc code=end

