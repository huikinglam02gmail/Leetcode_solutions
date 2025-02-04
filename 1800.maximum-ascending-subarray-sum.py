#
# @lc app=leetcode id=1800 lang=python3
#
# [1800] Maximum Ascending Subarray Sum
#

# @lc code=start
from typing import List


class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        result = 0
        current = 0
        for i in range(len(nums)):
            if i == 0: current += nums[i]
            elif nums[i] > nums[i - 1]: current += nums[i]
            else: current = nums[i]
            result = max(current, result)
        return result
# @lc code=end

