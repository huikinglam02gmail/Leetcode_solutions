#
# @lc app=leetcode id=525 lang=python3
#
# [525] Contiguous Array
#

# @lc code=start
from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        hash_table = {0: [-1,-1]}
        total = 0
        for i, num in enumerate(nums):
            if num == 0: total -= 1
            else: total += 1
            if total not in hash_table:
                hash_table[total] = [i, i]
            else:
                hash_table[total][1] = i
        result = 0
        for key in hash_table.keys():
            result = max(result, hash_table[key][1] - hash_table[key][0])
        return result
# @lc code=end

