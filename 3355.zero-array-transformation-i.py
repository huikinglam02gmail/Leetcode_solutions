#
# @lc app=leetcode id=3355 lang=python3
#
# [3355] Zero Array Transformation I
#

# @lc code=start
from typing import List


class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        toAdd = [0] * (len(nums) + 1)
        for l, r in queries:
            toAdd[l] += 1
            toAdd[r + 1] -= 1
        current = 0
        for i in range(len(nums)):
            current += toAdd[i]
            nums[i] -= current
            if nums[i] > 0: return False
        return True
# @lc code=end

