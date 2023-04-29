#
# @lc app=leetcode id=2248 lang=python3
#
# [2248] Intersection of Multiple Arrays
#

# @lc code=start
from typing import List


class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        hashTable = {}
        for numList in nums:
            for num in numList:
                hashTable[num] = hashTable.get(num, 0) + 1
        result = []
        for key in hashTable.keys():
            if hashTable[key] == len(nums):
                result.append(key)
        return sorted(result)
# @lc code=end

