#
# @lc app=leetcode id=2348 lang=python3
#
# [2348] Number of Zero-Filled Subarrays
#

# @lc code=start
from typing import List


class Solution:
    '''
    Go through the array, if hit at i-1 being not 0 and i is, set i as left. If hit at i-1 being 0 and i is, set i as right . When arrive at right, add (right-left)(right-left+1)//2 to result    
    '''

    def zeroFilledSubarray(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        result = 0
        for i in range(1, len(nums)):
            if nums[i-1] != 0 and nums[i] == 0:
                left = i
            elif nums[i-1] == 0 and nums[i] != 0:
                right = i
                result += (right-left)*(right-left+1)//2
        return result
        
# @lc code=end

