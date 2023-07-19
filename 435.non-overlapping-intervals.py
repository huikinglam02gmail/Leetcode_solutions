#
# @lc app=leetcode id=435 lang=python3
#
# [435] Non-overlapping Intervals
#

# @lc code=start
from typing import List


class Solution:
    '''
    minimum number of intervals you need to remove == n - max length of nonoverlapping intervals
    We can first sort intervals by second index
    (Earlier ending ones leave room for future ones to fill in)   
    '''

    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: [x[1], x[0]])
        n = len(intervals)
        result, ans = [], 0
        for interval in intervals:
            if result and interval[0] < result[-1]:
                ans += 1
            else:
                result.append(interval[1])
        return ans
# @lc code=end

