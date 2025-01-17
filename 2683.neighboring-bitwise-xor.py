#
# @lc app=leetcode id=2683 lang=python3
#
# [2683] Neighboring Bitwise XOR
#

# @lc code=start
from typing import List


class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        allXOR = 0
        for num in derived: allXOR ^= num
        return allXOR == 0
# @lc code=end

