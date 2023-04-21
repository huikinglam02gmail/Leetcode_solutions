#
# @lc app=leetcode id=879 lang=python3
#
# [879] Profitable Schemes
#

# @lc code=start
from typing import List


class Solution:
    '''
    A dp problem, more specifically, a knapsack problem
    dp[i][j] = number of profitable schemes for at i profits and j members, except for i == minProfit which is at least minProfit
    Go through the profit and group lists and ask if j + group[k] <= n
    dp[i+profit[k]][j + group[k]] += dp[i][j] if i + profit[k] < minProfit
    dp[minProfit][j + group[k]] += dp[i][j] if i+profit[k] >= minProfit    
    '''

    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        dp = [[0 for j in range(n+1)] for i in range(minProfit + 1)]
        MOD = pow(10,9) + 7
        dp[0][0] = 1
        for p, g in zip(profit, group):
            for i in range(minProfit,-1,-1):
                for j in range(n - g, -1, -1):
                    dp[min(minProfit, i + p)][j + g] += dp[i][j]
                    dp[min(minProfit, i + p)][j + g] %= MOD
        return sum(dp[minProfit]) % MOD
# @lc code=end

