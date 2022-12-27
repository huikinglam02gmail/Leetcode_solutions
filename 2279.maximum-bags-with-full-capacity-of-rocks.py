#
# @lc app=leetcode id=2279 lang=python3
#
# [2279] Maximum Bags With Full Capacity of Rocks
#

# @lc code=start
from typing import List


class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        free = []
        for i in range(len(capacity)):
            free.append(capacity[i] - rocks[i])
        if sum(free) <= additionalRocks:
            return len(capacity)
        else:
            free.sort()
            index = 0
            while additionalRocks >= free[index] and index < len(capacity):
                additionalRocks -= free[index]
                index += 1
            return index
# @lc code=end

