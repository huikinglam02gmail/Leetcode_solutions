#
# @lc app=leetcode id=3726 lang=python3
#
# [3726] Remove Zeros in Decimal Representation
#

# @lc code=start
class Solution:
    def removeZeros(self, n: int) -> int:
        result = 0
        while n > 0:
            digit = n % 10
            n //= 10
            if digit != 0:
                result = result * 10 + digit
        return int(str(result)[::-1])
# @lc code=end

