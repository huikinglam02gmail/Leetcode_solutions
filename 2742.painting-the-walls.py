#
# @lc app=leetcode id=2742 lang=python3
#
# [2742] Painting the Walls
#

# @lc code=start
from typing import List


class Solution:
    '''
    Given each wall, we can assign it to paid painter and in the same period, the free painter can paint time[i] walls. Then the problem is reduced to the minimum cost to paint i - time[i] - 1 walls
    Let dp[i] = minimum amount of $ required to paint i walls
    Then dp[i] = min(dp[max(i - time[i] - 1, 0)] + cost[i]). Loop for i
    '''
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n = len(cost)
        dp = [float("inf") for i in range(n + 1)]
        dp[0] = 0
        for c, t in zip(cost, time):
            for i in range(n, 0, -1):
                dp[i] = min(dp[i], dp[max(0, i - t - 1)] + c)
        return dp[-1]

# @lc code=end

