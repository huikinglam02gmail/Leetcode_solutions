#
# @lc app=leetcode id=2605 lang=python3
#
# [2605] Form Smallest Number From Two Digit Arrays
#

# @lc code=start
from typing import List


class Solution:
    '''
    brute force
    '''
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        for i in range(1, 100, 1):
            if i < 10 and i in nums1 and i in nums2: return i
            else:
                i1, i2 = divmod(i, 10)
                if (i1 in nums1 and i2 in nums2) or (i1 in nums2 and i2 in nums1): return i
        return -1
# @lc code=end

