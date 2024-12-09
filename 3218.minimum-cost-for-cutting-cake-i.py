#
# @lc app=leetcode id=3218 lang=python3
#
# [3218] Minimum Cost for Cutting Cake I
#

# @lc code=start
from functools import lru_cache
from typing import List


class Solution:
    @lru_cache(None)
    def dp(self, x1, y1, x2, y2):
        if x1 == x2 and y1 == y2: return 0
        result = float("inf")
        for i in range(x1, x2): result = min(result, self.horizontalCut[i] + self.dp(x1, y1, i, y2) + self.dp(i + 1, y1, x2, y2))
        for j in range(y1, y2): result = min(result, self.verticalCut[j] + self.dp(x1, y1, x2, j) + self.dp(x1, j + 1, x2, y2))
        return result


    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        self.horizontalCut = horizontalCut
        self.verticalCut = verticalCut
        return self.dp(0, 0, m - 1, n - 1)
        
# @lc code=end

