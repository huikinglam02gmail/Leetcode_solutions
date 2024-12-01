#
# @lc app=leetcode id=3178 lang=python3
#
# [3178] Find the Child Who Has the Ball After K Seconds
#

# @lc code=start
class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        t = k % (2 * (n - 1))
        if 0 <= t <= n - 1: return t
        else: return 2 * n - 2 - t
# @lc code=end

