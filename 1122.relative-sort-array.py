#
# @lc app=leetcode id=1122 lang=python3
#
# [1122] Relative Sort Array
#

# @lc code=start
from typing import List


class Solution:
    '''
    1 <= arr1.length, arr2.length <= 1000
    We should keep hash table of value to index in arr2
    Then for elements in arr1, we sort according to hash_table[x] or x + 1000    
    '''

    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        hash_table = {}
        for i, num in enumerate(arr2): hash_table[num] = i
        return sorted(arr1, key = lambda x: hash_table.get(x, x + 1000))
# @lc code=end

