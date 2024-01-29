#
# @lc app=leetcode id=2656 lang=python3
#
# [2656] Maximum Sum With Exactly K Elements 
#

# @lc code=start
from typing import List


class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        return max(nums) * k + k * (k - 1) // 2
# @lc code=end

