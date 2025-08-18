#
# @lc app=leetcode id=3301 lang=python3
#
# [3301] Maximize the Total Height of Unique Towers
#

from typing import List

# @lc code=start
class Solution:
    def maximumTotalSum(self, maximumHeight: List[int]) -> int:
        maximumHeight.sort()
        maximumHeight.append(maximumHeight[-1] + 1)
        result = 0
        for i in range(len(maximumHeight) - 2, -1, -1):
            maximumHeight[i] = min(maximumHeight[i], maximumHeight[i + 1] - 1)
            result += maximumHeight[i]
        return result if maximumHeight[i] > 0 else -1
# @lc code=end

