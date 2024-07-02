#
# @lc app=leetcode id=350 lang=python3
#
# [350] Intersection of Two Arrays II
#

# @lc code=start
from typing import List


class Solution:
    '''
    Two hash tables to store number of occurance and output minimum occurance of intersections    
    '''
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hash_table1 = {}
        hash_table2 = {}
        for num in nums1: hash_table1[num] = hash_table1.get(num, 0) + 1             
        for num in nums2: hash_table2[num] = hash_table2.get(num, 0) + 1   
        result = []
        for key in hash_table1.keys():
            if key in hash_table2:
                for j in range(min(hash_table1[key], hash_table2[key])): result.append(key)
        return result
# @lc code=end

