#
# @lc app=leetcode id=3572 lang=python3
#
# [3572] Maximize Y‑Sum by Picking a Triplet of Distinct X‑Values
#

# @lc code=start
from typing import List


class Solution:
    def maxSumDistinctTriplet(self, x: List[int], y: List[int]) -> int:
        hashTable = {}
        for i in range(len(x)):
            if x[i] not in hashTable: hashTable[x[i]] = y[i]
            else: hashTable[x[i]] = max(hashTable[x[i]], y[i])
        if len(hashTable) < 3: return -1
        sortedY = sorted(hashTable.values(), reverse=True)
        return sortedY[0] + sortedY[1] + sortedY[2]
# @lc code=end

