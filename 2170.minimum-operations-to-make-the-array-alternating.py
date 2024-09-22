#
# @lc app=leetcode id=2170 lang=python3
#
# [2170] Minimum Operations to Make the Array Alternating
#

# @lc code=start
from typing import List


class Solution:
    '''
    The optimal answer must be odd indices with a certain number and even indices with a certain number
    cost = len(nums) - # occur of odd Num Max - # occr of even Num Max
    However, we need to consider the case of if max occur odd key == max occur even key. Then we have to choose the minimum of (max occur odd key + second max occur even key) vs (max occur even key + second max occur odd key)
    '''
    def minimumOperations(self, nums: List[int]) -> int:
        if len(nums) < 2: return 0
        hashTables = [{}, {}]
        for i, num in enumerate(nums): hashTables[i % 2][num] = hashTables[i % 2].get(num, 0) + 1
        result = len(nums)
        kvPairs = [[[k, v] for k, v in hashTables[i].items()] for i in range(2)]
        for i in range(2): kvPairs[i].sort(key = lambda x : - x[1])
        if kvPairs[0][0][0] != kvPairs[1][0][0]:
            for i in range(2): result -= kvPairs[i][0][1]
        elif len(kvPairs[0]) == 1 and len(kvPairs[1]) == 1:
            result //= 2
        elif len(kvPairs[0]) == 1:
            result -= kvPairs[0][0][1]
            result -= kvPairs[1][1][1]
        elif len(kvPairs[1]) == 1:
            result -= kvPairs[1][0][1]
            result -= kvPairs[0][1][1]
        else:
            candidates = []
            candidates.append(kvPairs[0][0][1] + kvPairs[1][1][1])
            candidates.append(kvPairs[0][1][1] + kvPairs[1][0][1])
            result -= max(candidates)
        return result        
# @lc code=end

