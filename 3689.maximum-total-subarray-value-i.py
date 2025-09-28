#
# @lc app=leetcode id=3689 lang=python3
#
# [3689] Maximum Total Subarray Value I
#

# @lc code=start
from typing import List


class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        return k * (max(nums) - min(nums))
# @lc code=end

