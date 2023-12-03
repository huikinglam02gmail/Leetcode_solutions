#
# @lc app=leetcode id=1266 lang=python3
#
# [1266] Minimum Time Visiting All Points
#

# @lc code=start
from typing import List


class Solution:
    '''
    Diagonal is cheaper than moving in straight line
    So always take diagonal first
    '''    
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        result, n = 0, len(points)
        for i in range(n-1):
            x1, y1 = points[i]
            x2, y2 = points[i + 1]
            result += max(abs(x1-x2), abs(y1-y2))
        return result
# @lc code=end

