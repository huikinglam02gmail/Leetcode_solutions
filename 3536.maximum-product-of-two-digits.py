#
# @lc app=leetcode id=3536 lang=python3
#
# [3536] Maximum Product of Two Digits
#

# @lc code=start
class Solution:
    def maxProduct(self, n: int) -> int:
        nString = "".join(sorted([c for c in str(n)]))
        return int(nString[-1]) * int(nString[-2])
# @lc code=end

