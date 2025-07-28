#
# @lc app=leetcode id=2708 lang=python3
#
# [2708] Maximum Strength of a Group
#

# @lc code=start
from typing import List


class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        result = - float("inf")
        for mask in range(1, 1 << len(nums)):
            product = 1
            for i in range(len(nums)):
                if mask & (1 << i):
                    product *= nums[i]
            result = max(result, product)
        return result
# @lc code=end

