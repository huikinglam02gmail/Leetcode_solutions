#
# @lc app=leetcode id=3192 lang=python3
#
# [3192] Minimum Operations to Make Binary Array Elements Equal to One II
#

# @lc code=start
from typing import List


class Solution:
    '''
    LeftMost 0 at index i can only be converted to 1 by flipping nums[i:]. So we keep track of how many flips we conducted and iterate from left to right
    '''
    def minOperations(self, nums: List[int]) -> int:
        flips = 0
        for num in nums:
            if (num + flips) % 2 == 0: flips += 1
        return flips
        
# @lc code=end

