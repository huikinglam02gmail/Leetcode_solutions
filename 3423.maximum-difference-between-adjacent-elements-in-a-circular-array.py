#
# @lc app=leetcode id=3423 lang=python3
#
# [3423] Maximum Difference Between Adjacent Elements in a Circular Array
#

# @lc code=start
from typing import List


class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        result = 0
        for i in range(len(nums)): result = max(result, abs(nums[i] - nums[(i + 1) % len(nums)]))
        return result
# @lc code=end

