#
# @lc app=leetcode id=823 lang=python3
#
# [823] Binary Trees With Factors
#

# @lc code=start
from typing import List


class Solution:
    '''
    Construct all possible trees from the bottom
    We first consider all pairs (including self) inside arr to look for possible mapping
    For example, [2, 4, 5, 10]
    2*2 = 4, 2*5 = 10
    First level: only the node itself
    Second level: consider left and right subtrees. we can only consider trees with root that is product of other two elements in the array
    Therefore trees with root 4 has [4], [4,2,2] = 1+1
    Trees with root 10 has [10], [10,5,2] and [10,2,5]
    We sort the keys from small to large    
    '''

    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        hash_table = {}
        for i in arr:
            hash_table[i] = 1
        keys = list(hash_table.keys())
        keys.sort()
        products = {}
        for i in range(len(keys)):
            for j in range(i, len(keys)):
                if keys[i]*keys[j] in hash_table:
                    if keys[i]*keys[j] not in products:
                        products[keys[i] * keys[j]] = []
                    products[keys[i]*keys[j]].append([keys[i],keys[j]])
        result, MOD = 0, pow(10,9) + 7
        for key in keys:
            if key in products:
                for item in products[key]:
                    hash_table[key] += hash_table[item[0]] * hash_table[item[1]]
                    if item[0] != item[1]:
                        hash_table[key] += hash_table[item[0]] * hash_table[item[1]]
                    hash_table[key] %= MOD
            result += hash_table[key]
            result %= MOD
        return result
# @lc code=end

