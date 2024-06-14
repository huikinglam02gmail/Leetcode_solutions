#
# @lc app=leetcode id=945 lang=python3
#
# [945] Minimum Increment to Make Array Unique
#

# @lc code=start
from typing import List


class Solution:
    '''
    Sort the array
    To be unique, nums[i] must be at least nums[i-1] + 1    
    '''
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        result = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1] + 1:
                result += nums[i-1] + 1 - nums[i]
                nums[i] = nums[i-1] + 1
        return result
# @lc code=end

