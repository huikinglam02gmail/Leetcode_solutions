#
# @lc app=leetcode id=3100 lang=python3
#
# [3100] Water Bottles II
#

# @lc code=start
from functools import lru_cache


class Solution:
    @lru_cache(None)
    def dp(self, full, empty, numExchange):
        if full == 0 and empty < numExchange: return 0
        result = 0
        for i in range(1, full + 1): result = max(result, i + self.dp(full - i, empty + i, numExchange))
        if empty >= numExchange: result = max(result, self.dp(full + 1, empty - numExchange, numExchange + 1))
        return result
        
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        return self.dp(numBottles, 0, numExchange)
        
# @lc code=end

