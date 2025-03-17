#
# @lc app=leetcode id=2206 lang=python3
#
# [2206] Divide Array Into Equal Pairs
#

# @lc code=start
from typing import List


class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        hashTable = {}
        for num in nums: hashTable[num] = hashTable.get(num, 0) + 1
        return all(val % 2 == 0 for val in hashTable.values())
# @lc code=end

