#
# @lc app=leetcode id=1818 lang=python3
#
# [1818] Minimum Absolute Sum Difference
#

# @lc code=start
from typing import List


class Solution:
    '''
    We can only replace numbers on nums1. The number to look for is the number in nums1 just smaller than and above nums2[i]
    '''
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        result = sum([abs(num1 - num2) for num1, num2 in zip(nums1, nums2)])
        return result
# @lc code=end

