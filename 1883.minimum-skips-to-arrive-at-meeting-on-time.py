#
# @lc app=leetcode id=1883 lang=python3
#
# [1883] Minimum Skips to Arrive at Meeting On Time
#

# @lc code=start
from functools import lru_cache
from typing import List


class Solution:
    '''
    Only condition to return -1: sum(dist) > speed * hoursBefore
    dp[i][j] = amount of time needed to finish dist[i:] if j skips are left available
    When considering dist[i], we could:
    1. Use 1 skip on previously processed dist[i + 1:]. increase dist[i] on the time
    2. Don't use a skip on previously processed dist[i + 1:]. Increase dist[i] on the time ceildiv(time to process dist[i + 1:]) 
    '''
    def ceildiv(self, a, b):
        return -(a // -b)

    def minSkips(self, dist: List[int], speed: int, hoursBefore: int) -> int:
        n = len(dist)

        @lru_cache(None)
        def dp(i, j):
            if j < 0: return float("Inf")
            if i == n: return 0
            result = dist[i] + min(dp(i + 1, j - 1), self.ceildiv(dp(i + 1, j), speed) *speed)
            return result

        if sum(dist) > speed * hoursBefore:
            return -1
        
        for i in range(n):
            if dp(0, i) <= speed * hoursBefore:
                return i
        return -1 

# @lc code=end

