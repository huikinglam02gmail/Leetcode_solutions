#
# @lc app=leetcode id=1575 lang=python3
#
# [1575] Count All Possible Routes
#

# @lc code=start
from functools import lru_cache
from typing import List


class Solution:
    # just dp to solve the problem
    # dp[i][f] = number of ways you arrive at i at the end while you have f of fuel left
    # We want to sum up dp[finish][0: fuel]

    @lru_cache(None)
    def dfs(self, loc, f):
        result = 0
        if f >= 0:
            if loc == self.finish:
                result += 1
            for i in range(self.n):
                if i != loc:
                    result += self.dfs(i, f - abs(self.locations[i] - self.locations[loc])) 
                    result %= self.MOD
        return result

    def countRoutes(self, l: List[int], start: int, fin: int, fuel: int) -> int:
        self.finish, self.n, self.locations, self.MOD = fin, len(l), l, pow(10, 9) + 7
        return self.dfs(start, fuel)
        