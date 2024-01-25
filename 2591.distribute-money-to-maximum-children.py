#
# @lc app=leetcode id=2591 lang=python3
#
# [2591] Distribute Money to Maximum Children
#

# @lc code=start
from functools import lru_cache


class Solution:
    '''
    follow the rule
    '''
    @lru_cache(None)
    def distMoney(self, money: int, children: int) -> int:
        if money < children: return -1
        if children == 1: 
            if money == 4: return -1
            elif money == 8: return 1
            else: return 0
        result = 0
        for i in range(1, min(money, 9), 1):
            if i == 4: continue
            nextStep = self.distMoney(money - i, children - 1)
            if nextStep >= 0: result = max(result, 1 + nextStep if i == 8 else 0)
        return result

# @lc code=end

