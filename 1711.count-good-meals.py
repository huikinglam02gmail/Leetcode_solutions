#
# @lc app=leetcode id=1711 lang=python3
#
# [1711] Count Good Meals
#

# @lc code=start
from typing import List


class Solution:
    '''
    0 <= deliciousness[i] <= 2^20
    There are only 20 power of 2. So this is a twoSum problem with target = 2^0, 2^1,..., 2^20
    '''
    def countPairs(self, deliciousness: List[int]) -> int:
        hashTable = {}
        for d in deliciousness:
            if d not in hashTable:
                hashTable[d] = 0
            hashTable[d] += 1
        
        result = 0
        MOD = pow(10, 9) + 7
        for d in hashTable.keys():
            for i in range(22):
                partner = pow(2, i) - d
                if partner in hashTable:
                    if d != partner:
                        result += hashTable[d] * hashTable[partner]
                    else:
                        result += hashTable[d] * (hashTable[d] - 1)
        return (result // 2) % MOD 
        
# @lc code=end
