#
# @lc app=leetcode id=1128 lang=python3
#
# [1128] Number of Equivalent Domino Pairs
#

# @lc code=start
from typing import List


class Solution:
    '''
    equivalent dominoes have the same key if sorted    
    '''
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        hash_table = {}
        for domino in dominoes:
            key = tuple(sorted(domino))
            hash_table[key] = hash_table.get(key, 0) + 1
        
        result = 0
        for v in hash_table.values(): result += v * (v - 1) // 2
        return result
# @lc code=end

