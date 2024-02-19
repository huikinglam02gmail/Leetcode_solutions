#
# @lc app=leetcode id=231 lang=python3
#
# [231] Power of Two
#

# @lc code=start
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 2 or n == 1:
            return True
        elif n < 1 or n % 2:
            return False
        else:
            return self.isPowerOfTwo(n // 2)
# @lc code=end

