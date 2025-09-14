#
# @lc app=leetcode id=3678 lang=python3
#
# [3678] Smallest Absent Positive Greater Than Average
#

# @lc code=start
from typing import List


class Solution:
    def smallestAbsent(self, nums: List[int]) -> int:
        avg = sum(nums) / len(nums)
        s = set(nums)
        i = 1
        while i <= avg: i += 1
        while i in s: i += 1
        return i
# @lc code=end

