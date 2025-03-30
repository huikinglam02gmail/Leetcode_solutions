#
# @lc app=leetcode id=3502 lang=python3
#
# [3502] Minimum Cost to Reach Every Position
#

# @lc code=start
from typing import List


class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:
        minSoFar = float("inf")
        result = []
        for num in cost:
            minSoFar = min(minSoFar, num)
            result.append(minSoFar)
        return result

# @lc code=end

