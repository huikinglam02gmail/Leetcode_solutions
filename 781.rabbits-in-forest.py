#
# @lc app=leetcode id=781 lang=python3
#
# [781] Rabbits in Forest
#

# @lc code=start
from typing import List


class Solution:
    '''
    A hash table problem
    We record the appearance of answers.
    e.g. [1,1,2]
    hash_table = [1: 2, 2: 1]
    1 appearing 2 times mean there are minimally two rabbits of same color.
    if 1 appears 3 times, it means there are 4 rabbits
    if 2 appears 1 time, it means there are (2+1) = 3 rabbits
    We can come up with this formula
    hash_table[i] = n contributes (i+1) * ((n-1) // (i+1) + 1) rabbits    
    '''
    def numRabbits(self, answers: List[int]) -> int:
        hash_table = {}
        for ans in answers: hash_table[ans] = hash_table.get(ans, 0) + 1
        result = 0
        for key in hash_table: result += (key + 1) * (1 + (hash_table[key] - 1) // (key + 1))
        return result
# @lc code=end

