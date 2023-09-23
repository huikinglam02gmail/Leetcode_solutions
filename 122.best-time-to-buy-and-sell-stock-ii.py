#
# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#

# @lc code=start
from typing import List


class Solution:
    '''
    Infinite buy-sell: just capture all the rising waves
    '''
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        for i in range(len(prices) - 1):
            result += max(0, prices[i + 1] - prices[i])
        return result
# @lc code=end

