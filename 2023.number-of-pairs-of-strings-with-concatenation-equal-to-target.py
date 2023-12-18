#
# @lc app=leetcode id=2023 lang=python3
#
# [2023] Number of Pairs of Strings With Concatenation Equal to Target
#

# @lc code=start
from typing import List


class Solution:
    '''
    2 <= target.length <= 100
    List all possible cuts and use hash table
    '''
    def numOfPairs(self, nums: List[str], target: str) -> int:
        n, hashTable = len(target), {}
        for i in range(n - 1):
            if target[:i + 1] not in hashTable:
                hashTable[target[:i + 1]] = 0
            if target[i + 1:] not in hashTable:
                hashTable[target[i + 1:]] = 0
        
        for num in nums:
            if num in hashTable:
                hashTable[num] += 1
        
        result = 0
        for i in range(n - 1):
            if target[:i + 1] == target[i + 1:]:
                result += hashTable[target[:i + 1]] * (hashTable[target[:i + 1]] - 1)
            else:
                result += hashTable[target[:i + 1]] * hashTable[target[i + 1:]]
        return result
# @lc code=end

