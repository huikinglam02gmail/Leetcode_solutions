#
# @lc app=leetcode id=1561 lang=python3
#
# [1561] Maximum Number of Coins You Can Get
#

# @lc code=start
from typing import List


class Solution:
    # Sort piles
    # Then add up second last from the back up to n // 3
    def maxCoins(self, piles: List[int]) -> int:
        n = len(piles)
        piles.sort()
        result = 0
        for i in range(n-2, n // 3 -1, -2):
            result += piles[i]
        return result
        
# @lc code=end

