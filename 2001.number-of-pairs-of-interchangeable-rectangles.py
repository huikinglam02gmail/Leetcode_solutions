#
# @lc app=leetcode id=2001 lang=python3
#
# [2001] Number of Pairs of Interchangeable Rectangles
#

# @lc code=start
from typing import List


class Solution:
    '''
    Just hashTable
    '''
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        hashTable, result = {}, 0
        for a, b in rectangles: hashTable[b / a] = 1 + hashTable.get(b / a, 0)
        for v in hashTable.values(): result += v * (v - 1) // 2
        return result

        
# @lc code=end

