#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#

# @lc code=start
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''
        Keep nums[l] != 0 and nums[r] == 0 and swap
        '''
        l, r, n = 0, 0, len(nums)
        while l < n and r < n:
            while l < n and nums[l] == 0:
                l += 1
            while r < n and nums[r] != 0:
                r += 1
            if l < n and r < n and r < l:
                nums[l], nums[r] = nums[r], nums[l]
            else:
                l += 1
# @lc code=end

