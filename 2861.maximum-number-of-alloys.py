#
# @lc app=leetcode id=2861 lang=python3
#
# [2861] Maximum Number of Alloys
#

# @lc code=start
from typing import List


class Solution:
    '''
    Assume we can make x alloys.
    For each metal type i, we need max(0, x * composition[i] - stock[i]) units of metal i.
    The total cost to make x alloys is:
        total_cost = sum(max(0, x * composition[i] - stock[i]) * cost[i] for i in range(n))
    We can use binary search to find the maximum x such that total_cost <= budget.
    '''
    def maxNumberOfAlloys(self, n: int, k: int, budget: int, composition: List[List[int]], stock: List[int], cost: List[int]) -> int:
        self.cost = cost
        l, r = 0, pow(10, 15)
        while l < r:
            mid = l + (r - l) // 2
            if self.canMakeAlloys(mid, n, k, composition, stock, budget):
                l = mid + 1
            else:
                r = mid
        return l - 1

    def canMakeAlloys(self, x: int, n: int, k: int, composition: List[List[int]], stock: List[int], budget: int) -> bool:
        for i in range(k):
            total_cost = 0
            for j in range(n):
                total_cost += max(0, x * composition[i][j] - stock[j]) * self.cost[j]
            if total_cost <= budget: return True
        return False
# @lc code=end

