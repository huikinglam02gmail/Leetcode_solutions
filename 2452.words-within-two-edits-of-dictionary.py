#
# @lc app=leetcode id=2452 lang=python3
#
# [2452] Words Within Two Edits of Dictionary
#

# @lc code=start
from typing import List


class Solution:
    '''
    For each word in query, compare against each word in dictionary
    '''
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        result = []
        for query in queries:
            for word in dictionary:
                if sum([1 if c1 != c2 else 0 for c1, c2 in zip(query, word)]) <= 2: 
                    result.append(query)
                    break
        return result
        
# @lc code=end

