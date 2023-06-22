#
# @lc app=leetcode id=714 lang=python3
#
# [714] Best Time to Buy and Sell Stock with Transaction Fee
#

# @lc code=start
from typing import List


class Solution:
    '''
    Similar problem as Leetcode 309. Best Time to Buy and Sell Stock with Cooldown
    Will need DP to resolve states: no stock and not buy; no stock and buy; have stock and sell; have stock and not sell
    1st row: no stock and buy in this turn
    2nd row: no stock and not buy in this turn
    3rd row: have stock and sell in this turn
    4th row: have stock and not sell in this turn      
    '''
  
    def maxProfit(self, prices: List[int], fee: int) -> int:
        dp = [0] * 4
        n = len(prices)
        for i in range(n):
            dpNew = [0] * 4
            if i == 0:
                dpNew[0] -= prices[i]
            elif i == 1:
                dpNew[0] = dp[1] - prices[i]
                dpNew[2] = dp[0] + prices[i] - fee
                dpNew[3] = dp[0]
            else:
                dpNew[0] = max(dp[1] , dp[2]) - prices[i]
                dpNew[1] = max(dp[1], dp[2])
                dpNew[2] = max(dp[0], dp[3]) + prices[i] - fee
                dpNew[3] = max(dp[0], dp[3])
            dp = dpNew.copy()
        return max(dp)
# @lc code=end

