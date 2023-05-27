#
# @lc app=leetcode id=1140 lang=python3
#
# [1140] Stone Game II
#

# @lc code=start
from functools import lru_cache
from typing import List


class Solution:
    '''
    This is similar to the Stone Game DP solution, but with the extra factor of m
    Since m is kind of arbitrary, I will use top-down DFS + memo to handle DP
    Because one will get all the stones in the first X remaining piles, it makes sense to switch to a suffix sum array
    dp(i,m) = maximum of Alice get when piles[i:] is remaining and m
    When i + 2*m >= n, Alice can get all
    Or else, dp(i,m) = suffix[i] - min(dp(i + x, max(m,x)), for x in range(1,2*m+1))    
    '''

    @lru_cache(None)
    def dp(self, i, m):
        result = self.piles[i]
        if i + 2*m < self.n:
            optimize = float('inf')
            for x in range(1, 2*m+1):
                optimize = min(optimize, self.dp(i+x, max(m,x)))
            result -= optimize
        return result
            
    def stoneGameII(self, piles: List[int]) -> int:
        self.n, self.piles = len(piles), piles
        for i in range(self.n-2,-1,-1):
            self.piles[i] += self.piles[i+1]
        return self.dp(0,1)
# @lc code=end

