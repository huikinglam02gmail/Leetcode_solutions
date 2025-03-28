#
# @lc app=leetcode id=3477 lang=python3
#
# [3477] Fruits Into Baskets II
#

# @lc code=start
from typing import List


class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(baskets)
        used = [False for i in range(n)]
        result = 0
        for fruit in fruits:
            i = 0
            while i < n:
                if baskets[i] >= fruit and not used[i]:
                    used[i] = True
                    break
                else: i += 1
            if i == n: result += 1
        return result
                

# @lc code=end

