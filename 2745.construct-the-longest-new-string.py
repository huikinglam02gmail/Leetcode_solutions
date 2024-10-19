#
# @lc app=leetcode id=2745 lang=python3
#
# [2745] Construct the Longest New String
#

# @lc code=start
from functools import lru_cache


class Solution:
    '''
    DP problem. dp(x, y, z, last) = maximum possible length of the new string if last added string was -1: empty, 0: "AA", 1: "BB", 2: "CC"
    rules: 
    1. "AA" cannot be followed by "AA" or "AB"
    2. "BB" cannot be followed by "BB"
    3. "AB" cannot be followed by "BB"
    '''
    @lru_cache(None)
    def dp(self, x, y, z, last):
        result = 0
        if x > 0 and last != 0: result = max(result, 2 + self.dp(x - 1, y, z, 0))
        if y > 0 and last != 1 and last != 2: result = max(result, 2 + self.dp(x, y - 1, z, 1))
        if z > 0 and last != 0: result = max(result, 2 + self.dp(x, y, z - 1, 2))
        return result

    def longestString(self, x: int, y: int, z: int) -> int:
        return self.dp(x, y, z, -1)
# @lc code=end

