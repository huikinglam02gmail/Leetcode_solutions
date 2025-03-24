#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start
from typing import List


class Solution:
    '''
    First sort the intervals by start
    Then just keep pushing the new intervals into the lane  
    '''
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        result = [intervals[0]]
        i = 1
        while i < len(intervals):
            if intervals[i][0] <= result[-1][1]: result[-1][1] = max(intervals[i][1], result[-1][1])
            else: result.append(intervals[i])
            i += 1
        return result
# @lc code=end

