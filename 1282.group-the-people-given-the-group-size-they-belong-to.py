#
# @lc app=leetcode id=1282 lang=python3
#
# [1282] Group the People Given the Group Size They Belong To
#

# @lc code=start
from typing import List


class Solution:
    '''
    Keep hash table with group size as key and current open group as value
    if the current group is filled, append to result and add a new group    
    '''

    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        result, hash_table = [], {}
        for i, size in enumerate(groupSizes):
            hash_table[size] = hash_table.get(size,[]) + [i]
            if len(hash_table[size]) == size:
                result.append(hash_table[size])
                hash_table.pop(size)
        return result
# @lc code=end

