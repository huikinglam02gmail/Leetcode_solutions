#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
from typing import List


class Solution:
    '''
    sort the strings and use that as key    
    '''
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_table = {}
        for string in strs:
            key = ''.join(sorted(string))
            if key not in hash_table: hash_table[key] = []
            hash_table[key].append(string)
        return list(hash_table.values())
# @lc code=end

