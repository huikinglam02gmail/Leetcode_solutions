#
# @lc app=leetcode id=2744 lang=python3
#
# [2744] Find Maximum Number of String Pairs
#

# @lc code=start
from typing import List


class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        result = 0
        hashTable = {}
        for word in words:
            if word in hashTable: result += hashTable[word]
            hashTable[word[::-1]] = hashTable.get(word[::-1], 0) + 1
        return result
# @lc code=end

