#
# @lc app=leetcode id=2029 lang=python3
#
# [2029] Stone Game IX
#

# @lc code=start
from functools import lru_cache
from typing import List


class Solution:
    '''
    Firstly, notice in this game, 1 behaves the same as 4, 7...
    Just need to record occurrence of the modulo 3
    We then separate into two scenarios in which there is even or odd occurrences of mod0:
    So we just need to simulate
    '''
    def game(self, mod0, mod1, mod2, S, AliceSturn):
        if mod0 == 0 and mod1 == 0 and mod2 == 0: return False
        if S == 1:
            if mod1 > 0: return self.game(mod0, mod1 - 1, mod2, 2, not AliceSturn)
            elif mod0 > 0: return self.game(mod0 - 1, mod1, mod2, 1, not AliceSturn)
            else: return not AliceSturn
        else:
            if mod2 > 0: return self.game(mod0, mod1, mod2 - 1, 1, not AliceSturn)
            elif mod0 > 0: return self.game(mod0 - 1, mod1, mod2, 2, not AliceSturn)
            else: return not AliceSturn                     

    def stoneGameIX(self, stones: List[int]) -> bool:
        counts = [0] * 3
        for stone in stones: counts[stone % 3] += 1
        return (counts[1] > 0 and self.game(counts[0], counts[1] - 1, counts[2], 1, False)) or (counts[2] > 0 and self.game(counts[0], counts[1], counts[2] - 1, 2, False))
# @lc code=end

