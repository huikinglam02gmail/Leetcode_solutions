#
# @lc app=leetcode id=3184 lang=python3
#
# [3184] Count Pairs That Form a Complete Day I
#

# @lc code=start
from typing import List


class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        mods = [0] * 24
        for hour in hours: mods[hour % 24] += 1
        result = 0
        for i in range(1, 12): result += mods[i] * mods[24 - i]
        if mods[0] > 1: result += mods[0] * (mods[0] - 1) // 2
        if mods[12] > 1: result += mods[12] * (mods[12] - 1) // 2
        return result
        
# @lc code=end

