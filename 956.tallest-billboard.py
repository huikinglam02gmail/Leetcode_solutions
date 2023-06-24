#
# @lc app=leetcode id=956 lang=python3
#
# [956] Tallest Billboard
#

# @lc code=start
from functools import lru_cache
from typing import List


class Solution:
    '''
    Similar idea as DP solution
    For each rod, we either not use it, add it to long or add it to short
    Let dfs(idx, diff) = maximum length of the shorter support if I considered rods from rods[idx:] and the support length difference is diff 
    '''

    @lru_cache(None)
    def dfs(self, idx, diff):
        if idx == len(self.rods):
            if diff == 0:
                return 0
            else:
                return - float('Inf')
        skip = self.dfs(idx + 1, diff)
        long = self.dfs(idx + 1, diff + self.rods[idx])
        if diff >= self.rods[idx]:
            short = self.dfs(idx + 1, diff - self.rods[idx]) + self.rods[idx]
        else:
            short = self.dfs(idx + 1, self.rods[idx] - diff) + diff
        result = max(skip, long, short)
        return result
    
    def tallestBillboard(self, rods: List[int]) -> int:
        self.rods = rods
        return self.dfs(0,0)
# @lc code=end

