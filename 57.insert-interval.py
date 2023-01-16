#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#

# @lc code=start
import bisect
from operator import itemgetter
from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:     
        lval, rval = newInterval
        ri = bisect.bisect_right(intervals, rval, key = itemgetter(0))
        li = bisect.bisect_left(intervals, lval, key = itemgetter(1))        
        if li < len(intervals):
            lval = min(intervals[li][0], lval)
        if ri > 0:
            rval = max(intervals[ri-1][1], rval)
        intervals[li:ri] = [[lval, rval]]
        return intervals
# @lc code=end

