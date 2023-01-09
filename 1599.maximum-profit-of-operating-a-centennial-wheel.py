#
# @lc app=leetcode id=1599 lang=python3
#
# [1599] Maximum Profit of Operating a Centennial Wheel
#

# @lc code=start
from typing import List


class Solution:
    # Just simulate the process
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        profit, maxsofar, result, waiting, turn = 0, 0, -1, 0, 0
        while turn < len(customers) or waiting > 0:
            if turn < len(customers):
                waiting += customers[turn]
            board = min(4, waiting)
            profit += board * boardingCost - runningCost
            if profit > maxsofar:
                maxsofar = profit
                result = turn + 1
            waiting -= board
            turn += 1
        return result
# @lc code=end

