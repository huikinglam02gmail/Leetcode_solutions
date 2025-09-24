#
# @lc app=leetcode id=3688 lang=python3
#
# [3688] Bitwise OR of Even Numbers in an Array
#

# @lc code=start
from typing import List


class Solution:
    def evenNumberBitwiseORs(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            if num % 2 == 0: result |= num
        return result
# @lc code=end

