#
# @lc app=leetcode id=3309 lang=python3
#
# [3309] Maximum Possible Number by Binary Concatenation
#

# @lc code=start
from itertools import permutations
from typing import List


class Solution:
    def maxGoodNumber(self, nums: List[int]) -> int:
        binaries = [bin(num)[2:] for num in nums]
        perms = permutations(binaries)
        result = 0
        for perm in perms:
            current = int("".join(perm), 2)
            if current > result: result = current
        return result
# @lc code=end

