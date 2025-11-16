#
# @lc app=leetcode id=3745 lang=python3
#
# [3745] Maximize Expression of Three Elements
#

# @lc code=start
from typing import List


class Solution:
    def maximizeExpressionOfThree(self, nums: List[int]) -> int:
        nums.sort()
        return nums[-1] + nums[-2] - nums[0]
# @lc code=end

