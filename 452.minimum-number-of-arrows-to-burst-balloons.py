#
# @lc app=leetcode id=452 lang=python3
#
# [452] Minimum Number of Arrows to Burst Balloons
#

# @lc code=start
from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # first sort according to x start
        points.sort(key = lambda x: [x[0], x[1]])
        result, n = 1, len(points)
        end = points[0][1]
        for i in range(1, n):
            if points[i][0] > end:
                end = points[i][1]
                result += 1
            elif points[i][1] < end:
                end = points[i][1]
        return result# @lc code=end

