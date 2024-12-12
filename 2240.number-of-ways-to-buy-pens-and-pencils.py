#
# @lc app=leetcode id=2240 lang=python3
#
# [2240] Number of Ways to Buy Pens and Pencils
#

# @lc code=start
class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        result = 0
        for i in range(total // cost1 + 1): result += (total - i * cost1) // cost2 + 1
        return result
# @lc code=end

