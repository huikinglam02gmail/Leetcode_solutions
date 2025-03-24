#
# @lc app=leetcode id=3169 lang=python3
#
# [3169] Count Days Without Meetings
#

# @lc code=start
from typing import List


class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings = self.merge(meetings)
        result = 0
        prev = 1
        for a, b in meetings:
            result += a - prev
            prev = b + 1
        return result + days - prev + 1
    
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

