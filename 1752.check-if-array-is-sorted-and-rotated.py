#
# @lc app=leetcode id=1752 lang=python3
#
# [1752] Check if Array Is Sorted and Rotated
#

# @lc code=start
from typing import List


class Solution:
    def check(self, nums: List[int]) -> bool:
        number_drop = 0
        for i in range(len(nums)-1):
            if nums[i+1] < nums[i]:
                number_drop += 1
                if number_drop > 1: return False
        if number_drop == 1: return nums[-1] <= nums[0]
        else: return True
        # @lc code=end

