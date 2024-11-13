#
# @lc app=leetcode id=2563 lang=python3
#
# [2563] Count the Number of Fair Pairs
#

# @lc code=start
from typing import List
from sortedcontainers import SortedList
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        SL = SortedList()
        SL.add(nums[0])
        result = 0
        for i in range(1, len(nums)):
            result += SL.bisect_right(upper - nums[i]) - SL.bisect_left(lower - nums[i])
            SL.add(nums[i])
        return result
# @lc code=end

