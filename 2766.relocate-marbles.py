#
# @lc app=leetcode id=2766 lang=python3
#
# [2766] Relocate Marbles
#

# @lc code=start
from typing import List


class Solution:
    def relocateMarbles(self, nums: List[int], moveFrom: List[int], moveTo: List[int]) -> List[int]:
        hashTable = {}
        for num in nums: hashTable[num] = hashTable.get(num, 0) + 1
        for f, t in zip(moveFrom, moveTo):
            if f != t:
                hashTable[t] = hashTable.get(t, 0) + hashTable.get(f, 0)
                if f in hashTable: hashTable.pop(f)
        return sorted(hashTable.keys())
# @lc code=end
