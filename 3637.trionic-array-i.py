#
# @lc app=leetcode id=3637 lang=python3
#
# [3637] Trionic Array I
#

# @lc code=start
from typing import List


class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        for i in range(1, len(nums)): 
            if nums[i] == nums[i - 1]: return False
        if nums[1] < nums[0]: return False 
        transitionCount = 0
        for i in range(1, len(nums) - 1):
            if nums[i - 1] < nums[i] > nums[i + 1]: transitionCount += 1
            if nums[i - 1] > nums[i] < nums[i + 1]: transitionCount += 1
        return transitionCount == 2
            
        # @lc code=end

