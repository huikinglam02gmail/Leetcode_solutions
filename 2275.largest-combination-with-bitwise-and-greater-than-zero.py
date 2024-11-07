#
# @lc app=leetcode id=2275 lang=python3
#
# [2275] Largest Combination With Bitwise AND Greater Than Zero
#

# @lc code=start
from typing import List


class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        hash_table = {}
        for candidate in candidates:
            binary_reverse = bin(candidate)[2:][::-1]
            for i in range(len(binary_reverse)):
                if binary_reverse[i] == '1':
                    if i not in hash_table: hash_table[i] = 1
                    else: hash_table[i] += 1
        return max(hash_table.values())
# @lc code=end

