#
# @lc app=leetcode id=539 lang=python3
#
# [539] Minimum Time Difference
#

# @lc code=start
from typing import List


class Solution:
    '''
    Convert all time points to mins
    Sort and find min neighbor diff, including between 0th and last
    '''
    def findMinDifference(self, timePoints: List[str]) -> int:
        allTime = []
        for timePoint in timePoints: allTime.append(int(timePoint[0:2]) * 60 + int(timePoint[3:]))
        allTime.sort()
        result = allTime[0] + 24 * 60 - allTime[-1]
        for i in range(len(allTime) - 1): result = min(result, allTime[i + 1] - allTime[i])
        return result
# @lc code=end

