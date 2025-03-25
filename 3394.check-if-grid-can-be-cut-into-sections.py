#
# @lc app=leetcode id=3394 lang=python3
#
# [3394] Check if Grid can be Cut into Sections
#

# @lc code=start
from typing import List


class Solution:
    '''
    Use Leetcode 56
    '''
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        x = []
        y = []
        for x1, y1, x2, y2 in rectangles:
            x.append([x1, x2])
            y.append([y1, y2])
        if len(self.merge(x)) >= 3: return True
        if len(self.merge(y)) >= 3: return True
        return False

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        result = [intervals[0]]
        i = 1
        while i < len(intervals):
            if intervals[i][0] < result[-1][1]: result[-1][1] = max(intervals[i][1], result[-1][1])
            else: result.append(intervals[i])
            i += 1
        return result
# @lc code=end

