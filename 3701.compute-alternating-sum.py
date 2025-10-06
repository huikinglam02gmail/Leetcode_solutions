#
# @lc app=leetcode id=3701 lang=python3
#
# [3701] Compute Alternating Sum
#

from typing import List

# @lc code=start
class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        result = 0
        for i, num in enumerate(nums):
            if i % 2 == 0: result += num
            else: result -= num
        return result
# @lc code=end

