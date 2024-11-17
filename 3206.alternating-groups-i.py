#
# @lc app=leetcode id=3206 lang=python3
#
# [3206] Alternating Groups I
#

# @lc code=start
from typing import List


class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        result = 0
        for i in range(len(colors)):
            if colors[i] != colors[(i + len(colors) - 1) % len(colors)] and colors[i] != colors[(i + len(colors) + 1) % len(colors)]: result += 1
        return result
        
# @lc code=end

