#
# @lc app=leetcode id=1641 lang=python3
#
# [1641] Count Sorted Vowel Strings
#

# @lc code=start
import math


class Solution:
    def countVowelStrings(self, n: int) -> int:
        return math.comb(n + 4, 4)
# @lc code=end

