#
# @lc app=leetcode id=403 lang=python3
#
# [403] Frog Jump
#

# @lc code=start
from typing import List


class Solution:
    def canCross(self, stones: List[int]) -> bool:
        stone_table = {}
        for i, stone in enumerate(stones):
            stone_table[stone] = i
        k_set = [set() for i in range(len(stones))]
        k_set[0].add(0)
        for i,stone in enumerate(stones):
            for item in k_set[i]:
                for j in range(-1,2,1):
                    if item + j >= 1 and stone + item + j in stone_table:
                        k_set[stone_table[stone + item + j]].add(item + j)                
        return len(k_set[-1]) > 0
# @lc code=end

