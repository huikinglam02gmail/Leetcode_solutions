#
# @lc app=leetcode id=2121 lang=python3
#
# [2121] Intervals Between Identical Elements
#

# @lc code=start
from typing import List


class Solution:
    '''
    Get hash table with ele : [indices] first
    Then for each indice i, its contribution is (numbers of indices before i - number of indices after i) * i - sum(indices before i) +  sum(indices after i)
    '''
    def getDistances(self, arr: List[int]) -> List[int]:
        hashTable = {}
        n = len(arr)
        for i, num in enumerate(arr):
            hashTable[num] = hashTable.get(num, [0])
            hashTable[num].append(hashTable[num][-1] + i)
        result = [0] * n
        for num in hashTable:
            nl = len(hashTable[num])
            for j in range(1, nl):
                i = hashTable[num][j] - hashTable[num][j - 1]
                result[i] += i * (2 * j - nl) - hashTable[num][j - 1] + hashTable[num][nl - 1] - hashTable[num][j]
        return result
# @lc code=end

