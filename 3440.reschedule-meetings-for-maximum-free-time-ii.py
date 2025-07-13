#
# @lc app=leetcode id=3440 lang=python3
#
# [3440] Reschedule Meetings for Maximum Free Time II
#

# @lc code=start
from typing import List


class Solution:
    '''
    For each time interval, there are two possibilities:
    1. We move it to the empty slots apart from its current empty slot neighrborhood.
    2. We move it to the left or right such that it merges with the previous or next interval.
    So from left to right and then from right to left, we scan if there are empty slots larger or equal to current interval size.
    1. If either of the two conditions is satisfied, we can achieve startTime[i + 1] - endTime[i - 1]
    2. else, we can only achieve start[i + 1] - endTime[i - 1] - endTime[i] + startTime[i]
    '''
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        maxFromLeft =  0
        left = 0
        canMove = []
        for s, e in zip(startTime, endTime):
            canMove.append(e - s <= maxFromLeft)
            maxFromLeft = max(maxFromLeft, s - left)
            left = e
        right = eventTime
        maxFromRight = 0
        for i in range(len(startTime) - 1, -1, -1):
            s, e = startTime[i], endTime[i]
            canMove[i] = canMove[i] or (maxFromRight >= e - s)
            maxFromRight = max(maxFromRight, right - e)
            right = s
        startTime = [0] + startTime + [eventTime]
        endTime = [0] + endTime + [eventTime]
        result = 0
        for i in range(1, len(startTime) - 1):
            if canMove[i - 1]:
                result = max(result, startTime[i + 1] - endTime[i - 1])
            else:
                result = max(result, startTime[i + 1] - endTime[i - 1] + startTime[i] - endTime[i])
        return result
# @lc code=end

