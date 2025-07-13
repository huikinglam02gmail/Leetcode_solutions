#
# @lc app=leetcode id=3439 lang=python3
#
# [3439] Reschedule Meetings for Maximum Free Time I
#

# @lc code=start
from typing import List


class Solution:
    '''
    if k = 1, we try to move each meeting to its left, and the result will be maximum of gapLeft[i] + gapRight[i]
    if k > 1, we just move k meetings windows to its left.
    '''
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        l = 0
        gaps = []
        for s, e in zip(startTime, endTime):
            gaps.append(s - l)
            l = e
        gaps.append(eventTime - l)
        S = 0
        for i in range(k): S += gaps[i]
        result = 0
        for i in range(k, len(gaps)):
            S += gaps[i]
            result = max(S, result)
            S -= gaps[i - k]
        return result
# @lc code=end
