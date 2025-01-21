#
# @lc app=leetcode id=2808 lang=python3
#
# [2808] Minimum Seconds to Equalize a Circular Array
#

# @lc code=start
from typing import List


class Solution:
    def minimumSeconds(self, nums: List[int]) -> int:
        hashTable = {}
        for i, num in enumerate(nums + nums): 
            if num not in hashTable: hashTable[num] = []
            hashTable[num].append(i)
        result = float("inf")
        for key in hashTable:
            current = 0
            for i in range(len(hashTable[key]) // 2): current = max(current, (hashTable[key][i + 1] - hashTable[key][i]) // 2)
            result = min(result, current)
        return result
# @lc code=end

