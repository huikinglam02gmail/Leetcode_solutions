#
# @lc app=leetcode id=2913 lang=python3
#
# [2913] Subarrays Distinct Element Sum of Squares I
#

# @lc code=start
from typing import List


class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        result = 0
        for i in range(len(nums)):
            hashTable = {}
            for j in range(i, len(nums)):
                hashTable[nums[j]] = hashTable.get(nums[j], 0) + 1
                result += len(hashTable) * len(hashTable)
        return result
# @lc code=end

