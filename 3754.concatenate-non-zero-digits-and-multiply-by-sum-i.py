#
# @lc app=leetcode id=3754 lang=python3
#
# [3754] Concatenate Non-Zero Digits and Multiply by Sum I
#

# @lc code=start
class Solution:
    def sumAndMultiply(self, n: int) -> int:
        nStripped = [int(d) for d in str(n) if d != '0']
        x = 0
        S = 0
        while nStripped:
            num = nStripped.pop(0)
            x *= 10
            x += num
            S += num
        return x * S
# @lc code=end

