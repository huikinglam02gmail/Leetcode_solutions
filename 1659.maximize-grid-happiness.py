#
# @lc app=leetcode id=1659 lang=python3
#
# [1659] Maximize Grid Happiness
#

# @lc code=start
from functools import lru_cache


class Solution:
    '''
    1 <= m, n <= 5
    Total count of grid is at most 25, therefore can use bitmask. Use two bitmasks to represent the introvert / extrovert occupancy states. Also, as the score only concerns about neighbours, we do not need to consider the occupancy states further than n away from current state
    Also keep track of number of introverts / extroverts left behind. For each position, we consider not doing anything, put an introvert or put an extrovert.
    dp(i, I, E, iMask, eMask) = maximum possible grid happiness after considering grid[i+1:], with I introvert and E extrovert left behind and iMask and eMask representing the introvert / extrovert occupancy states of grid[i+1: i+1+n]
    '''
    @lru_cache(None)
    def dp(self, i, I, E, iMask, eMask):
        result = 0
        if i >= 0:
            neigs = [0, 0]
            # bottom has a neigbour:
            if i // self.n < self.m - 1:
                if (iMask & (1 << (self.n - 1))) != 0:
                    neigs[0] -= 30 * 2
                    neigs[1] += 20 - 30
                if (eMask & (1 << (self.n - 1))) != 0:
                    neigs[0] += 20 - 30
                    neigs[1] += 20 * 2
            # right has a neigbour:
            if i % self.n < self.n - 1:
                if (iMask & 1) != 0:
                    neigs[0] -= 30 * 2
                    neigs[1] += 20 - 30
                if (eMask & 1) != 0:
                    neigs[0] += 20 - 30
                    neigs[1] += 20 * 2
            
            # update the masks
            iMask <<= 1
            if iMask >= (1 << self.n):
                iMask -= (1 << self.n)
            eMask <<= 1
            if eMask >= (1 << self.n):
                eMask -= (1 << self.n)
            
            # Not put anything
            result = self.dp(i - 1, I, E, iMask, eMask)
            # put in an introvert
            if I > 0:
                result = max(result, 120 + neigs[0] + self.dp(i - 1, I - 1, E, iMask + 1, eMask))
            if E > 0:
                result = max(result, 40 + neigs[1] + self.dp(i - 1, I, E - 1, iMask, eMask + 1))
        return result

    def getMaxGridHappiness(self, m: int, n: int, introvertsCount: int, extrovertsCount: int) -> int:
        iMask, eMask = 0, 0
        self.m, self.n = m, n
        return self.dp(m*n - 1, introvertsCount, extrovertsCount, iMask, eMask)
# @lc code=end
