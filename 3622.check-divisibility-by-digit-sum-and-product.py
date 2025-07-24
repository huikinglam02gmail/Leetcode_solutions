#
# @lc app=leetcode id=3622 lang=python3
#
# [3622] Check Divisibility by Digit Sum and Product
#

# @lc code=start
class Solution:
    def checkDivisibility(self, n: int) -> bool:
        product = 1
        S = 0
        for c in str(n):
            product *= int(c)
            S += int(c)
        return n % (S + product) == 0
# @lc code=end

