#
# @lc app=leetcode id=2110 lang=python3
#
# [2110] Number of Smooth Descent Periods of a Stock
#

# @lc code=start
from typing import List


class Solution:
    '''
    Regular dp: dp[i] = # of smooth descent periods ending with prices[i]
    '''
    def getDescentPeriods(self, prices: List[int]) -> int:
        result = 0
        dp = 0
        n = len(prices)
        for i in range(n):
            if i > 0 and prices[i] != prices[i - 1] - 1: dp = 0
            dp += 1
            result += dp
        return result
        
# @lc code=end

