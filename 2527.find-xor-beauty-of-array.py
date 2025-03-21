#
# @lc app=leetcode id=2527 lang=python3
#
# [2527] Find Xor-Beauty of Array
#

# @lc code=start
from typing import List


class Solution:
    def xorBeauty(self, nums: List[int]) -> int:
        XOR =  0
        for num in nums: XOR ^= num
        return XOR
# @lc code=end

