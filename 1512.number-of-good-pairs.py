#
# @lc app=leetcode id=1512 lang=python3
#
# [1512] Number of Good Pairs
#

# @lc code=start
from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        hash_table = {}
        for num in nums:
            hash_table[num] = hash_table.get(num, 0) + 1
        result = 0
        for key in hash_table.keys():
            result += hash_table[key] * (hash_table[key] - 1) // 2
        return result
# @lc code=end

