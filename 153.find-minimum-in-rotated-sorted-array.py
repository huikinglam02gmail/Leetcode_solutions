#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#

# @lc code=start
from typing import List


class Solution:
    '''
    When nums is rotated by i % n != 0, nums[0] > nums[-1]
    So we binary search for it
    '''
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)
        while l < r - 1:
            mid = l + (r - l) // 2
            if nums[mid] > nums[l]:
                l = mid
            else:
                r = mid
        return nums[(l + 1) % len(nums)]
# @lc code=end

