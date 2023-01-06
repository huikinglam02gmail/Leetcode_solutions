#
# @lc app=leetcode id=1833 lang=python3
#
# [1833] Maximum Ice Cream Bars
#

# @lc code=start
from typing import List


class Solution:
    # Sort the costs first
    # Then buy from the bottom until coins are used up
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        n = len(costs)
        costs.sort()
        for i in range(n):
            if coins < costs[i]:
                return i
            else:
                coins -= costs[i]
        return n
# @lc code=end

