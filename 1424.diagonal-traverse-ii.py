#
# @lc app=leetcode id=1424 lang=python3
#
# [1424] Diagonal Traverse II
#

# @lc code=start
from typing import List


class Solution:
    '''
    Go through each row
    record (i+j): (i,j)
    Then sort the keys from low to high
    For each key, sort the x from high to low
    Traverse and record one by one     
    '''
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        result, m, hashTable = [], len(nums), {}
        for i in range(m):
            l = len(nums[i])
            for j in range(l):
                if i+j not in hashTable:
                    hashTable[i + j] = []
                hashTable[i + j].append([i, j])
        keys = sorted(list(hashTable.keys()))
        for key in keys:
            hashTable[key].sort(key = lambda x: -x[0])
            for x, y in hashTable[key]:
                result.append(nums[x][y])
        return result

# @lc code=end

