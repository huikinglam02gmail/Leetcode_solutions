#
# @lc app=leetcode id=1726 lang=python3
#
# [1726] Tuple with Same Product
#

# @lc code=start
from typing import List


class Solution:
    '''
    Go through all pairs: 1 <= nums.length <= 1000, save the products inside a hashTable with count of pairs
    For each product (hashTable[p] = n) the first number can be any of them -> 2 * n
    The second number can only be 1 -> 2 * n
    The third number can be 1 of (2* n - 2) -> 4 * n * ( n - 1)
    The last number can be 1 of 1 -> 4 * n * ( n - 1)

    '''
    def tupleSameProduct(self, nums: List[int]) -> int:
        hashTable = {}
        n = len(nums)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] * nums[j] not in hashTable:
                    hashTable[nums[i] * nums[j]] = 0
                hashTable[nums[i] * nums[j]] += 1
        result = 0
        for v in hashTable.values():
            result += 4 * v * (v - 1)
        return result
# @lc code=end

