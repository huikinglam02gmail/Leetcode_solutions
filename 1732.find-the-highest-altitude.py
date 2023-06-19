#
# @lc app=leetcode id=1732 lang=python3
#
# [1732] Find the Highest Altitude
#

# @lc code=start
from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        current_max = 0
        current_height = 0
        for i in gain:
            current_height += i
            current_max = max(current_max, current_height)
        return current_max
# @lc code=end

