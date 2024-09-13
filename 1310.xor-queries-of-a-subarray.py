#
# @lc app=leetcode id=1310 lang=python3
#
# [1310] XOR Queries of a Subarray
#

# @lc code=start
from typing import List


class Solution:
    '''
    prepare prefix XOR
    x0 ^ x1 ^ x2 ^ x3 ^ x4 ^ x5 ^ x6 = x
    x2 ^ x3 ^ x4 = x0 ^ x1 ^ x ^ x5 ^ x6
    = prefix[2]^prefix[7]^(prefix[7]^prefix[5])
    = prefix[2]^prefix[5]    
    '''


    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix = [0]
        for num in arr: prefix.append(prefix[-1] ^ num)
        
        result = []
        for left, right in queries: result.append(prefix[left] ^ prefix[right + 1])
        return result
# @lc code=end

