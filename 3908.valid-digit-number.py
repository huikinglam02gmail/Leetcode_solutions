#
# @lc app=leetcode id=3908 lang=python3
#
# [3908] Valid Digit Number
#

# @lc code=start
class Solution:
    def validDigit(self, n: int, x: int) -> bool:
        if str(n)[0] == str(x): return False
        count = [0] * 10
        for c in str(n):
            count[int(c)] += 1
        return count[x] >= 1
# @lc code=end

