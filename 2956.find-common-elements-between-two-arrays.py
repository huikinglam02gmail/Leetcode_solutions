#
# @lc app=leetcode id=2956 lang=python3
#
# [2956] Find Common Elements Between Two Arrays
#

# @lc code=start
from typing import List


class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashTable1, hashTable2 = {}, {}
        for num in nums1: hashTable1[num] = hashTable1.get(num, 0) + 1
        for num in nums2: hashTable2[num] = hashTable2.get(num, 0) + 1
        result = [0, 0]
        for key in hashTable1.keys(): 
            if key in hashTable2: result[0] += hashTable1[key]
        for key in hashTable2.keys(): 
            if key in hashTable1: result[1] += hashTable2[key]    
        return result
# @lc code=end

