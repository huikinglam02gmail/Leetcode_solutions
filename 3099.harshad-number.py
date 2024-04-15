#
# @lc app=leetcode id=3099 lang=python3
#
# [3099] Harshad Number
#

# @lc code=start
class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        S = sum([int(c) for c in str(x)])
        return S if not x % S else -1
# @lc code=end

