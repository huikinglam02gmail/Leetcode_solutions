#
# @lc app=leetcode id=2433 lang=python3
#
# [2433] Find The Original Array of Prefix Xor
#

# @lc code=start
from typing import List


class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        n = len(pref)
        for i in range(n - 1, 0, -1):
            pref[i] ^= pref[i - 1]
        return pref
# @lc code=end

