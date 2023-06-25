#
# @lc app=leetcode id=1575 lang=python3
#
# [1575] Count All Possible Routes
#

# @lc code=start
from functools import lru_cache
from typing import List


class Solution:
    '''
    just dp to solve the problem
    dp[i][f] = number of ways you arrive at i at the end while you have f of fuel left
    dp[i][f] = sum(dp[j][f])
    We want to sum up dp[finish][0: fuel]    
    '''

    def countRoutes(self, l: List[int], start: int, fin: int, fuel: int) -> int:
        n, MOD = len(l), pow(10, 9) + 7
        cost = [[abs(l[i] - l[j]) for i in range(n)] for j in range(n)]
        dp = [[0 for j in range(fuel + 1)] for i in range(len(l))]
        dp[start][fuel] = 1
        for f in range(fuel, -1, -1):
            for i in range(n):
                if dp[i][f] > 0:
                    for j in range(n):
                        if j != i and f - cost[i][j] >= 0:
                            dp[j][f - cost[i][j]] += dp[i][f]
                            dp[j][f - cost[i][j]] %= MOD
        return sum(dp[fin][:]) % MOD
        