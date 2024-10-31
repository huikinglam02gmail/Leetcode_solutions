#
# @lc app=leetcode id=2463 lang=python3
#
# [2463] Minimum Total Distance Traveled
#

# @lc code=start
from functools import lru_cache
from typing import List


class Solution:
    '''
    First sort the robots and factories according to position
    Then we try to assign robot from i to factory j, starting with i = 0  and j = 0
    Because both of them are sorted, the problem has substructure:
    for robot i, we can either not use factory j or use factory j
    if we use factory j, we need to check if the factory j capacity is not yet reached
    dp(i,j,k) = minimum total distance traveled by robots[i:] if factory[j:] is open to use and factory[j] has repaired k robots
    '''
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()
        
        @lru_cache(None)
        def dp(i, j, k):
            if i == len(robot): return 0
            if j == len(factory):return float('Inf')
            skip = dp(i, j + 1, 0)
            if k + 1 > factory[j][1]: no_skip = float('Inf')
            else: no_skip = abs(robot[i] - factory[j][0]) + dp(i + 1, j, k + 1)
            return min(skip, no_skip)
        
        return dp(0, 0, 0)
# @lc code=end

