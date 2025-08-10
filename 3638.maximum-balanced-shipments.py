#
# @lc app=leetcode id=3638 lang=python3
#
# [3638] Maximum Balanced Shipments
#

from typing import List

# @lc code=start
class Solution:
    def maxBalancedShipments(self, weight: List[int]) -> int:
        result = 0
        stack = []
        for w in weight:
            if stack and stack[-1] > w:
                stack.clear()
                result += 1
            else: stack.append(w)
        return result
# @lc code=end
