#
# @lc app=leetcode id=791 lang=python3
#
# [791] Custom Sort String
#

# @lc code=start
class Solution:
    '''
    keep a hash table of occurences of characters in order
    keep the rest in the string rest
    then construct the final string from hash table and rest    
    '''
    def customSortString(self, order: str, s: str) -> str:
        hash_table = {}
        rest = ""
        for c in s:
            if c in order:
                if c not in hash_table:
                    hash_table[c] = 0
                hash_table[c] += 1
            else:
                rest += c
        result = ""
        for c in order:
            if c in hash_table:
                for j in range(hash_table[c]):
                    result += c
        result += rest
        return result
# @lc code=end

