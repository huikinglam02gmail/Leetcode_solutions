#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#

# @lc code=start
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        default_sum = len(nums) * (len(nums) + 1) // 2
        for i in range(len(nums)):
            default_sum -= nums[i]
        return default_sum
# @lc code=end

