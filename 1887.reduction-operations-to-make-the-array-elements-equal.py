#
# @lc app=leetcode id=1887 lang=python3
#
# [1887] Reduction Operations to Make the Array Elements Equal
#

# @lc code=start
from typing import List


class Solution:
    '''
    Index does not matter.
    '''
    def reductionOperations(self, nums: List[int]) -> int:
        hashTable = {}
        for num in nums:
            hashTable[num] = hashTable.get(num, 0) + 1
        result = 0
        keys = sorted(hashTable.keys())
        current = 0
        n = len(keys)
        for i in range(n - 1, 0, -1):
            current += hashTable[keys[i]]
            result += current
        return result
# @lc code=end

