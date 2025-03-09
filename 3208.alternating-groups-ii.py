#
# @lc app=leetcode id=3208 lang=python3
#
# [3208] Alternating Groups II
#

# @lc code=start
from typing import List


class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        transitions = 0
        result = 0
        for i in range(len(colors) + k - 1):
            if i >= k and colors[i - k] != colors[i - k + 1]: transitions -= 1
            if i > 0 and colors[i % len(colors)]  != colors[(i - 1) % len(colors)]: transitions += 1
            if transitions == k - 1: result += 1
        return result 

# @lc code=end

