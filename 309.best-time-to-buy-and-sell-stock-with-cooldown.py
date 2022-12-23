#
# @lc app=leetcode id=309 lang=python3
#
# [309] Best Time to Buy and Sell Stock with Cooldown
#

# @lc code=start
from typing import List


class Solution:
    # DP problem
    # 4 possible states on each day:
    # 1: no stock and buy in this turn
    # 2: no stock and not buy in this turn
    # 3: have stock and sell in this turn
    # 4: have stock and not sell in this turn    
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        # Edge cases
        if n == 1:
            return 0
        elif n == 2:
            return max(0, prices[1] - prices[0])
        else:
            dp = [[0 for i in range(n)] for j in range(4)]
            for i in range(n):
                if i == 0:
                    dp[0][i] -= prices[i]
                elif i == 1:
                    dp[0][i] = dp[1][i-1] - prices[i]
                    dp[2][i] = prices[i] + dp[0][i-1]
                    dp[3][i] = dp[0][i-1]
                else:
                    dp[0][i] = dp[1][i-1] - prices[i]
                    dp[1][i] = max(dp[1][i-1], dp[2][i-1])
                    dp[2][i] = prices[i] + max(dp[0][i-1], dp[3][i-1])
                    dp[3][i] = max(dp[0][i-1], dp[3][i-1])
            #print(dp)
            return max(dp[0][n-1], dp[1][n-1], dp[2][n-1], dp[3][n-1])
# @lc code=end

