#
# @lc app=leetcode id=3131 lang=python3
#
# [3131] Find the Integer Added to Array I
#

# @lc code=start
from typing import List


class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        diff = sum(nums2) - sum(nums1)
        if diff >= 0: return diff // len(nums1)
        else: return - ((- diff) // len(nums1))
# @lc code=end

