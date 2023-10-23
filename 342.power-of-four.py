#
# @lc app=leetcode id=342 lang=python3
#
# [342] Power of Four
#

# @lc code=start
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n > 0:
            nBinary = bin(n)[2:][::-1]
            if nBinary.count("1") == 1 and nBinary.find("1") % 2 == 0:
                return True
        return False
# @lc code=end

