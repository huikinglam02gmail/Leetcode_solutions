#
# @lc app=leetcode id=904 lang=python3
#
# [904] Fruit Into Baskets
#

# @lc code=start
from typing import List


class Solution:
    # Sliding window + hashTable
    def totalFruit(self, fruits: List[int]) -> int:
        i, basket, result = 0, {}, 0
        for j, fruit in enumerate(fruits):
            if fruit not in basket:
                basket[fruit] = 0
            basket[fruit] += 1
            while len(basket) > 2:
                basket[fruits[i]] -= 1
                if basket[fruits[i]] == 0:
                    basket.pop(fruits[i])
                i += 1
            result = max(result, j - i + 1)
        return result
# @lc code=end

