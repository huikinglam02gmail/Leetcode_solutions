#
# @lc app=leetcode id=2864 lang=python3
#
# [2864] Maximum Odd Binary Number
#

# @lc code=start
class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        n = len(s)
        countOne = s.count('1')
        return '1' * (countOne - 1) + '0' * (n - countOne) + '1'
# @lc code=end

