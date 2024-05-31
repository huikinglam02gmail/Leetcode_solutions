#
# @lc app=leetcode id=260 lang=python3
#
# [260] Single Number III
#

# @lc code=start
from typing import List


class Solution:
    '''
    XOR all nums to get a ^ b, where a != b
    Get the last set bit in which a & (1 << i) != b & (1 << i): can be obtained by bitmask & (- bitmask) or bitmask & (bitmask -1 ) ^ bitmask
    Loop through nums to separate out which num is set on that bit and only occur once. The other number is bitmask ^ num
    '''
    def singleNumber(self, nums: List[int]) -> List[int]:
        bitmask = 0
        for num in nums: bitmask ^= num
        last = bitmask & (bitmask - 1) ^ bitmask
        x = 0
        for num in nums:
            if num & last: x ^= num
        return [x, bitmask^x]
    # @lc code=end

