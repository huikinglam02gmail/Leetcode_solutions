#
# @lc app=leetcode id=3345 lang=python3
#
# [3345] Smallest Divisible Digit Product I
#

# @lc code=start
from functools import reduce


class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
       while reduce(lambda x, y: x * y, [int(x) for x in str(n)]) % t: n += 1
       return n 
# @lc code=end

