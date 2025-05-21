#
# @lc app=leetcode id=3550 lang=python3
#
# [3550] Smallest Index With Digit Sum Equal to Index
#

# @lc code=start
from typing import List


class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if i == sum([int(digit) for digit in str(nums[i])]): return i
        return -1        
# @lc code=end

