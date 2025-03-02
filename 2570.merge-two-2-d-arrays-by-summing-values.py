#
# @lc app=leetcode id=2570 lang=python3
#
# [2570] Merge Two 2D Arrays by Summing Values
#

# @lc code=start
from typing import List


class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        hashTable = {}
        for id, val in nums1: hashTable[id] = hashTable.get(id, 0) + val
        for id, val in nums2: hashTable[id] = hashTable.get(id, 0) + val
        return sorted([[k, v] for k, v in hashTable.items()], key = lambda x: x[0])
# @lc code=end

