#
# @lc app=leetcode id=2540 lang=python3
#
# [2540] Minimum Common Value
#

# @lc code=start
from typing import List


class Solution:
    '''
    basically two pointers:
    i, j on nums1, nums2
    if nums1[i] < nums2[j] : i++
    elif nums1[i] > nums2[j] : j++
    else return nums1[i]
    '''
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        i,  j =  0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]: i += 1
            elif nums1[i] > nums2[j]: j += 1
            else: return nums1[i]
        return -1
# @lc code=end

