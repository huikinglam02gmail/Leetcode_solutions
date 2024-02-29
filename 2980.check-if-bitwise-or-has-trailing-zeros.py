#
# @lc app=leetcode id=2980 lang=python3
#
# [2980] Check if Bitwise OR Has Trailing Zeros
#

# @lc code=start
from typing import List


class Solution:
    '''
    at least 2 even numbers
    '''
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        count = 0
        for num in nums:
            if num % 2 == 0: count += 1
        return count > 1
# @lc code=end

