#
# @lc app=leetcode id=452 lang=python3
#
# [452] Minimum Number of Arrows to Burst Balloons
#

# @lc code=start
from typing import List


class Solution:
    '''
    first sort according to x start
    We keep the leftmost position of the current arrow's range (end)
    '''
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: [x[0], x[1]])
        result, n = 1, len(points)
        end = points[0][1]
        for i in range(1, n):
            if points[i][0] > end: 
                result += 1
                end = points[i][1]
            end = min(end, points[i][1])
        return result
    # @lc code=end

