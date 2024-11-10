#
# @lc app=leetcode id=3151 lang=python3
#
# [3151] Special Array I
#

# @lc code=start
from typing import List


class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        for i in range(len(nums) - 1):
            if nums[i] % 2 == nums[i + 1] % 2: return False
        return True
# @lc code=end

