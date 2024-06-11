#
# @lc app=leetcode id=1051 lang=python3
#
# [1051] Height Checker
#

# @lc code=start
from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        height_sorted, result = sorted(heights), 0
        for i in range(len(heights)):
            if heights[i] != height_sorted[i]: result += 1
        return result
# @lc code=end

