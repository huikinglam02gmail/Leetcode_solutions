#
# @lc app=leetcode id=3147 lang=python3
#
# [3147] Taking Maximum Energy From the Mystic Dungeon
#

# @lc code=start
from typing import List
import heapq


class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        energy.reverse()
        S = [0] * k
        result = -float('inf')
        for i, e in enumerate(energy):
            S[i % k] += e
            result = max(result, S[i % k])
        return result

# @lc code=end

