#
# @lc app=leetcode id=3424 lang=python3
#
# [3424] Minimum Cost to Make Arrays Identical
#

# @lc code=start
from typing import List


class Solution:
    def minCost(self, arr: List[int], brr: List[int], k: int) -> int:
        result = 0
        for a, b in zip(arr, brr): result += abs(a - b)
        result1 = k
        for a, b in zip(sorted(arr), sorted(brr)): result1 += abs(a - b)
        return min(result, result1)
# @lc code=end

