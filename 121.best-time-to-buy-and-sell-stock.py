#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
from typing import List


class Solution:
    '''
    Since we only buy and sell once, the strategy should be to sell at a highest price and buy at the lowest price that occurred before selling. Each time we are given a price, we record the minimum price seen so far. The result is max(profit, price - min_so_far)    
    '''
    def maxProfit(self, prices: List[int]) -> int:
        profit, minSoFar = 0, 10001
        for price in prices:
            profit = max(profit, price - minSoFar)
            minSoFar = min(minSoFar, price)
        return profit
# @lc code=end

