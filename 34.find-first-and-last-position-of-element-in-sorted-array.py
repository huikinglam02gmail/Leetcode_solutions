#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
import bisect
from typing import List


class Solution:
    '''
    # First search for target inside nums    
    '''
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if nums:
            left = bisect.bisect_left(nums, target)
            if left < len(nums) and nums[left] == target:
                return [left, bisect.bisect_right(nums, target) - 1]
        return [-1, -1]
# @lc code=end

