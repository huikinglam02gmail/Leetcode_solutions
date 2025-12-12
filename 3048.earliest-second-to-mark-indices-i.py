#
# @lc app=leetcode id=3048 lang=python3
#
# [3048] Earliest Second to Mark Indices I
#

# @lc code=start
from typing import List


class Solution:
    def earliestSecondToMarkIndices(self, nums: List[int], changeIndices: List[int]) -> int:
        l, r = 0, len(changeIndices) + 1
        while l < r:
            mid = l + (r - l) // 2
            if self.canMarkAll(nums, changeIndices, mid):
                r = mid
            else:
                l = mid + 1
        if l == len(changeIndices) + 1: return -1
        else: return l
    
    def canMarkAll(self, nums: List[int], changedIndices, time: int) -> bool:
        timeToMark = [-1] * len(nums)
        for i, ind in enumerate(changedIndices[:time]):
            timeToMark[ind - 1] = max(timeToMark[ind - 1], i + 1)
        timeToMarkData = [[t, i] for i, t in enumerate(timeToMark)]
        timeToMarkData.sort()
        S = 0
        count = 0
        for t, i in timeToMarkData:
            if t == -1 or t - S - count - 1 < nums[i]: return False
            S += nums[i]
            count += 1
        return True
# @lc code=end

