#
# @lc app=leetcode id=3894 lang=python3
#
# [3894] Traffic Signal Color
#

# @lc code=start
class Solution:
    def trafficSignal(self, timer: int) -> str:
        if timer == 0: return "Green"
        if timer == 30: return "Orange"
        if 30 < timer <= 90: return "Red"
        return "Invalid"
# @lc code=end

