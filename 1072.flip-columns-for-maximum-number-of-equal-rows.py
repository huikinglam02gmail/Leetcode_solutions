#
# @lc app=leetcode id=1072 lang=python3
#
# [1072] Flip Columns For Maximum Number of Equal Rows
#

# @lc code=start
from typing import List


class Solution:
    '''
    We see that the answer is the row pattern which has the most of identical and complement rows
    Therefore it would be advantageous to keep a hash table to save the sequence as key
    To converge complement rows, we use the first entry (row[0]) to always make it to be 0
    Then the answer is the maximum of hash values    
    '''    
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        hash_table = {}
        for row in matrix:
            key = "".join([str(x^row[0]) for x in row])
            hash_table[key] = hash_table.get(key, 0) + 1
        return max(hash_table.values())
# @lc code=end

