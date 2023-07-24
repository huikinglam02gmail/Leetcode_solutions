#
# @lc app=leetcode id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        y = n if n >= 0 else -n
        result = 1
        while (y > 0): 
            if (y % 2 == 0): 
                x *= x
                y //= 2

            else:
                result *= x
                y -= 1
        return result if n >= 0 else 1 / result
# @lc code=end

