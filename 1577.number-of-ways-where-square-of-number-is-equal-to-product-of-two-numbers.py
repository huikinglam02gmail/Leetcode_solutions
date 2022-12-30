#
# @lc app=leetcode id=1577 lang=python3
#
# [1577] Number of Ways Where Square of Number Is Equal to Product of Two Numbers
#

# @lc code=start
from typing import List


class Solution:
    # Get appearance of each number in hash table
    # Then count all the pairs
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        hashTable1, hashTable2 = {}, {}
        for num in nums1:
            if num not in hashTable1:
                hashTable1[num] = 0
            hashTable1[num] += 1
        for num in nums2:
            if num not in hashTable2:
                hashTable2[num] = 0
            hashTable2[num] += 1
        result = 0
        for key1 in list(hashTable1.keys()):
            for key2 in list(hashTable2.keys()):
                 if (key1 * key1) % key2 == 0 and key1 * key1 // key2 in hashTable2:
                    if key1 == key2:
                        result += hashTable1[key1] * hashTable2[key2] * (hashTable2[key2] - 1)
                    else:
                        result += hashTable1[key1] * hashTable2[key2] * hashTable2[key1 * key1 // key2]
        for key2 in list(hashTable2.keys()):
            for key1 in list(hashTable1.keys()):
                 if (key2 * key2) % key1 == 0 and key2 * key2 // key1 in hashTable1:
                    if key2 == key1:
                        result += hashTable2[key2] * hashTable1[key1] * (hashTable1[key1] - 1)
                    else:
                        result += hashTable2[key2] * hashTable1[key1] * hashTable1[key2 * key2 // key1]
        return result // 2

# @lc code=end

