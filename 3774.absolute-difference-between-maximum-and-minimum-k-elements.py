#
# @lc app=leetcode id=3774 lang=python3
#
# [3774] Absolute Difference Between Maximum and Minimum K Elements
#

# @lc code=start
from typing import List


class Solution:
    def absDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        return abs(sum(nums[-k:]) - sum(nums[:k]))
# @lc code=end

