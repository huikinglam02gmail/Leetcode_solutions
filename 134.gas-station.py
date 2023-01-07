#
# @lc app=leetcode id=134 lang=python3
#
# [134] Gas Station
#

# @lc code=start
from typing import List


class Solution:
    # From index 0, we scan the array by keeping track of deficit on the road
    # When current surplus becomes negative, that means whatever start point before is invalid
    # We push all of current to the accumulated deficit
    # At the end, we ask if current can cover deficit
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        current = 0
        deficit = 0
        start = 0
        for i in range(len(gas)):
            current += gas[i] - cost[i]
            if current < 0:
                start = i+1
                deficit += current
                current = 0
        if current + deficit >= 0:
            return start
        else:
            return -1
                        
# @lc code=end

