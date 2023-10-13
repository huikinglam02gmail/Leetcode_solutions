#
# @lc app=leetcode id=746 lang=python3
#
# [746] Min Cost Climbing Stairs
#

# @lc code=start
from typing import List


class Solution:
    '''
    DP question clearly
    dp[i] = min cost to reach i
    0 and 1 are trivial    
    '''
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        a, b, n = 0, 0, len(cost)
        for i in range(n):
            a, b = b, min(a, b) + cost[i]
        return min(a, b)
# @lc code=end

