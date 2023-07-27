#
# @lc app=leetcode id=1829 lang=python3
#
# [1829] Maximum XOR for Each Query
#

# @lc code=start
from typing import List


class Solution:
    '''
    First XOR through the array and pop element out by XOR the last element against the total XOR.
    The maximized XOR is 1 << maximumBit - 1. For example, if maximumBit is 3, max is 7 = 111. Suppose we have total XOR of 2 = 010, and the answer is num: num ^ 010 = 111
    num = 111 ^ 010 = 101 = 5
    '''
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        XOR = 0
        for num in nums:
            XOR ^= num
        n = len(nums)
        result = []
        for i in range(n):
            result.append(((1 << maximumBit) - 1) ^ XOR)
            XOR ^= nums[n - i - 1]
        return result
# @lc code=end

