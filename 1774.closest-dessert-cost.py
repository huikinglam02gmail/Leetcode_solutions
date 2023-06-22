#
# @lc app=leetcode id=1774 lang=python3
#
# [1774] Closest Dessert Cost
#

# @lc code=start
from typing import List


class Solution:
    '''
    According to the rules:
    There must be exactly one ice cream base -> so must choose one out of baseCosts
    You can add one or more types of topping or have no toppings at all. There are at most two of each type of topping. -> for each toppingCost, it can be 0 *, 1* and 2* toppingCost[i]
    Time complexity: O(n) * O(3 ^ m) ~ at most O(590490)
    '''
    def backtracking(self, i, diff):
        if (diff > 0 and abs(diff) < self.resultDiff) or (diff <= 0 and abs(diff) <= self.resultDiff):
            self.result = self.target + diff
            self.resultDiff = abs(diff)
        if diff < 0 and i < len(self.toppingCosts):
            for j in range(3):
                self.backtracking(i + 1, diff + j * self.toppingCosts[i])

    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        self.baseCosts, self.toppingCosts, self.target = baseCosts, toppingCosts, target
        self.result, self.resultDiff = -1, float('inf')
        for i in range(len(baseCosts)):
            self.backtracking(0, baseCosts[i] - target)
        return self.result
# @lc code=end

