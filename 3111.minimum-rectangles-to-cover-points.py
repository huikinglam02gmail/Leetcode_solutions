#
# @lc app=leetcode id=3111 lang=python3
#
# [3111] Minimum Rectangles to Cover Points
#

# @lc code=start
from typing import List


class Solution:
    def minRectanglesToCoverPoints(self, points: List[List[int]], w: int) -> int:
        points.sort()
        result = 0
        start = - float("inf")
        for x, y in points:
            if x - start > w:
                start = x
                result += 1
        return result
# @lc code=end

