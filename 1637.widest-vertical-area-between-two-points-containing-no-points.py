#
# @lc app=leetcode id=1637 lang=python3
#
# [1637] Widest Vertical Area Between Two Points Containing No Points
#

# @lc code=start
from typing import List


class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        xPos = set()
        for x, y in points:
            xPos.add(x)
        
        xList = sorted(xPos)
        result = 0
        for i in range(len(xList) - 1):
            result = max(result, xList[i+1] - xList[i])
        return result
# @lc code=end

