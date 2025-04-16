#
# @lc app=leetcode id=3516 lang=python3
#
# [3516] Find Closest Person
#

# @lc code=start
class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        if abs(x - z) == abs(y - z): return 0
        elif abs(x - z) < abs(y - z): return 1
        else: return 2
# @lc code=end

