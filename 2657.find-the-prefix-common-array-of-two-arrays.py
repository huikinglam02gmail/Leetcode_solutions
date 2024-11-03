#
# @lc app=leetcode id=2657 lang=python3
#
# [2657] Find the Prefix Common Array of Two Arrays
#

# @lc code=start
from typing import List


class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        ASet, BSet = set(), set()
        result = []
        for numA, numB in zip(A, B):
            ASet.add(numA)
            BSet.add(numB)
            result.append(len(ASet.intersection(BSet)))
        return result
# @lc code=end

