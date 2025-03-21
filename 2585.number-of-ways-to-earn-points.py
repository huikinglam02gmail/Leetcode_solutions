#
# @lc app=leetcode id=2585 lang=python3
#
# [2585] Number of Ways to Earn Points
#

# @lc code=start
from typing import List


class Solution:
    '''
    dp[i] = number of ways you can earn exactly i points
    '''
    def waysToReachTarget(self, target: int, types: List[List[int]]) -> int:
        dp = [0 for i in range(target + 1)]
        dp[0] = 1
        MOD = 1000000007

        for count, mark in types:
            for j in range(target, -1, -1):
                for i in range(count):
                    if j + (i + 1) * mark <= target: 
                        dp[j + (i + 1) * mark] += dp[j]
                        dp[j + (i + 1) * mark] %= MOD
        
        return dp[-1]
# @lc code=end

