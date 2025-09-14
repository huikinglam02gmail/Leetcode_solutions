#
# @lc app=leetcode id=3674 lang=python3
#
# [3674] Minimum Operations to Equalize Array
#

from typing import List
# @lc code=start
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        if len(set(nums)) == 1: return 0
        else: return 1
# @lc code=end

