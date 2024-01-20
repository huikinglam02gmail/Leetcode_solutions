#
# @lc app=leetcode id=2544 lang=python3
#
# [2544] Alternating Digit Sum
#

# @lc code=start
class Solution:
    def alternateDigitSum(self, n: int) -> int:
        result = 0
        sign = 1
        for c in str(n):
            result += sign * int(c)
            sign *= -1
        return result
# @lc code=end

