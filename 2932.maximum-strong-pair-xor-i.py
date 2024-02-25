#
# @lc app=leetcode id=2932 lang=python3
#
# [2932] Maximum Strong Pair XOR I
#

# @lc code=start
from typing import List


class Solution:
    '''
    Brute force
    '''
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        result = 0
        for num1 in nums:
            for num2 in nums:
                if abs(num1 - num2) <= min(num1, num2): result = max(result, num1 ^ num2)
        return result
# @lc code=end

