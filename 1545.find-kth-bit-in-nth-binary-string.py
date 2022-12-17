#
# @lc app=leetcode id=1545 lang=python3
#
# [1545] Find Kth Bit in Nth Binary String
#

# @lc code=start
class Solution:
    # If we look for the mid element, it is always 1 except for n = 1
    # Otherwise just find if it is left or right of the mid element
    def findKthBit(self, n: int, k: int) -> str:
        if n == 1:
            return "0"
        if k == pow(2, n - 1):
            return "1"
        elif k > pow(2, n - 1):
            return str(1 - int(self.findKthBit(n - 1, pow(2, n) - k)))
        else:
            return self.findKthBit(n - 1, k)
# @lc code=end

