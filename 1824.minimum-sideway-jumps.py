#
# @lc app=leetcode id=1824 lang=python3
#
# [1824] Minimum Sideway Jumps
#

# @lc code=start
from typing import List


class Solution:
    '''
    Number of states are limited at each position
    dp[i][j] = number of side jumps needed to reach at (i, j)
    dp[i][j] = min(dp[i - 1][j], 1 + dp[i][k != j]) if obstable[i] != k
    We aim to get min(dp[n][:]) 
    '''
    def minSideJumps(self, obstacles: List[int]) -> int:
        n = len(obstacles)
        dp1 = [1, 0, 1]
        for i in range(n):
            dp2 = dp1
            if obstacles[i] > 0:
                dp2[obstacles[i] - 1] = float("inf")
            dp3 = dp2
            for j in range(2):
                for k in range(j + 1, 3):
                    if obstacles[i] - 1 != j:
                        dp3[j] = min(dp3[j], 1 + dp2[k])
                    if obstacles[i] - 1 != k:
                        dp3[k] = min(dp3[k], 1 + dp2[j])
            dp1 = dp3
        return min(dp1)

            
# @lc code=end

