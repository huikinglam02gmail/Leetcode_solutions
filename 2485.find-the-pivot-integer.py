#
# @lc app=leetcode id=2485 lang=python3
#
# [2485] Find the Pivot Integer
#

# @lc code=start
class Solution:
    def pivotInteger(self, n: int) -> int:
        prefix = [0]
        for i in range(1, n + 1): prefix.append(prefix[-1] + i)
        for x in range(1, n + 1):
            if prefix[x] - prefix[0] == prefix[-1] - prefix[x - 1]: return x
        return -1
# @lc code=end

