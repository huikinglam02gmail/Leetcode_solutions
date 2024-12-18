#
# @lc app=leetcode id=1475 lang=python3
#
# [1475] Final Prices With a Special Discount in a Shop
#

# @lc code=start
from typing import List


class Solution:
    '''
    Monotonic increasing stack
    '''

    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        result = [price for price in prices]
        n = len(prices)
        for i in range(n):
            while stack and prices[stack[-1]] >= prices[i]: result[stack.pop()] -= prices[i]
            stack.append(i)
        return result
# @lc code=end

