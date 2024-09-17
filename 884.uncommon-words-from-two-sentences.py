#
# @lc app=leetcode id=884 lang=python3
#
# [884] Uncommon Words from Two Sentences
#

# @lc code=start
from typing import List


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1_split, s2_split = s1.split(' '), s2.split(' ')
        hash_table_1, hash_table_2 = {}, {}
        for i in s1_split:
            if i not in hash_table_1:
                hash_table_1[i] = 0
            hash_table_1[i] += 1
        for i in s2_split:
            if i not in hash_table_2:
                hash_table_2[i] = 0
            hash_table_2[i] += 1
        key_list_1 = list(hash_table_1.keys())
        key_list_2 = list(hash_table_2.keys())
        result = []
        for key in key_list_1:
            if hash_table_1[key] == 1 and key not in hash_table_2:
                result.append(key)
        for key in key_list_2:
            if hash_table_2[key] == 1 and key not in hash_table_1:
                result.append(key)
        return result
        
# @lc code=end

