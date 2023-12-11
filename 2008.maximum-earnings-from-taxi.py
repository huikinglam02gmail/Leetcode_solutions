#
# @lc app=leetcode id=2008 lang=python3
#
# [2008] Maximum Earnings From Taxi
#

# @lc code=start
from typing import List


class Solution:
    '''
    Solve the problem with DP
    dp[i] = maximum number of dollars you can earn by picking up the passengers optimally when you are at i + 1.
    we look for dp[n - 1]
    dp[i] = max(dp[i - 1], dp[i - j] + i - j + tips)
    '''
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        possibleEarnings = [[] for i in range(n)]
        for s, e, t in rides: possibleEarnings[e - 1].append([s - 1, t])
        
        dp = [0] * n
        for i in range(1, n):
            dp[i] = dp[i - 1]
            for s, t in possibleEarnings[i]: dp[i] = max(dp[i], dp[s] + i - s + t)
        return dp[-1]
# @lc code=end

